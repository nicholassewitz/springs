
# coding: utf-8

# ## Data Exploration to Predict Gallery Tier
# ### First step towards building an objective Gallery Qualification Score
# **Author: Nicholas Sewitz
# Contributors: Anil Bawa-Cavia, Will Goldstein**
#
# This notebook processes certain predetermined features that we believe are predictive of the qualitative gallery tier score applied by the GFI team. The goal is to identify what features and models should be used to build a more ambitious objective qualification score.

# In[207]:


import sys, os
import datetime
sys.path.append(os.environ['minotaur'])

import os.path
import http
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from socket import timeout
import boto3
import gzip
import io


from __future__ import print_function

from pprint import pprint
from time import time
import logging


import yaml

get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

import pandas as pd
import numpy as np

from pylab import rcParams
rcParams['figure.figsize'] = 14,3

from dbs import redshift
redshift.connect()

from __future__ import division

from pygeocoder import Geocoder
from geopy.distance import vincenty

from slugify import slugify

from sklearn.linear_model import LogisticRegression, LinearRegression, SGDRegressor, SGDClassifier
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, scale
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, accuracy_score
from scipy.stats import randint
from sklearn.pipeline import Pipeline
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from gensim.models import doc2vec
from collections import namedtuple


# #### Locations from Bearden (In Progress)

# In[208]:


bearden_locations = redshift.execute("""
SELECT website AS "domain",
       latitude,
       longitude
FROM bearden_exports.organizations
WHERE latitude IS NOT NULL and latitude != 0""")


# #### Artsy Partners

# In[209]:


partners = redshift.execute("""
SELECT website as "domain"
FROM gravity.partners
where website is not null
""")


# #### Artsy Partners with Artists

# In[210]:


partner_artists = redshift.execute("""
SELECT
       p.website AS "domain",
       a.slug AS artist_slug
FROM gravity.partners p
  LEFT JOIN gravity.partner_artists pa ON p.id = pa.partner_id
  LEFT JOIN gravity.artists a ON pa.artist_id = a.id
  """)


# #### Artist Bids and Inquiries on Artsy

# In[211]:


artsy_artists = redshift.execute("""
SELECT artists.slug AS artist_slug,
       COUNT(DISTINCT inquiry_requests.inquiry_id ) AS "inquiry_requests_count",
       SUM(sale_artworks.artsy_bid_count) AS "bid_count"
FROM gravity.artists
  LEFT JOIN analytics.artworks ON artworks.artist_id = artists.id
  LEFT JOIN analytics.inquiry_requests AS inquiry_requests
         ON artworks.id = inquiry_requests.inquireable_id
        AND inquiry_requests.inquireable_type = 'Artwork'
  LEFT JOIN analytics.sale_artworks ON sale_artworks.artwork_id = artworks.id
GROUP BY 1
""")


# #### Gallery Tier (From Salesforce)

# In[212]:


salesforce_partners = redshift.execute("""
SELECT website as domain,
       gallery_tier
FROM analytics.salesforce_companies
WHERE website is not null and website != '' and gallery_tier is not null and gallery_tier != '' and "type" IN ('Gallery','Design Gallery')
""")


# #### No Longer in Business

# In[213]:


closed = redshift.execute("""
SELECT sc.website as domain,disqualified_reason
FROM analytics.salesforce_companies sc
WHERE sc."type" IN ('Gallery', 'Design Gallery')
AND sc.website IS NOT NULL
""")


# In[ ]:





# In[214]:


redshift.close()


# #### Bearden Artists Rosters

# In[215]:


artists = pd.read_csv('artist_rosters.csv',index_col='domain')


# In[216]:


del artists['organization_type']
del artists['notes']
del artists['specialization']
del artists['updated_website']
del artists['roster_url']
del artists['roster_type']


# #### Artsy Artist Page Search Metrics

# In[217]:


search = pd.read_csv('artist_search_analytics.csv')


# In[218]:


del search['CTR']
del search['Position']


# #### Artist Keyword Search Volume

# In[219]:


search_volume = pd.read_csv('artist-organic-search-volume.csv')


# In[ ]:





# #### Begin Wrangling

# In[ ]:





# In[220]:


bearden_artists = artists.iloc[:,2:].copy()


# In[221]:


bearden_artists = pd.DataFrame(bearden_artists.unstack().dropna()).reset_index()


# In[222]:


bearden_artists['artist_slug'] = bearden_artists[0].apply(lambda x: slugify(x))
bearden_artists['source'] = 'bearden'


# In[223]:


search_volume['artist_slug'] = search_volume['Keyword'].apply(lambda x: str(x))
search_volume['artist_slug'] = search_volume['artist_slug'].apply(lambda x: slugify(x))
del search_volume['Keyword']


# In[224]:


import re

def strip_domain(website):
    website = website.replace("http://","")
    website = website.replace("http:","")
    website = website.replace("https://","")
    website = website.replace("http:","")
    website = re.sub(r'(www.)(?!com)',r'',website)
    urls = website.split('/')[0]
    urls = urls.replace("]","")
    urls = urls.replace("[","")
    urls = urls.strip('.')
    return urls
bearden_artists.domain = bearden_artists.domain.apply(strip_domain)
salesforce_partners.domain = salesforce_partners.domain.apply(strip_domain)
partners.domain = partners.domain.apply(strip_domain)
closed.domain = closed.domain.apply(strip_domain)


# In[225]:


bearden_artists = bearden_artists[['domain','artist_slug','source']].copy()
bearden_artists = bearden_artists.drop_duplicates(subset=['domain','artist_slug'], keep='last')
closed = closed.drop_duplicates('domain')


# In[226]:


partner_artists.domain = partner_artists.domain.astype(str)
partner_artists.domain = partner_artists.domain.apply(strip_domain)
partner_artists['source'] = 'partners'



# In[228]:


all_artists = pd.concat([bearden_artists, partner_artists])


# In[229]:


all_artists = all_artists.drop_duplicates(subset=['domain','artist_slug'], keep='last')


# In[230]:


artsy_artists = artsy_artists.dropna()


# In[231]:


all_artists['on_artsy'] = all_artists.artist_slug.isin(artsy_artists.artist_slug)


# In[232]:


search['artist_slug'] = search.Pages.apply(lambda x: re.split('\\/artist/\\b',x)[-1])
del search['Pages']


# In[233]:


artists_with_search = all_artists.merge(search, how="left", left_on='artist_slug', right_on='artist_slug')


# In[234]:


# There are 10k artists with search volume that match with the partner artists dataset

test = artists_with_search.merge(search_volume, how="inner", left_on='artist_slug', right_on='artist_slug')
test.drop_duplicates('artist_slug').shape


# In[235]:


artists_with_search = artists_with_search.merge(search_volume, how="left", left_on='artist_slug', right_on='artist_slug')


# In[236]:


artists_with_search_bids_inquiries = artists_with_search.merge(artsy_artists, how="left", left_on='artist_slug', right_on='artist_slug')


# In[237]:


# artists_with_search_bids_inquiries.domain = artists_with_search_bids_inquiries.domain.str.strip('.')
# salesforce_partners.domain = salesforce_partners.domain.str.strip('.')


# In[238]:


domains_with_metrics = artists_with_search_bids_inquiries[['domain','Clicks','Impressions','inquiry_requests_count','bid_count','on_artsy','search_volume']].groupby('domain').sum()


# In[239]:


slug_count = pd.DataFrame(artists_with_search_bids_inquiries[['domain','artist_slug']].groupby('domain').count())
domains_with_metrics = domains_with_metrics.merge(slug_count, how="left", left_index=True, right_index=True)
salesforce_partners = salesforce_partners.drop_duplicates('domain')


# In[240]:


domains_with_metrics_and_demographic = salesforce_partners.merge(domains_with_metrics, how="left", left_on="domain",right_index=True)
domains_with_metrics_and_demographic = domains_with_metrics_and_demographic.fillna(np.nan)


# #### Minimum Distance to Art City

# In[ ]:





# In[241]:


bearden_locations.domain = bearden_locations.domain.apply(strip_domain)
bearden_locations = bearden_locations.drop_duplicates('domain')


# In[242]:


domain_locations = bearden_locations[['domain','latitude','longitude']].copy()

domain_locations['lat_long'] = list(zip(domain_locations.latitude, domain_locations.longitude))
del domain_locations['latitude']
del domain_locations['longitude']


# In[243]:


ny = (40.7465, 74.0014)
london = (51.4851, 0.1749)
los_angeles = (34.0900, 118.3617)
paris = (48.8587, 2.3588)
berlin = (52.5194, 13.4067)
hong_kong = (22.3964, 114.1095)
miami = (25.7617, 80.1918)
venice = (45.4408, 12.3155)
basel = (47.5596, 7.5886)
sao_paulo = (23.5505, 46.6333)
melbourne = (37.8136, 144.9631)
mexico_city = (19.4326, 99.1332)


# In[244]:


domain_locations['distance_to_ny'] = domain_locations.lat_long.apply(lambda x: vincenty(x, ny).miles)
domain_locations['distance_to_london'] = domain_locations.lat_long.apply(lambda x: vincenty(x, london).miles)
domain_locations['distance_to_los_angeles'] = domain_locations.lat_long.apply(lambda x: vincenty(x, los_angeles).miles)
domain_locations['distance_to_paris'] = domain_locations.lat_long.apply(lambda x: vincenty(x, paris).miles)
domain_locations['distance_to_berlin'] = domain_locations.lat_long.apply(lambda x: vincenty(x, berlin).miles)
domain_locations['distance_to_hong_kong'] = domain_locations.lat_long.apply(lambda x: vincenty(x, hong_kong).miles)
domain_locations['distance_to_miami'] = domain_locations.lat_long.apply(lambda x: vincenty(x, miami).miles)
domain_locations['distance_to_venice'] = domain_locations.lat_long.apply(lambda x: vincenty(x, venice).miles)
domain_locations['distance_to_basel'] = domain_locations.lat_long.apply(lambda x: vincenty(x, basel).miles)
domain_locations['distance_to_sao_paulo'] = domain_locations.lat_long.apply(lambda x: vincenty(x, sao_paulo).miles)
domain_locations['distance_to_melbourne'] = domain_locations.lat_long.apply(lambda x: vincenty(x, melbourne).miles)
domain_locations['distance_to_mexico_city'] = domain_locations.lat_long.apply(lambda x: vincenty(x, mexico_city).miles)


# In[245]:


distance_columns = [col for col in domain_locations if col.startswith('distance_to_')]
domain_locations['min_distance_to_art_city'] = domain_locations[distance_columns].min(axis=1)
galleries_w_demographic_metric_location = domains_with_metrics_and_demographic.merge(domain_locations[['domain','min_distance_to_art_city']], how="left", left_on="domain",right_on="domain")
galleries_w_demographic_metric_location = galleries_w_demographic_metric_location.merge(closed,how="left",left_on="domain",right_on="domain")
galleries_w_demographic_metric_location['disqualified_reason'] = galleries_w_demographic_metric_location['disqualified_reason'].astype(str)
galleries_w_demographic_metric_location['is_closed'] = [True if x.startswith('No Longer') else False for x in galleries_w_demographic_metric_location['disqualified_reason']]
galleries_open_w_all_metrics = galleries_w_demographic_metric_location[galleries_w_demographic_metric_location['is_closed'] == False].copy()


# #### Limit DF to only include galleries with minimum # of features

# In[ ]:





# In[247]:


# limit dataframe to only galleries that have a tier and at least 3 features

df = galleries_open_w_all_metrics.copy()
df_with_many_features= df[(df.gallery_tier.notnull()) & (df.min_distance_to_art_city.notnull()) & (df.artist_slug > 0)]
df_with_less_features = df[(df.gallery_tier.notnull())]


partners['partner_on_artsy'] = True
partners = partners.drop_duplicates('domain')


# In[248]:


# 1250 galleries have most of the features and are not on artsy, with tier

df_with_less_features = df_with_less_features.merge(partners,how="left",left_on="domain",right_on="domain").copy()
df_with_less_features.partner_on_artsy = df_with_less_features.partner_on_artsy.fillna(False)

df_with_many_features = df_with_many_features.merge(partners,how="left",left_on="domain",right_on="domain").copy()
df_with_many_features.partner_on_artsy = df_with_many_features.partner_on_artsy.fillna(False)


# In[249]:


def qualify(x):
    if x == '1':
        return "very_qualified"
    elif x == '2':
        return "very_qualified"
    elif x == '3':
        return "very_qualified"
    elif x == '4':
        return "qualified"
    elif x == '5':
        return "not_qualified"

def numeralize(x):
    if x == '1':
        return 100
    elif x == '2':
        return 100
    elif x == '3':
        return 100
    elif x == '4':
        return 50
    elif x == '5':
        return 0

df_with_many_features['qualified'] = df_with_many_features.gallery_tier.apply(lambda x: qualify(x))
df_with_less_features['qualified'] = df_with_less_features.gallery_tier.apply(lambda x: qualify(x))

df_with_many_features.gallery_tier = df_with_many_features.gallery_tier.apply(lambda x: numeralize(x))
df_with_less_features.gallery_tier = df_with_less_features.gallery_tier.apply(lambda x: numeralize(x))


# In[251]:


if sys.version_info[0] < 3:
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x

# get your credentials from environment variables
aws_id = os.environ['AWS_ID']
aws_secret = os.environ['AWS_SECRET']

s3 = boto3.client('s3', aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret)

bucket_name = 'artsy-data'


# In[252]:


object_key = 'temp/many_text.csv.gz'
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

many_text = pd.read_csv(StringIO(csv_string))


# In[253]:


object_key = 'temp/less_text.csv.gz'
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

less_text = pd.read_csv(StringIO(csv_string))


# In[254]:


df_with_many_text = df_with_many_features.merge(many_text,how='left',left_on='domain',right_on='domain')
df_with_less_text = df_with_less_features.merge(less_text,how='left',left_on='domain',right_on='domain')

del df_with_many_text['Unnamed: 0']
del df_with_less_text['Unnamed: 0']


# In[255]:


csv_buffer = StringIO()
df_with_many_text.to_csv(csv_buffer)
s3_resource = boto3.resource('s3',aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret)
s3_resource.Object(bucket_name, 'temp/df_with_many_text.csv').put(Body=csv_buffer.getvalue())


# In[256]:


csv_buffer = StringIO()
df_with_less_text.to_csv(csv_buffer)
s3_resource = boto3.resource('s3',aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret)
s3_resource.Object(bucket_name, 'temp/df_with_less_text.csv').put(Body=csv_buffer.getvalue())


# #### Website Text Parse Wrangle

# In[1]:


# url_keywords = ["about", "fairs", "exhibitions", "artists", "home"]

# def site_text(url):
#     try:
#         sub_urls = []
#         url_full = "http://www."+ str(url).strip()
#         print(url_full)
#         page = urlopen(url_full, timeout=8)
#         soup = BeautifulSoup(page, "html.parser")
#         links = soup.find_all('a', href=True)
#         links = [link['href'] for link in links]
#         lower_links = [x.lower() for x in links]
#         link_dict = dict(zip(links, lower_links))
#         sub_urls = [k for k, v in link_dict.items() if any(xs in v for xs in url_keywords)  ]
#         sub_urls = list(set(sub_urls))
#         raw = soup.get_text()
#         num = 0

#         for sub_url in sub_urls:
#             try:
#                 if "http" in sub_url:
#                     sub_url
#                     if sub_url.count("/") > 3:
#                         break
#                 elif url_full.endswith("/"):
#                     sub_url = url_full + sub_url
#                     if sub_url.count("/") > 3:
#                         break
#                 else:
#                     if sub_url.startswith("/"):
#                         sub_url = url_full + sub_url
#                         if sub_url.count("/") > 3:
#                             break
#                     else:
#                         sub_url = url_full + "/" + sub_url
#                         if sub_url.count("/") > 3:
#                             break
#                 print("sub_url: " + sub_url)
#                 sub_page = urlopen(sub_url, timeout=8)
#                 sub_soup = BeautifulSoup(sub_page, "html.parser")
#                 raw += sub_soup.get_text()
#                 num = num + 1
#                 if num == 5:
#                     break

#             except urllib.error.URLError as e:
#                 if hasattr(e, 'reason'): # <--
#                     print('We failed to reach a server.')
#                     print('Reason: ', e.reason)
#                 elif hasattr(e, 'code'): # <--
#                     print('The server couldn\'t fulfill the request.')
#                     print('Error code: ', e.code)
#             except http.client.HTTPException as e:
#                 if hasattr(e, 'reason'): # <--
#                     print('We failed to reach a server.')
#                     print('Reason: ', e.reason)
#                 elif hasattr(e, 'code'): # <--
#                     print('The server couldn\'t fulfill the request.')
#                     print('Error code: ', e.code)
#             except timeout:
#                 print("timeout")
#             except KeyboardInterrupt:
#                 raise
#             except:
#                 print("unknown")

#         return raw

#     except urllib.error.URLError as e:
#         if hasattr(e, 'reason'): # <--
#             print('We failed to reach a server.')
#             print('Reason: ', e.reason)
#         elif hasattr(e, 'code'): # <--
#             print('The server couldn\'t fulfill the request.')
#             print('Error code: ', e.code)
#     except http.client.HTTPException as e:
#         if hasattr(e, 'reason'): # <--
#             print('We failed to reach a server.')
#             print('Reason: ', e.reason)
#         elif hasattr(e, 'code'): # <--
#             print('The server couldn\'t fulfill the request.')
#             print('Error code: ', e.code)
#     except timeout:
#         print("timeout")
#     except KeyboardInterrupt:
#         raise
#     except:
#         print("unknown")

# http://jmausolf.github.io/code/Analyzing_Text_in_Python/#analyzing_text_in_python



# In[ ]:
