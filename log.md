This is a brief catalogue of the work we shipped each week.  It tends not to include more ephemeral one-off work, or any of the substantial number of minor updates and changes we make each week.  Instead, it provides a high level overview of the PRs and documents that illustrate our steady march to a robust and impactful data platform.

# Analytics Sprint Log

November 17
-----
_Create revenue recognition table_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/issues/704
https://github.com/artsy/fulcrum/pull/730

_Curation schema for the Gucci event_ - [Will Goldstein](github.com/wrgoldstein)

_Who has saved artworks in auctions since the "Watch Lot" feature rolled out?_ - [Mike Hromchak](github.com/mikehrom)
> (since Aug 1 approx.) 

_Causality events payload now has clientMetadata containing user agent info; use this to add device type to unified bidding report._ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/735

_Change to payment requests explore_ - 
> caroline.perkins [3:27 PM] 
Hey Analytics! Can I put in a small request to change "Payment Request Line Items USD Amount" from a dimension to a measure? Not urgent of course, but @ani this is somewhat related to what we discussed re reporting transactional vs non-transactional GMV in Looker. Right now, we don't include the line item amounts into our calculation of total inquiry purchase GMV. https://artsy.looker.com/explore/artsy/payment_requests?qid=kWDBeefGINW9BQUAaZAQRD&toggle=fil

_Spec out AB test for /collect_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/collector-experience/issues/691#issuecomment-343592497

_QA eigen_ - [Ani Petrov](github.com/anipetrov)

_Deep dive into performance of CRM vol 1_ - [Ani Petrov](github.com/anipetrov)


November 10
-----
_Market data AB test_ - [Ani Petrov](github.com/anipetrov)
> Estimate time for running the test


_Enrich mkto partner_apps_ - [Ani Petrov](github.com/anipetrov)
> cat.finsness [3:15 PM] 
hey would it possible to add in the marketo `referrer url` on the partnership_applications table? the current use case is trying to see the conversion of the new partnership page here https://artsy.looker.com/looks/4829?toggle=fil but doing it by form name / id would not be accurate since our GP page shared a form with another lp at one point
> 
[3:15] 
(this is non-urgent but would be great to be able to do this report)

_Board deck: exploring new lines of business_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)

_Hiring_ - [Will Goldstein](github.com/wrgoldstein)

_Support B2B goals and projections_ - [Ani Petrov](github.com/anipetrov)


November 3
-----
_Add partner and artists article mentions to https://artsy.looker.com/looks/4580 or otherwise make available to gp_ - [Mike Hromchak](github.com/mikehrom)
> asked for by @jeffrey
> https://github.com/artsy/fulcrum/pull/734
https://github.com/artsy/looker/pull/898

_Support for new Eigen instrumentation schema_ - [Ani Petrov](github.com/anipetrov)

_Market data support_ - [Ani Petrov](github.com/anipetrov)
> 
commercial activity for top auction results artists: https://artsy.looker.com/sql/m4fwh49bwcbvjm
> pageviews for top auction results artists: https://artsy.looker.com/sql/spsvkh8qvzky7d
> over the last month, 3,235 web inquiries, 536,837 web views of artworks by these artists; that means sample size of ~265k per variation, or about a month of testing
> https://cl.ly/3v1t34071X1P

_Board deck asks_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)


October 27
-----
_marketing b2b: reporting help for Cat_ - [Ani Petrov](github.com/anipetrov)

_Product support for email marketing_ - [Ani Petrov](github.com/anipetrov)

_emission instrumentation support_ - [Ani Petrov](github.com/anipetrov)

_Quarterly option for bid count measure in Looker_ - [Mike Hromchak](github.com/mikehrom)
> https://artsy.looker.com/explore/artsy/sales?qid=g8MZkMucMycdMjwet67QCU&toggle=fil,vis

_Surface partner show views (the whole partner analytics email?) in looker_ - [Mike Hromchak](github.com/mikehrom)
> a request from multiple GR members to look at partner show pageviews and other stats report in the monthly analytics emails
> [compare to fairs analytics email]
> https://github.com/artsy/fulcrum/pull/716
https://github.com/artsy/looker/pull/885


_Hiring_ - [Will Goldstein](github.com/wrgoldstein)

_Support for Gallery Weekends and Country Partnerships_ - [Ani Petrov](github.com/anipetrov)

_Sessions_ - [Ani Petrov](github.com/anipetrov)

_Product support for new artist page_ - [Ani Petrov](github.com/anipetrov)


October 20
-----
_How many ACBs will we need to hit forecasted GMV?_ - [Mike Hromchak](github.com/mikehrom)

_Create tracking schema for articles2: => click, impression (check with owen)_ - [Will Goldstein](github.com/wrgoldstein)

_board deck support_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)

_Hiring_ - [Will Goldstein](github.com/wrgoldstein)

_Sessions_ - [Ani Petrov](github.com/anipetrov)


October 13
-----
_GP Pitch Support_ - [Will Goldstein](github.com/wrgoldstein)
> ## October Sales Data:
> MoM and YoY in confirmed GMV 
MoM and YoY # of confirmed sales
Average confirmed sale value in 2017
Confirmed sales vs total inquiries delivered in 2017 ( I know this won't be a true conversion rate), include 5.7x multiple
Traffic increases MoM and YoY
> ## Partner success deep dive:
> We created a Look to represent the kind of data Alexa wants: https://artsy.looker.com/explore/artsy/partners?qid=3PnfzAEsEQWSSVzl0wWsww
> But she would like to make the following changes
> - just the past 12 months of data
- add partner impressions
- add cms sessions
- add avg # works uploaded per month
- add response rate in hours, (within 7 days?)
> ## Plan specific
> - what are the data points that sell the top tier plans? (inquiries by plan, purchases by plan, impressions by plan)


_Use adjust install attributed to set account creation medium on users_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/708

_Update Sailthru explore in looker so that we are able to match conversions to the blast id in the utm_source (as well as the utm_campaign, which is what we currently have)._ - [Mike Hromchak](github.com/mikehrom)
> currently, we match conversions to email blasts by comparing the numbers at the start of a utm_campaign to the blast id of an email (they should match); we are going to start slowly switching over our email tracking so that we will be matching in the exact same way on the utm_source but there will be both things happening for a period of time while we switch over.  
> We would like to look at the utm_campaign AND the source to match for that period of time; there's no way the params would ever BOTH have it and there's no way it could have conflicting blast ids.
> 
addressed in: https://github.com/artsy/fulcrum/pull/712

_Hiring_ - [Will Goldstein](github.com/wrgoldstein)

_Ani OOO_ - 


October 6
-----
_[1] new consignments fields in Looker_ - [Mike Hromchak](github.com/mikehrom)

_New artist page filters design analysis_ - [Mike Hromchak](github.com/mikehrom)
> From Brian: 
" we’re considering the usefulness of being able to filter works on the artist page by those that are at auction currently vs those available from a gallery/institution. am hoping to get a sense for the average number of auction lots that are active at any given time for an artist, taking into account seasonality, etc. if there’s only a handful of active auction lots it probably means we dont need this filter so any data you guys can provide here would be very helpful. "
> https://cl.ly/0M092D2z3p0W
> Addressed here: https://github.com/artsy/minotaur/pull/263


_Associate artworks to auctions using CMS fields for Gallery Auctions_ - [Mike Hromchak](github.com/mikehrom)
> [via Leslie, in auctions]
> We're hoping to be able to export all of their existing artworks in one look that pulls all artwork metadata needed for our auction upload template. Would you be able to help us add the following CMS fields as filters? 
> - Manufacturer
- Dimension Metric (already there)
- Signature
- Provenance (already there)
- Literature
- Series
- Publisher
> https://github.com/artsy/looker/pull/869
https://github.com/artsy/fulcrum/pull/709
> the following are excluded for now and will be added later once we can properly clean the text in the fields:
- Additional Information
- Exhibition History
https://github.com/artsy/fulcrum/pull/711
https://github.com/artsy/looker/pull/872

_GR + Analytics discussion_ - [Will Goldstein](github.com/wrgoldstein)
> What should we prioritize for Q4?
> How should we understand the churn analysis that has been done and how should we move forward.

_CRT blog post_ - [Will Goldstein](github.com/wrgoldstein)

_is the Downloadable dimension on Artworks broken?_ - [Will Goldstein](github.com/wrgoldstein)
> see Anna's help channel question
> this field is always null in the artworks table

_GP + Analytics discussion_ - [Will Goldstein](github.com/wrgoldstein)
> What should we work on in Q4?

_Analytics GDPR survey_ - [Will Goldstein](github.com/wrgoldstein)

_CRM + Analytics (Vendor data discussion)_ - [Will Goldstein](github.com/wrgoldstein)
> - Formulate a doc summarizing discussion in #data.
> https://docs.google.com/document/d/1sbRbVpTehEYxKn8G5iW94fggc-Lh1FxVbxT034slnro/edit#heading=h.lt9tpukuhee6
> - Discuss with SP.


_Ani OOO_ - 


September 29
-----
_Spec the work required to replicate the Accounting Team's Revenue model in Looker_ - [Will Goldstein](github.com/wrgoldstein)

_[4] Buyer retention analysis (continued)_ - [Mike Hromchak](github.com/mikehrom)
> - Cleaned up poison rate analysis
- Added more to session and pageview counts between account creation and first inquiry
- Began analysis on activity leading up to first inquiry
> Full conversation here: https://github.com/artsy/minotaur/pull/259


_[2] (Consignments) Associate specific submissions with sessions_ - [Mike Hromchak](github.com/mikehrom)
> Bettina wants to be able to assess the quality of consignment submissions related to marketing channel: 
> - whether a submission is able to be sent in the digest
- whether a submission receives proposals from partners
- whether a submission converts to a consignment
- whether it sells
> `submission_id` is present on the `force_production.consignment_submitted` event, so we can associate specific submissions via that link
> We can also translate session channel info to the consignments explore in Looker (+ add session info to analytics.consignments)
> 
https://github.com/artsy/minotaur/blob/master/queries/auctions/consignment_submission_sessions.sql
https://github.com/artsy/minotaur/blob/master/queries/auctions/untracked_consignments.sql
> 
https://github.com/artsy/fulcrum/pull/702

_Add fields to article tags look_ - [Will Goldstein](github.com/wrgoldstein)
> - add purchasers
- add GMV for purchases
- reader/visitors: how many distinct visitors saw this tag?
- converting readers to users: how many people saw this tag and then created an account within 30 days?
> - provide retention looks to editorial team (retention may make sense as a metric to track for them, since all artsy users are sent editorial after signup)
> - reengagements by vertical (I think this is one area that editorial really can shine)
> - 

_Redshift to Sailthru data pipeline_ - [Will Goldstein](github.com/wrgoldstein)

_CRM: Transition dates for crm tier_ - [Will Goldstein](github.com/wrgoldstein)

_Figure out next steps for radiation message NLP_ - [Will Goldstein](github.com/wrgoldstein)

_[3] Send Asian gallery summary stats to Melody_ - [Mike Hromchak](github.com/mikehrom)
> https://docs.google.com/a/artsymail.com/document/d/13OVq1pN99dx5rY3K5Fq70jWJR8MfZlnwfo9OHyut9Mg/edit?usp=sharing



September 22
-----
_[4] Propose tracking for live auction events_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/auctions/issues/644
> For marketing attribution we need to have prediction events firing in force; the above issue proposes schema for these events

_[4] First pass at inquiry retention and dormant user analysis_ - [Mike Hromchak](github.com/mikehrom)
> 1. Look into poison rate specifically. What is the poison rate -- what % of users who do not receive a (quick) response to their first inquiry do not inquire ever again? 
> 2. What is the average rate of inquiry (distinct days) for users who do get a first response vs. users who do not get a response? 
> 3. For dormant users, what initiates their "return" sessions? (i,e. did a particular marketing channel affect their return to being commercially active?)
> https://github.com/artsy/minotaur/pull/259
- This PR finds average rate of inquiry is actually higher for those who do not receive a response to their first inquiry. Additionally, analysis shows that for long-dormant users, Google search is the marketing channel that most frequently begins their first commercial session after a long period of non-commercial activity.


_[2] Add new measures to auctions explore in Looker_ - [Mike Hromchak](github.com/mikehrom)
> From Melanie in the help channel: 
> "One is the local currency version of "Total Direct Underbid Dollars" and "Total Underbid Dollars" (as seen here https://artsy.looker.com/explore/artsy/sales?qid=GYUoZzkjk2jWPmLtjaxN4A) and the other is a little more complicated - Essentially the count version of this instead of the value (https://artsy.looker.com/explore/artsy/sales?qid=g0MKrbOyRlcESlmo06PNOl)"
> https://github.com/artsy/looker/pull/856

_[1] Fix impulse assessments count in the inquiries explore_ - [Mike Hromchak](github.com/mikehrom)
> ##### Problem:
"Something seems wrong with the "Impulse Assessments Count" Measure. https://artsy.looker.com/explore/artsy/inquiry_requests?qid=1839pemfovW98FBiEBoUrx&toggle=fil
> It seems like no matter the date range, the count of assessments always equals the count of all inquiry requests."
> 
##### Addressed here:
https://github.com/artsy/looker/pull/859

_[1] Add provenance and "about the work" sections to looker (for artworks)_ - [Mike Hromchak](github.com/mikehrom)
> Addressed here: https://github.com/artsy/fulcrum/pull/694
and here: https://github.com/artsy/looker/pull/857

_[4] Summarize what's going on with users who receive auction offers_ - [Mike Hromchak](github.com/mikehrom)
> Performed an initial analysis on bid-through rates for offered sale artworks, the conclusions of which are summarized in the minotaur links below, as well as in an email between Sara, Erin and the analytics team.
> - 58% of all sale artworks receive bids
- 4.4% of all offered sale artworks receive bids
- 1.3% of all offered sale artworks receive winning bids
- 0.2% of all offers sent (across all sales) convert to a bid
> https://github.com/artsy/minotaur/pull/254
https://github.com/artsy/minotaur/pull/255
https://github.com/artsy/minotaur/pull/260
> Further exploration is required and summarized in a new card. 


September 15
-----
_[1] Add ((unrenewed + churned) / starting) MRR measure to PSM_ - [Mike Hromchak](github.com/mikehrom)
> % MRR churn
> https://github.com/artsy/looker/pull/851/

_[3] Conversation assessment tags in looker_ - [Mike Hromchak](github.com/mikehrom)
> @carolineperkins3: Hi Analytics! Since last week's office hours, Ashkan has synced the new Impulse Assessment tags to Redshift (assessments are fully outlined in this github: https://github.com/artsy/impulse/pull/320). Can we surface these assessments in the Inquiry Requests explore in Looker? Not sure of your workflow for such requests, but let me know how I can help or if you need any further context!
> https://docs.google.com/a/artsymail.com/document/d/1gL8S5QBVx4ClmzJpiEF5irU26Ek9VEKx5i70XJlWa48/edit?usp=sharing
> https://github.com/artsy/fulcrum/pull/690
> https://github.com/artsy/looker/pull/852

_[2] Funnel of consignment engagement_ - [Mike Hromchak](github.com/mikehrom)
> http://artsy-filtration.herokuapp.com/funnel/59baeee3086c58000440330d/show
> Goal is to get a handle on how many people are clicking through to the consignments flow


September 8
-----
_Discuss account creation tracking with engineering_ - [Ani Petrov](github.com/anipetrov)

_Add new salesforce fields to the partners table and to looker_ - 54904350f482666493a5010c, [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/668
> Added several salesforce-related fields to the partners table/view 

_Roadmap Draft_ - [Will Goldstein](github.com/wrgoldstein)

_[1] add campaign_content to multitouch_ - [Ani Petrov](github.com/anipetrov)

_Hiring_ - [Will Goldstein](github.com/wrgoldstein)

_Analyze effectiveness of apple ads for iphone app_ - [Ani Petrov](github.com/anipetrov)

_Fix fallout from b2b marketing overhaul_ - [Ani Petrov](github.com/anipetrov)

_Finalize public => gravity migration, fix fallout_ - [Will Goldstein](github.com/wrgoldstein)

_[1] Move credit cards report to Fulcrum_ - [Joel Auerbach](github.com/joelauerbach), [Mike Hromchak](github.com/mikehrom)

_Add new article fields to Looker_ - [Mike Hromchak](github.com/mikehrom)

_[1] Update credit card geo information on the bidder registrations table_ - [Mike Hromchak](github.com/mikehrom)
> Pull city state and country from the credit cards report (fields need to be added to credit card report.rb)
Change bidder registrations table (analytics) to accept credit card location data rather than data from the users table


_Weekly instead of radiation update for events_ - [Ani Petrov](github.com/anipetrov)

_Analyze effectiveness of facebook authentication_ - [Will Goldstein](github.com/wrgoldstein)

_Predict purchases from radiation messages_ - [Will Goldstein](github.com/wrgoldstein)
> https://gist.github.com/wrgoldstein/da5f3756f63963f00442f9a8e4e15729


September 1
-----
_[2] Create GR query to estimate ROI for partners per admin_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/258

_Will + Ani out_ - 

_[epic] b2b last touch and multitouch_ - [Ani Petrov](github.com/anipetrov)
> This work will result in being able to include partner gallery applications and marketo optins in Looker

_[2] determine sessions involving consignments that did not have tracking from June-Aug_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/253

_Performance reviews week_ - 


August 25
-----
_[1] Make sure Candela builds properly_ - [Mike Hromchak](github.com/mikehrom)
> run
```
bundle exec rake transform:candela
```
> and fix the issues it mentions.
> https://github.com/artsy/fulcrum/pull/671

_Move PartnerShows and related reports to Fulcrum_ - [Madeleine Boucher](https://trello.com/madeleineboucher), [Joel Auerbach](github.com/joelauerbach)
> And add `is_reference` flag on PartnerShows.
> This is needed to be able to track which partners and artists have reference shows, beyond the raw stats of which partner submitted admin_metadata tickets. 
> Happy to do the bit of adding it to the Explore view myself after it's in Redshift. Believe it should be in the `public.partner_shows` table.
Thanks!
> https://github.com/artsy/gravity/pull/11179
https://github.com/artsy/looker/pull/816

_More logic adjustments on form submissions and opportunity associations_ - [Ani Petrov](github.com/anipetrov)
> part of epic https://trello.com/c/V4UvF1xF/1093-b2b-last-touch-and-multitouch
> https://github.com/artsy/fulcrum/pull/651


_Update salesforce_patrons table_ - [Ani Petrov](github.com/anipetrov)
> part of epic https://trello.com/c/V4UvF1xF/1093-b2b-last-touch-and-multitouch
> https://github.com/artsy/fulcrum/pull/651

_Pick up impulse conversation ids from purchase notes_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/673


_Create marketing leads, optins and applications report in Looker_ - [Ani Petrov](github.com/anipetrov)
> part of epic https://trello.com/c/V4UvF1xF/1093-b2b-last-touch-and-multitouch
> https://github.com/artsy/fulcrum/pull/651


August 18
-----
_Fixed candela data/analytics emails_ - [Will Goldstein](github.com/wrgoldstein)

_[1] Fix date and dimensions fields in the Looker artworks view_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/looker/pull/837

_[1] Add cms_last_login and latest_show_end_at to Looker_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/661
> 
https://github.com/artsy/looker/pull/835

_[1] New consignments events in force_mapped_tracks and sessions_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/consignments/issues/30
https://github.com/artsy/force/pull/1721/
> https://github.com/artsy/fulcrum/pull/665

_[1] Add crm tier to the follow artists explore_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/looker/pull/836

_Richer account creation data: flush out issues_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)
> issue: https://github.com/artsy/collector-experience/issues/416
new onboarding designs: https://artsy.wake.com/1813
> **Why we need this:**
> _Product:_
- Bad user experience -- we are not preserving context, eg we'd send you to the home page after creating an account to follow an artist
- Product wants to know drop off rates at each question in onboarding in order 
- Product and marketing will eventually want to trigger different onboarding flows for different sign up modals
> _Marketing:_
- Information about user sign up context (sign up after inquiry and skip onboarding, sign up to follow an artist, sign up to read editorial, etc.) is important for content personalization, directly affecting CRM
- Marketing wants to be able to quickly iterate on sign up modal content (CTAs, images, etc) and test modals against each other which means that we need to know which user was created through which modal
- Marketing wants to know who goes through onboarding and how far they get
> _Analytics:_
- We need to accurately fire tracking events whenever anyone an account is created in order to attribute account creation events to marketing campaigns as well as analyze A/B tests correctly
> **Onboarding design comments (to be added to wake):**
- research prices, not auctions
- should you be able to skip out of this question
- if not, should we put learn first


_[4] PSM documentation_ - [Joel Auerbach](github.com/joelauerbach), [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/248
https://github.com/artsy/minotaur/pull/249

_finishing touches on b2b form submission attribution_ - [Ani Petrov](github.com/anipetrov)

_set up marketing with adjust and help start adwords app downloads campaign_ - [Ani Petrov](github.com/anipetrov)
> [link to email thread](https://mail.google.com/mail/u/0/?ui=2&ik=36927be5f3&jsver=CT4mZw8g6YU.en.&view=pt&msg=15df77f28671098f&q=christine&qs=true&search=query&siml=15df77f28671098f)


August 11
-----
_Knowledge share_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach), [Ani Petrov](github.com/anipetrov), [Mike Hromchak](github.com/mikehrom)

_Get geo data from billing info for registered bidders_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/gravity/pull/11187

_Liaise with Owen to understand the opportunities with promoted content._ - [Will Goldstein](github.com/wrgoldstein)

_Discuss how to evaluate liaison performance numerically_ - [Will Goldstein](github.com/wrgoldstein)

_[1] Add last cms login and most recent show timestamp to partners table_ - [Mike Hromchak](github.com/mikehrom)
> Jacqueline (IR) is running metrics on institutional partners and how much they interact with CMS; these fields were notably missing from the `analytics.partners` table and looker
> https://github.com/artsy/fulcrum/pull/661

_[1] consign@artsy broken link needs to be reported/fixed_ - [Mike Hromchak](github.com/mikehrom)
> [ see image ]
> https://github.com/artsy/force/issues/1695

_[1] Log issue for /auction page events that are not firing_ - [Mike Hromchak](github.com/mikehrom)
> Events do not fire for clicking register to bid in context: auctions landing and when clicking 'bid' on context: your active bids
> Reference:
https://github.com/artsy/force/issues/1254
https://github.com/artsy/force/blob/master/desktop/analytics/bidding.js
> 
Logged at:
https://github.com/artsy/auctions/issues/582


_[2] merge convection and rothko data for reporting purposes_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/659
https://github.com/artsy/looker/pull/832
> Next step is to connect sessions, but we either need to connect domain data based on timestamp (i.e. when the consignment was created compared to the timestamps of the current and next session start) 
> OR 
> we need the front-end tracking events implemented for Convection, since right now, sessions use the 'submitted-consignment-form' event, which has not fired in two months

_[8] Create user marketing label field based on sperle's definition_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/652
https://github.com/artsy/fulcrum/pull/653
https://github.com/artsy/fulcrum/pull/654
https://github.com/artsy/collector-experience/issues/458
https://github.com/artsy/fulcrum/pull/658
> final logic PR:
https://github.com/artsy/fulcrum/pull/656
> looker PR:
https://github.com/artsy/looker/pull/830
> Sara's look: 
https://artsy.looker.com/looks/4501

_[1] what events fire on article pages and with what frequency_ - [Mike Hromchak](github.com/mikehrom)

_[1] Fix Sara's marketing funnel dashboard in Looker_ - [Mike Hromchak](github.com/mikehrom)
> Reference: 
https://github.com/artsy/fulcrum/pull/656
https://github.com/artsy/looker/pull/830
> Update dashboards in looker once these PRs are merged
> Sara's new look:
https://artsy.looker.com/looks/4501

_[1] Add winning bid value on lots that received x types of bid_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/655
https://github.com/artsy/looker/pull/826

_Report on No Homepage Banner test_ - [Will Goldstein](github.com/wrgoldstein)

_[4] spec out and build a dashboard for GR to help them go through partner conversations around inquiry-to-sale conversions_ - [Ani Petrov](github.com/anipetrov)
> [link to dashboard](https://artsy.looker.com/dashboards/214?Partner%20Name=BERLIN%20BLUE%20art&filter_config=%7B%22Partner%20Name%22:%5B%7B%22type%22:%22%3D%22,%22values%22:%5B%7B%22constant%22:%22BERLIN%20BLUE%20art%22%7D,%7B%7D%5D,%22id%22:2%7D%5D%7D)

_iOS messaging schema kickoff and walk-through_ - [Ani Petrov](github.com/anipetrov)

_[shitload] MKTO opt-ins table + report_ - [Ani Petrov](github.com/anipetrov)


July 28
-----
_Next stab at churn model_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/243
https://github.com/artsy/splinter/pull/20

_add 'subscription state' to partners view in fairs explore_ - [Mike Hromchak](github.com/mikehrom)

_add new users 'last_sign_in' fields to Looker and remove 'last login force mg'_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/649

_add last login tstamp to gravity.users report_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/641

_Rename latest_subscription_state and add new rollups to analytics.partners_ - [Mike Hromchak](github.com/mikehrom)
> rename to `latest_subscription_end_state`
> possible fields to add: 
- days_on_platform
- multiple_inquirer_count
- inquiry_count
- pre_subscription_inquiry_count
- during_subscription_inquiry_count
- avg_response_time
- purchase_count
- pre_subscription_purchase_count
- during_subscription_purchase_count
- cms_session_count
- artwork_count
- ever_published_artwork_count
- has_price_visible_count
- upload_days
- publish_days
- avg_price_listed
- artwork_impression_count
- pre_subscription_impression_count
- during_subscription_impression_count
- average_fair_tier
- fairs_attended
- pre_subscription_fair_count
- during_subscription_fair_count
- show_count
- pre_subscription_show_count
- during_subscription_show_count
- show_artwork_count
- avg_artist_follow_count

> https://github.com/artsy/fulcrum/pull/636
https://github.com/artsy/looker/pull/817

_More frequently updated payment requests and consignments data_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/640

_Salesforce patrons and companies + updated MKTO forms submissions in fulcrum_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/639
https://github.com/artsy/fulcrum/pull/632



July 21
-----
_GP Looker Session_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach)

_Security patch: Upgrade Node for Looker slack bot_ - [Will Goldstein](github.com/wrgoldstein)
> See https://trello.com/c/6dsBdvRU/152-nodejs-security-update-on-heroku.
> Fixed with https://github.com/anipetrov/looker-slackbot/pull/1/files and redeployed.

_Investigate low numbers of sessions with account creations_ - [Will Goldstein](github.com/wrgoldstein)
> The data type for gravity.users.created_at was inferred as `date` instead of `timestamp`. Redshift happily coerces timestamps to dates, so nothing failed, but the 30 minute requirement for connecting sessions and account creations [here](https://github.com/artsy/fulcrum/blob/master/sql/force_sessions_enriched/force_enriched_account_creations.sql#L31) wasn't being met.
> Fixed with https://github.com/artsy/fulcrum/pull/624

_Auction pipeline documentation_ - [Joel Auerbach](github.com/joelauerbach)

_Auction pipeline refactoring_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/625
https://github.com/artsy/fulcrum/pull/628
https://github.com/artsy/looker/pull/807

_Minor sailthru format fixes in gravity_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/gravity/pull/11162

_Add views to Invoices explore in Looker_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/looker/pull/808
https://github.com/artsy/looker/pull/810

_Remove collector_profiles join to users in Looker because it is redundant_ - [Mike Hromchak](github.com/mikehrom)
> Also edit dashboards downstream to point to the `collector_profile` field, which is now located in the `Users` explore
> https://github.com/artsy/looker/pull/811
https://github.com/artsy/fulcrum/pull/633

_[4] New naming for joined views in Looker_ - [Mike Hromchak](github.com/mikehrom)
> [WIP Google Doc](https://docs.google.com/a/artsymail.com/spreadsheets/d/1KecYu-csQmtCrzvjyvmHyt5Y5KCBC-y32JhpRoWviXU/edit?usp=sharing)
> https://github.com/artsy/looker/pull/806

_[4] more Fairs analysis_ - [Mike Hromchak](github.com/mikehrom)
> https://docs.google.com/spreadsheets/d/1-03FZKhCCdS8T2VVc_14yWmNsQtI76nL94mo82q_5Mo/edit#gid=0
> due before Wed 7/19

_Report on users with high bid exposure in multiple active sales_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/looks/4277 


July 14
-----
_Prep Looker LL_ - [Will Goldstein](github.com/wrgoldstein)

_Report on partners who have at least one artwork with a backend price or default new artwork currency in USD_ - [Will Goldstein](github.com/wrgoldstein)
> We're looking to get the list of partners we should target for stripe setup. Can we pull a list of all partners with the following fields?
> Partner name
Partner type (gallery, institutional seller, auction, etc.)
Subscription state (active, fair, etc)
Default currency for new artworks
Total artworks uploaded
Total published artworks 
Total published, for sale artworks 
Number published, for sale artworks listed in USD
> Query: https://artsy.looker.com/sql/r3q8n4r7bcfzrz


_[4] Create suggested consignments analytics schema_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)
> * export consignment submissions from convection
* buttons, account created with consignment submissions for context
> https://github.com/artsy/consignments/issues/30
> [see Consignments tab](https://docs.google.com/a/artsymail.com/spreadsheets/d/17oqFli15x1SmNBu_-fPZhFifMw2BNSPJe9VdOgs1aKs/edit?usp=sharing)

_[2] Expose user_facts in Looker and check for dependencies_ - [Mike Hromchak](github.com/mikehrom)
> This is fields like `inquiries_7_days` etc.
> https://github.com/artsy/fulcrum/pull/620

_[1] Look into adding eigen usage in last six months to Users table_ - [Mike Hromchak](github.com/mikehrom)
> `app_session_time` is the best way to count sessions / timestamps (use `received_at`)
> https://github.com/artsy/fulcrum/pull/620

_[1] Create Volt tracking doc_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/collector-experience/issues/204
https://github.com/artsy/volt/pull/2579
[Google workbook](https://docs.google.com/a/artsymail.com/spreadsheets/d/16Jv62-WXdd6NFLutWDUBdNMeXn5zvCpeEYW8vJuo0ns/edit?usp=sharing)
> Created a schema doc for tracking in Volt, specific to payment requests which are in the process of being implemented. 

_Board deck + investor Q2 prep_ - [Ani Petrov](github.com/anipetrov)

_[2] Last touch b2b attribution: sketch out salesforce tables and outline next steps_ - [Ani Petrov](github.com/anipetrov)
> 1. de-dupe marketo form submissions:
  * remove all test emails
  * address duplicate form submission entries — might be part of the extract
  * de-duping is not actually necessary
*outstanding items: de-dupe form submissions extract*
> 2. Remove spamers, bots and testers
  * testers: we can create a scratch table, a CTE, or manually exclude testing emails, something like: 
```
WHERE form_submitter_email NOT ilike '%perkuto%'
AND   form_submitter_email NOT ilike '%artsy%'
AND   form_submitter_email NOT ilike '%finsness%'
AND   form_submitter_email NOT ilike '%dupe2%'
AND   form_submitter_email NOT ilike '%test%'
```
  * exclude people that are deleted in marketo; that would include spammers/bots
*outstanding items: export marketo leads for inner joining where marketo lead *
> 3. Make sure there is an easy way to distinguish gallery applications
  * rename forms to match id’s with well-named activity names — Cat finished this
  * historically, on the marketo.form_submissions table we record the old name of the form but the proper id => we can join to forms tables to source new better names
*outstanding items: export form types table*
> 4. Still seeing a lot of qualified applications without utm sources and mediums
  * dig into data
  * if we decide there is enough information in segment for us to recreate that report with greater accuracy, than redo that part of the report
*outstanding items: data inspection, potential new utm sourcing*
> 5. Recreate report on the company (account/contact) level to get opportunities and $$
> In the meantime, we can recreate the numbers Cat reports on through: 
```
SELECT TO_CHAR(activity_date,'yyyy-mm-01'),
       qualified_definition,
       utm_medium,
       utm_source,
       utm_campaign,
       utm_content,
       COUNT(*)
FROM analytics.enriched_marketo_form_submissions
WHERE form_submitter_email NOT ilike '%perkuto%'
AND   form_submitter_email NOT ilike '%artsy%'
AND   form_submitter_email NOT ilike '%finsness%'
AND   form_submitter_email NOT ilike '%dupe2%'
AND   form_submitter_email NOT ilike '%test%'
AND   primary_attribute_value_id IN (1059,1110,1211,1238,1449,1450,1539,1741,1957,1964,2014,2001)
GROUP BY 1,
         2,
         3,
         4,
         5,
         6
ORDER BY 1 DESC LIMIT 300
```

_Support web onboarding redesign_ - [Ani Petrov](github.com/anipetrov)
> iOS onboarding: what worked well, how much more personalized info do we get for users through it than through web?
> + an in-depth ios newest onboarding



July 7
-----
_[4] Partner success analysis blog post in splinter_ - [Mike Hromchak](github.com/mikehrom)

_[2] Don't multiplicably sum inquiries on article tags_ - [Mike Hromchak](github.com/mikehrom)
> In [this line](https://github.com/artsy/looker/blob/master/article_tag_readers.view.lkml#L278) we are summing inquiries, but since this is inquiries per user assigned to each tag per article read, a user who reads several articles (potentially each with multiple tags) will have their inquiries way over counted, so we should remove this.
> https://github.com/artsy/looker/pull/799

_[2] Create user_facts table in fulcrum_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/620
> additional work is required in looker and need to check downstream in fulcrum and minotaur for dependencies

_[4] fairs analysis - are inquiries on fair artworks declining?_ - [Mike Hromchak](github.com/mikehrom)


June 30
-----
_Mongoexport artworks_ - [Will Goldstein](github.com/wrgoldstein)
> Create a document detailing requirements / hopes for the ETL process

_[4] Support Fairs analysis followup_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/235

_[3] Add collector profile fields to users table in fulcrum_ - [Mike Hromchak](github.com/mikehrom)
> Especially artsy confirmed buyer, collector level, and professional buyer status
> https://github.com/artsy/fulcrum/pull/612

_[2] export images from convection_ - [Mike Hromchak](github.com/mikehrom)
> from bettina [1:34 PM]:
>hi again -- for convection.submissions, would someone be able to help me get a field added for image URL (large size)?
> There's an example of this here: https://github.com/artsy/looker/blob/master/artworks.view.lkml#L338
> 
https://github.com/artsy/fulcrum/pull/613
https://github.com/artsy/looker/pull/797

_Make underbidder suggested artworks a dashboard_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/795

_Splinter post on decision tree research_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/splinter/pull/12

_Price currency conversion on artworks_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/impulse/pull/267
https://github.com/artsy/gravity/pull/11129
https://github.com/artsy/fulcrum/pull/604
https://github.com/artsy/looker/pull/793

_Add measures for finance monthly executive report_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/794

_Launch Splinter publicly_ - 

_Add artist slug and follow count to sale_artworks_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/614
https://github.com/artsy/looker/pull/796

_refine auction analysis writeup_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/220

_Inquirer/registrant decision tree classification_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/234

_Finish search AB test analysis and write a blogpost about it_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/splinter/pull/10

_Updates to AB testing framework_ - [Ani Petrov](github.com/anipetrov)

_Collection management writeup_ - [Ani Petrov](github.com/anipetrov)


June 23
-----
_positron verticals and authors in rollups_ - [Will Goldstein](github.com/wrgoldstein)

_First pass at forecasting GMV_ - [Will Goldstein](github.com/wrgoldstein)
> https://github.com/artsy/fulcrum/pull/600
[writeup](https://docs.google.com/document/d/1gPXXhmMy9qKPKoiGIFg3DhwxR3WXs6tda-6mlW3boxo/edit)

_Add a couple new Bearden fields to Explore view_ - [Madeleine Boucher](https://trello.com/madeleineboucher)
> All these fields are in the `bearden_exports.organizations` table, think it should be pretty straightforward to just add them to the Explore view. 
> Also, if you wanna punt this back to me and show me how to do it, more than happy to!
> ## Fields to add
- `organization_type`
- `city`
- `country`
- `sources`

_Expose local bid values_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/600
https://github.com/artsy/looker/pull/784

_Suggested works for underbidders_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/sql/bjct9dggsxws58

_retention_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/607
https://github.com/artsy/looker/pull/791



June 16
-----
_Investigate/restore missing sailthru blast data_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/597

_Fair admin offers_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/sql/jjrg2h9brtwmnv

_[4] initial Fairs analysis_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/229

_[4] highlight_header_search AB test initial analysis + add testing events to unified_sessions_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/pull/230

_[3] set up tracking for Volt_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/volt/issues/2550
> https://github.com/artsy/collector-experience/issues/204
> https://github.com/artsy/volt/pull/2579

_Looker I_ - [Ani Petrov](github.com/anipetrov), [Mike Hromchak](github.com/mikehrom), [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein)

_kick off artist page AB test conversations_ - 
> We'd like to test removing the image slideshow at the top of artist pages in order to get commercial works above the fold. We went through historic artist page tests and we expect that this change will have an effect on bounce rate. We have to add bounce rate to our current rollups and add time on page as a metric in our AB testing framework
> https://github.com/artsy/collector-experience/issues/336#issuecomment-309448266

_kick off onboarding redesign_ - 
> Goal of project: improve information capture through targeted improvements of the existing flow
Analysis of current flow: https://docs.google.com/a/artsymail.com/document/d/1VMlhIm3DyIHtLHJhvFkKACSklLR7_AjDRhWHnPEghjU/edit?usp=sharing

_session 3.0 planning (force awakens)_ - 
> _Problems with current rollups:_  
1. take too long
2. too confusing to add things to
3. artificial division between web and mobile web
> _The new session architecture will allow us to:_  
1. decrease complexity by 
2. be agnostic to the multiple microservices that comprise artsy.net
3. associate more events with the respective sessions they occur in
4. take a first step towards incremental builds
> _Steps:_  
1. Unionize mG and force
2. Sessionize based on site landings: closer to GA session definitions
3. Alias sessions
4. Alias pages
5. Alias important tracks and associate more events with the respective sessions they occur in
6. Add emails to aliasing



June 9
-----
_Fix extract:fx_ - [Joel Auerbach](github.com/joelauerbach)
> See http://joe.artsy.net:9000/job/fulcrum-extract-daily/329/changes
> https://github.com/artsy/fulcrum/pull/586

_Tags_ - [Will Goldstein](github.com/wrgoldstein)

_[4] Document response time analysis_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein)
> https://github.com/artsy/minotaur/pull/228
https://github.com/artsy/splinter/pull/7

_Ship b2b multitouch v1_ - [Ani Petrov](github.com/anipetrov)
> initial work: https://github.com/anipetrov/fulcrum/tree/b2b/sql/b2b_attribution
> outstanding questions:
> 1. do we say site landing == attended webinar and that just becomes another thing we give credit to
2. do we consider first touch in any meaningful way
3. do we split pre opp creation and post opp creation activity
4. if not, do we give equal credit to everything pre close for the opp and how long for
> those and some reporting ideas are listed here: https://docs.google.com/document/d/1gtvxsblcNoY5Ma-oPP_Qmh0YlFQ482ABdkJsFFMW1Zc/edit

_QA eigen analytics v1_ - [Ani Petrov](github.com/anipetrov)
> Review the most recent release, follow up with Katarina and Maxim on QA items, leftover, and next steps:
https://github.com/artsy/collector-experience/issues/327#issuecomment-306902577

_add follow count to the gene report_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/gravity/pull/11099

_Deploy splinter_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)
> Deploy splinter; require auth; allow for multiple authors

_QA search and experiment events for search AB test_ - [Ani Petrov](github.com/anipetrov)
> test setup: https://github.com/artsy/collector-experience/issues/251#issuecomment-306533720
> test will be peeked into next week for search volume result and we will likely leave it running if those are positive to look for inquiry lift while we are thinking through the second iteration of the test


June 2
-----
_[3] check out undefined mediums_ - [Mike Hromchak](github.com/mikehrom), [Joel Auerbach](github.com/joelauerbach)
> Try to understand what these should be.
> Look in Force or Microg pageview history, look at mediums that are currently "undefined" in sessions, look at what the actual referring source / url is, see if there are patterns.
> https://github.com/artsy/fulcrum/pull/575

_[2] fix users table structure to stop truncation_ - [Mike Hromchak](github.com/mikehrom)

_Retire Mixpanel_ - [Will Goldstein](github.com/wrgoldstein)
> https://github.com/artsy/minotaur/issues/105

_[3] Populate owner_id for inquiry purchases that have radiation url in notes_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)
> eg for purchase `586c476d9c18db595c000239`, note says:

Radiation: https://radiation.artsy.net/admin/conversations/190647/messages
> An inquirer from AUS inquired on 3 prints by the artist and quickly moved forward with purchasing 2 (the 3rd being no longer available).
> primary


_Splinter in git!_ - [Ani Petrov](github.com/anipetrov)
> create a repo + readme + first blogpost for the artsy analytics blog: https://github.com/artsy/splinter


_b2b multitouch: email aliasing_ - [Ani Petrov](github.com/anipetrov)
> Artsy visitors are only identified via email in marketo and salesforce. Marketo gathers some other information upon form submission -- ip and user agent. This card is about figuring out possibilities and limitations of using that + our identify event to connect web and sf/mkto activity



May 26
-----
_Backup Mixpanel data_ - [Will Goldstein](github.com/wrgoldstein)

_Ensure no projects send data to Mixpanel directly_ - [Will Goldstein](github.com/wrgoldstein)

_carefully merge https://github.com/artsy/gravity/pull/11063_ - [Will Goldstein](github.com/wrgoldstein)

_Design churn for SC_ - [Will Goldstein](github.com/wrgoldstein)

_[3] Merge PSM historic with main PSM_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/772

_Finish sailthru user import_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/gravity/pull/11069
https://github.com/artsy/gravity/pull/11075

_[4] What does a "successful gallery" look like?_ - [Mike Hromchak](github.com/mikehrom)
> - What is average behavior for a gallery in terms of number of sessions in CMS, frequency of CMS usage, responsiveness to inquiries, or number of inquiries received?   How does this change by tier?  By geography?
> 

- Which galleries are receiving the most inquiries? What makes them different from other galleries?
> - Which galleries have the most _repeat inquirers_ (or highest percentage of repeat inquirers). Are these different from above? What characterizes these galleries? (Be wary of same-day inquiries to the gallery, which isn't the same as repeat behavior)
> https://github.com/artsy/minotaur/blob/master/sandbox/mike/partner_success_analysis.md


_Glossary v1.0_ - [Mike Hromchak](github.com/mikehrom)
> https://docs.google.com/a/artsymail.com/spreadsheets/d/1pj1F10hbBGnuSbUKU-qOF7AsXKJRbsrrrksqAPEBn3I/edit?usp=sharing


May 19
-----
_[2] Confirm `historical_partner_subscriptions` and `partner_subscription_metrics` give the same results_ - [Mike Hromchak](github.com/mikehrom)
> They appear to return the same results - example:
> `partner_subscriptions_historic`
https://artsy.looker.com/x/qs3n9qB
https://artsy.looker.com/x/bzRxtg2
> `partner_subscriptions_metrics`
https://artsy.looker.com/x/QpcWQKn
https://artsy.looker.com/x/qxDQj6W


_Add promoted content charges to redshift_ - [Will Goldstein](github.com/wrgoldstein)
> [look](https://artsy.looker.com/explore/artsy/subscription_charges?qid=tXcKfF0DHpwGmZsEk7lKoe)
[PR](https://github.com/artsy/looker/pull/767)

_Recover Alonzo dash_ - [Will Goldstein](github.com/wrgoldstein)

_Check on artsy.cn tracking_ - [Will Goldstein](github.com/wrgoldstein)
> it seems a splash page was launched without tracking of any kind, so there's no traffic to look up.  It looks to me like google analytics should work in china (https://chineseseoshifu.com/blog/is-google-analytics-blocked-in-china.html) so @craig or @christina might be good point people to get that implemented, but you'd have to wait a while after they do that work to see any results

_Send potential GMV "Templates" to Sebastian_ - [Will Goldstein](github.com/wrgoldstein)

_Answer Ilana's "Questions for Analytics"_ - [Will Goldstein](github.com/wrgoldstein)

_Redo QFU analysis_ - [Will Goldstein](github.com/wrgoldstein)
> It turns out the CE team actually reaches out to the galleries in question to confirm the user reported sales
> [2:45] 
And that hasn't been done since the last analysis
> [2:45] 
so we don't know what % of recent user reported sales are real at this point
> william [3:03 PM] 
Ok so since that last study ended there were 24 new self reported purchases and only *1* was already recorded.  Last time galleries confirmed user reports 8 out of 11 times, so we can estimate the denominator as 8/11 * 24 =~ 17
> [3:07] 
And the total number of survey responses was 59,291

_[1] Find a good avatar that is not your actual suit-face_ - [Mike Hromchak](github.com/mikehrom)

_[4 -> 3] Bidding behavior analysis_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/220


May 12
-----
_[epic] Track down and consolidate a record of A/B testing at Artsy_ - [Mike Hromchak](github.com/mikehrom)

_[4] Start documenting AB testing_ - [Mike Hromchak](github.com/mikehrom)
> - what tests are being planned
- what the goal of each is
- links back to any relevant issues or documents
- what has been done or is in progress
- what outcome a test had, if any
> 
https://docs.google.com/a/artsymail.com/spreadsheets/d/1TA2ZcEuxq4fRFRDM8ofOw2qwGPladrQ0SKFnStOmpRQ/edit?usp=sharing

_Send email about GR changes_ - [Joel Auerbach](github.com/joelauerbach)
> https://groups.google.com/a/artsymail.com/forum/?hl=en#!topic/analytics/Az9btbc5NCU

_Prepare Sailthru user data import_ - [Joel Auerbach](github.com/joelauerbach)

_[3] Set up search AB test and make sure we have all needed search events_ - [Ani Petrov](github.com/anipetrov), [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/collector-experience/issues/251
```
> 
SELECT AVG(uniques)
FROM (SELECT sent_at::DATE,
             COUNT(DISTINCT looker_visitor_id) AS uniques
      FROM analytics.unified_pages
      WHERE sent_at > '2017-04-01'
      and app_id = 'force'
      GROUP BY 1)
--77236
> SELECT AVG(unique_nonreaders)
FROM (SELECT sent_at::DATE,
             COUNT(DISTINCT looker_visitor_id) AS unique_nonreaders
      FROM analytics.unified_pages
      WHERE sent_at > '2017-04-01'
      and pagetype <> 'article'
      and app_id = 'force'
      GROUP BY 1)
--47674
> SELECT AVG(inquirers)
FROM (SELECT sent_at::DATE,
             COUNT(DISTINCT anonymous_id) AS inquirers
      FROM force_production.sent_artwork_inquiry
      WHERE sent_at > '2017-04-01'
      AND   context_page_path NOT LIKE '%/inquiry/%'
      GROUP BY 1)
      --154
> SELECT AVG(searchers)
FROM (SELECT sent_at::DATE,
             COUNT(DISTINCT anonymous_id) AS searchers
      FROM force_production.focused_on_search_input
      WHERE sent_at > '2017-04-01'
      AND   context_page_path NOT LIKE '%/inquiry/%'
      GROUP BY 1)
--2294
> 
SELECT COUNT(DISTINCT looker_visitor_id) AS unique_nonreaders
FROM analytics.unified_pages
WHERE sent_at > '2017-04-15'
AND   pagetype <> 'article'
AND   app_id = 'force'
--955505
```
> Estimated runtime of test: 15-20 days to see effect on inquiry CVR; 2-3 days to see effect on search CVR. Design wants to iterate on this quickly and test for search volume mainly. We also proposed an change in some of the current event schema in the above issue.


_Loyalty QA_ - [Ani Petrov](github.com/anipetrov)
> Loyalty page was hosted in a different repo (https://github.com/artsy/reaction-force). After re-introducing all automated events in force (pageviews, identify, time on page), we now see everything firing as expected. 

_[2] Investigate account creation instrumentation_ - [Ani Petrov](github.com/anipetrov)
> 1. We are seeing `sign_up_user_agent`s overwritten by node :https://github.com/artsy/force/issues/1390. after some investigation, we found out that the overwriting is happening for facebook signups. Craig PR-ed a fix and we are now monitoring

_[6] Multitouch next steps https://trello.com/c/I52LjVs1/1056-multitouch_ - [Ani Petrov](github.com/anipetrov)


May 5
-----
_[2] Political art on artsy_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)
> Inquiries and pageviews over time for artworks that have artists with a political gene: request from anna for a story
> Findings:
We investigated whether or not there was a spike in commercial/non-commercial behavior on the website around elections focused on artworks by artists with a 'political' gene but found no significant pattern
> https://github.com/artsy/minotaur/blob/master/queries/analysis/political_art.sql
> This is the query we used to search gravity for artists with a political gene:

```
require 'csv'
> ids = Artist.where("genome.genes.Political" => {"$exists" => true }).pluck(:_id)
> ids.each do |id|
    artist = Artist.find(id)
  puts [
    artist._id,
    artist.slug,
    artist.name,
    artist.genome.genes["Political"].to_i
    ].to_csv
  end; nil
```


_[1] Venice instrumentation_ - [Will Goldstein](github.com/wrgoldstein), [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/force/issues/1305


_[1] add consignments to users_ - [Joel Auerbach](github.com/joelauerbach)

_[1] investigate missing sale_artworks in gravity report_ - [Joel Auerbach](github.com/joelauerbach)
> Resolution: this was caused by Fulcrum's schema inference from random sampling of data types, which caused errors on rows containing strings in a column inferred to be integers. Since it only allows up to 10 errors before failing the build completely, this is probably safe for now until we figure out a longer term plan for warehousing.

_[2] Remove deleted lots from bidding and build in better protections re currency conversion dates_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/556
https://github.com/artsy/looker/pull/757

_[3] Sailthru artworks import_ - [Joel Auerbach](github.com/joelauerbach)

_[1] Investigate failing extract-daily_ - 

_[1] Segment-Marketo integration_ - [Ani Petrov](github.com/anipetrov)
> After some discussion and testing we decided to turnoff the marketo integration in segment: 
- it was using up our quota of API calls, not allowing us to extract data from the API
- we were getting user browsing behavior information from the implemented marketo munchkin already
- we get marketo-segment alignment through identify calls that fire on every marketo form event


_[6] Editorial continues_ - [Ani Petrov](github.com/anipetrov)
> Link to analysis in the analytics group https://groups.google.com/a/artsymail.com/forum/?utm_medium=email&utm_source=footer#!msg/analytics/pV4-gAXPXF8/xu0SmfloAQAJ
> 
iPython Notebook:  https://github.com/artsy/minotaur/blob/master/analysis/editorial/2017-04-24-Editorial_commercial_activity.ipynb

_[3] add partner to-do's to partners explore_ - [Mike Hromchak](github.com/mikehrom), [Will Goldstein](github.com/wrgoldstein)
> https://artsy.looker.com/explore/sql__nh2vdrrvvmrgjz/sql_runner_query?qid=T2EpD9eIaO2zMqMCQTehLf
> also percentages like https://artsy.looker.com/explore/artsy/partners?qid=uFKdHrNqe15QhiDNBYXkpr
> also add medium to-do
> https://github.com/artsy/looker/pull/759

_Present about iOS onboarding + next steps in eigen development_ - [Ani Petrov](github.com/anipetrov)
> Eigen shipped a new onboarding flow in april, asking users to sign up immediately after launching the app and then go through personalization (as opposed to the other way around). High level takeaways: higher conversion rate download -> account (63% as opposed to 39% before) and 90% of eigen users go through personalization and follow at least one artist or category
> Deck: 

_Eigen Instrumentation, part of https://trello.com/c/hwBsIigZ/624-eigen-analytics-overhaul_ - [Ani Petrov](github.com/anipetrov)
> Deep linking is almost ready for shipping. It will be brought to beta with analytics hooked up for testing next week.
> Progress on the rest: we will not hook up any type of analytics to non-native views. 

_[1] Investigate failing transform-daily_ - 

_[2] Loyalty schema_ - [Ani Petrov](github.com/anipetrov)
> After QA-ing the proposed instrumentation schema, we noticed that loyalty is not hooked up to our regular automated events (pageviews, time on page, identify), as it was not in the force repo but rather in reaction-force. We requested further instrumentation.
> https://github.com/artsy/collector-experience/issues/228#issuecomment-299186872
https://github.com/artsy/collector-experience/issues/257

_[2] Look into `historical_partner_subscriptions` and `partner_subscription_metrics` discrepancies_ - [Mike Hromchak](github.com/mikehrom), [Joel Auerbach](github.com/joelauerbach)
> First part of investigation showed different counts of rows in the two tables. Looking deeper next week



April 28
-----
_Filtration funnel properties_ - [Will Goldstein](github.com/wrgoldstein)

_how many inquiries happen on an artwork before it is sold? what about on the artist level?_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/minotaur/pull/212
> ## Inquiries on artworks pre/post-sale
```
|       | total_inquiries | inquiries_before_sale | inquiries_after_sale |
|-------|-----------------|-----------------------|----------------------|
| count | 5463            | 5463                  | 5463                 |
| mean  | 5.339374        | 3.558667              | 1.780524             |
| std   | 31.408976       | 14.127402             | 21.136112            |
| min   | 1               | 0                     | 0                    |
| max   | 1864            | 594                   | 1460                 |
```
> ## Inquiries on the artist level, pre/post-first sale
```
|       | total_inquiries | inquiries_pre_first_sale | inquiries_post_first_sale |
|-------|-----------------|--------------------------|---------------------------|
| count | 2872            | 2872                     | 2872                      |
| mean  | 73.261490       | 24.883008                | 48.378482                 |
| std   | 255.321118      | 59.412474                | 223.273517                |
| min   | 1               | 0                        | 0                         |
| max   | 6080            | 1309                     | 5952                      |
```

_Analytics 2017 roadmap_ - [Will Goldstein](github.com/wrgoldstein)

_eigen instrumentation: https://trello.com/c/hwBsIigZ/624-eigen-analytics-overhaul_ - [Ani Petrov](github.com/anipetrov)
> Came up with instrumentation strategy and outlined screen views for every eigen screen; went over some of the expected changes to make future-proof.
> Started outlining important event lists.
> Plan for deep link tracking.

_collector experience product work_ - [Ani Petrov](github.com/anipetrov)
> * definitional/kick-off meetings for a new user (and non-user) management tool + new ui to replace torque. Will likely involve some modeling of offline events and possibly purchases?
> * ideas for continuous testing: a series for small(scope) ab tests for q2


_[6] Marketing funnels v2_ - [Joel Auerbach](github.com/joelauerbach)

_[2] Send email about editorial crossover_ - [Ani Petrov](github.com/anipetrov)

_[2] PSM followups_ - [Joel Auerbach](github.com/joelauerbach), [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/554
https://github.com/artsy/looker/pull/752



April 21
-----
_[4] Editorial crossover analysis_ - [Ani Petrov](github.com/anipetrov)
> How much do transactional people read, how many, what vs non-transactional articles?
> > People read a little bit, mostly art market and emerging artist content.  Also, many of these people inquire before reading but we don't know the impact of reading on retention / future commercial activity.  Purchasers who do read mainly arrive on article pages from emails.

_Fix radiation messages_ - 
> blacklist? truncate messages? incremental extracts?

_Value of auction articles_ - [Will Goldstein](github.com/wrgoldstein)
> eg https://www.artsy.net/article/artsy-auctions-works-to-buy-this-week-at-phillips-head-of-sale-simon-tovey-on-highlights-and-market-market
> how important is content for selling work? Currently, we popularize those mostly through email but users can only find them on the on the /auction/ page (currently at the bottom of the sale page).
> Notebook: https://github.com/artsy/minotaur/blob/master/analysis/auctions/auction_editorial.ipynb

_Set up airbnb knowledge repo_ - [Will Goldstein](github.com/wrgoldstein)
> Isac did this, it's up at https://knowledge.artsy.net/feed.  There are some remaining challenges.. we had to fork it to make auth work, and apparently https redirects don't work, and we need isac to kick off any deploys.  Let's see what happens.

_Bearden in looker_ - [Ani Petrov](github.com/anipetrov), [Mike Hromchak](github.com/mikehrom)
> Fixed the permissions issue - granted access to read_only users. [github thread](https://github.com/artsy/collector-experience/issues/202#issuecomment-294490710)

_Art Fair Relations Fair Summary Dashboard_ - [Mike Hromchak](github.com/mikehrom)
> moved requested explores between dashboards and added `fair_slug` filter to Fairs Summary dashboard [PR](https://github.com/artsy/looker/pull/739)

_`is_admin` is scattered across looker: fix_ - [Mike Hromchak](github.com/mikehrom)
> reintroduced `is_admin` to the users table [PR](https://github.com/artsy/fulcrum/pull/545)

_Add Inquiry to purchase CVR to looker inquiries aggregate metrics_ - [Mike Hromchak](github.com/mikehrom)
> [PR](https://github.com/artsy/looker/pull/740)

_[4] Historic partner subscription adminship_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/204

_[4] Resolve bidding currency issue_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/547
https://github.com/artsy/looker/pull/742
https://github.com/artsy/minotaur/pull/207

_Gather data on UK audience for Editorial/Content_ - [Mike Hromchak](github.com/mikehrom)
> ## Traffic in the last year 
- 10% of overall traffic is from the UK
- Approximately 1.5 million unique visitors
- Over 3 million sessions
- 45% of UK traffic is from London
> ## Registered Users from UK
_country data available for 38% of registered users_
> - 21,713 total registered users in UK
- 11,536 of these come from London
- 3,761 users inquired
- 176 users with inquiry purchases
- 103 users with bids
- 37 users with auction purchases
> ## E-mail engagement in the UK
- UK users make up 6% of whole editorial list
- Of users who have clicked at least one e-mail/visited at least one article in the last 30 days, UK users make up 11%
- The UK user group is highly engaged -- 85% of UK users who receive the daily editorial email have clicked at least one e-mail/visited one article in the last 30 days


_[2] Why does facebook instant article traffic show up as undefined at times?_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)

```sql
SELECT first_referrer,
       first_referrer_source, first_referrer_medium,
       app_id,
       landing_page_type,
       COUNT(*)
FROM analytics.unified_session_facts
WHERE DATE_TRUNC('month',session_start_at) = '2017-03-01'
GROUP BY 1,
         2,
         3,4,5
ORDER BY "count" DESC
LIMIT 100
```
> referrer task is not running on microgravity; is only sourcing possible referrers from force_production.pages

_Impact of show browsing on buying habits_ - [Ani Petrov](github.com/anipetrov)
> Shows are an important way that people buy but not through the /shows explore but rather through artist pages and so on, so we're going to remove the /shows section from the browse screen on Eigen.

_[3] Partner added artist metadata --> Redshift & Looker_ - [Mike Hromchak](github.com/mikehrom)
> Since the introduction of the feature, there's no data in Redshift or added to Looker to see how many partners are using metadata features in CMS. This includes:
> - Partners adding artist biographical metadata, incl `nationality` `location` `hometown` `birthyear` `deathyear` `gender`
- Partners adding reference_shows for artists
- Whether an artist has a partner bio is already in Looker, but whether that bio has been featured to the artist's Artsy page in https://admin-metadata.artsy.net is not
> 
## Why we need this
> Any future work on artist metadata features is dependent on how high adoption rates have been so far, which is not something we have any visibility into. 
> In the past, I've asked for help from an engineer to pull one-off numbers, but it's a big ask in terms of their time, and results in a ~24 hr time delay when we need those numbers to make a decision.
> 
[PR](https://github.com/artsy/looker/pull/740)

_[3] Identify which artworks got autopublished in looker_ - [Mike Hromchak](github.com/mikehrom), [Will Goldstein](github.com/wrgoldstein)
> Now that we are allowing artworks that meet the minimum metadata requirements to be published without GR approval, we need a way to identify these autopublished works to 1. know the volume of time saved and 2. make sure there's not poor accuracy data being submitted. 
> Currently in Looker there's not a way to identify these, but Oksana reports that "publish_change_requested_by" and  "publish_change_requested_at" are only set if the artwork requires review. 
> Works can get published and unpublished repeatedly but we don't have an immediate need to really rigorously track change over time.
> Github issue: https://github.com/artsy/collector-experience/issues/116
> Step 1: https://github.com/artsy/gravity/pull/10953 
- add to Gravity report
> Step 2: https://github.com/artsy/looker/pull/744
- add to Looker

_Marketing: analytics, last touch, multitouch with Ilana_ - [Ani Petrov](github.com/anipetrov)
> We had three meetings with marketing that went over a lot. We outlined next steps on multi touch and there was an official Marketing Ask that came out of it that we will prioritize this week.
> Also, there's some interest in "multitouch" for _internal_ features.. i.e. what makes people inquire (the golden question).


April 14
-----
_[3] artists that sell: what is their avg follow count_ - [Mike Hromchak](github.com/mikehrom), [Ani Petrov](github.com/anipetrov)
> median artist follows for purchased artists is 74
avg artist follows for purchased artists is 484
> would be interesting to look into this based on "manner of discovery" of the purchased artwork
> https://github.com/artsy/minotaur/blob/master/queries/analysis/purchased_artist_follows.sql

_[1] Unified pages is dead, fix_ - [Will Goldstein](github.com/wrgoldstein), [Mike Hromchak](github.com/mikehrom)
> `is_admin` field was removed in favor of `roles` which broke our page rollups and this pr fixes that in fulcrum
> https://github.com/artsy/fulcrum/pull/533

_[3] Consolidate e.g. Facebook and facebook sources in sessions_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/fulcrum/pull/536

_[3] Add count of attachments on conversations_ - [Ani Petrov](github.com/anipetrov), [Mike Hromchak](github.com/mikehrom)
> Radiation credentials were outdated, pushed the new ones up to S3. Extracting messages seems to be taking a long time -- let's keep an eye out on how long this takes next time it runs. Might be a good idea to not extract it regularly. [PR](https://github.com/artsy/fulcrum/pull/541)
> Additionally, exposed fields from `radiation_attachments` to the `inquiry_requests` table so it is possible to count the number of attachments in a given conversation. [PR](https://github.com/artsy/fulcrum/pull/542)
> Added new attachments measure and dimension in Looker [PR](https://github.com/artsy/looker/pull/736)


_Artwork data upload to the sailthru content library (final version)_ - [Joel Auerbach](github.com/joelauerbach)
> https://www.dropbox.com/s/ozmatihd02aerqm/sailthru_artworks.json?dl=0

_[4] Marketing funnel investor ask_ - [Joel Auerbach](github.com/joelauerbach)
> https://groups.google.com/a/artsymail.com/forum/?hl=en#!topic/analytics/AFJJNhyQWSo

_Progress on eigen analytics https://trello.com/c/hwBsIigZ/624-eigen-analytics-overhaul_ - [Ani Petrov](github.com/anipetrov)

_Look into different sections of eigen's influence over inquiry behavior_ - [Ani Petrov](github.com/anipetrov)

_Onboarding Mike week 2_ - 


April 7
-----
_Onboarding Mike week 1_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach), [Ani Petrov](github.com/anipetrov)

_[1] Consignment campaign test results_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/sql/n9zkwmttshj3bz

_Filtration work_ - [Will Goldstein](github.com/wrgoldstein)
> - All new UI
- Add Eigen pageviews/screens

_[4] document what is happening with email sessions discrepancies btw in-house and GA_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)
> https://sites.google.com/a/artsymail.com/intranet/team-pages/analytics/best-practices

_Renew segment contract_ - [Will Goldstein](github.com/wrgoldstein)

_Add partner genomes to Looker._ - [Madeleine Boucher](https://trello.com/madeleineboucher), [Joel Auerbach](github.com/joelauerbach)
> We currently can't quite query these things in gravity, and would appreciate adding to Looker:
> 1. Whether a work has genes in its `partner_genome` (yes/no)
2. When that `partner_genome` was last updated (timestamp)
3. Number of genes in `partner_genome` (`gene_count`)
4. A measure for the count of partner genomes.

_Surface bearden tables in looker_ - [Mike Hromchak](github.com/mikehrom)
> issue: https://github.com/artsy/collector-experience/issues/202
pr: https://github.com/artsy/looker/pull/727

_Add image_count to Looker_ - [Mike Hromchak](github.com/mikehrom)
> https://github.com/artsy/looker/pull/729

_[2] b2b strategy alignment and documentation for marketing_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/blob/master/doc/reference/b2b_multitouch_attribution.md

_[1] Purchase request: how many people send a standard inquiry when purchase request is an option_ - [Ani Petrov](github.com/anipetrov)

_Product asks_ - [Ani Petrov](github.com/anipetrov)


April 1
-----
_Haha fooled you!_ - 
> A joke! _A joke_


March 31
-----
_Analytics Onboading_ - [Ani Petrov](github.com/anipetrov)
> https://gist.github.com/anipetrov/9c3efdf4f13322fe5eb8c740c73f5cfd

_[4] Clean up auction naming (date and currency) conventions_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/716
https://github.com/artsy/looker/pull/720

_[2] Promoting content through Sailthru: evaluate success per gallery_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/blob/master/queries/email/partner_pvs_from_email.sql

_investor asks_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach)

_[2] Loyalty program instrumentation_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/collector-experience/issues/86#issuecomment-280413761
https://docs.google.com/spreadsheets/d/1hVlMfjEII8VrjZ2DyKenNiOEn3B5sVimgkrS2nC58Nk/edit#gid=0

_[6] Prekuto contract renegotiation, multi-touch attribution strategy validation, documentation_ - [Ani Petrov](github.com/anipetrov)

_Analytics <> Product strategy_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)


March 24
-----
_segment track deletion is too hard on redshift. consider unstaging old data. consider only rebuilding last few months of sessions._ - [Will Goldstein](github.com/wrgoldstein)
> Changed the segment sync schedule to not overlap with overnight transforms.

_Intro Ilana to Looker and Artsy data_ - [Will Goldstein](github.com/wrgoldstein)

_[4] churn analysis v2_ - [Joel Auerbach](github.com/joelauerbach)
> What causes galleries to churn? What characteristics are indicative of galleries more likely to churn?
> Geographic region
Payment frequency
Plan
Whether gallery upgraded or downgraded
Total uploads
CMS log-ins (total? yes/no per month? )
Inquiries
outreach admin
fair participation rate
# of fairs participated in
folio usage (y/n; times per month)
> This work item is really to plug the above into the survival regression we already have in minotaur.. hopefully in the future we can spend time improving it.

_[4] QA/scope work on prediction instrumentation_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/spreadsheets/d/17Efke6l6bzXdCgbp5zh1XmVNoZAALZR2eDZlE7pxWK8/edit#gid=0

_Dynamic properties in Prediction are causing Redshift errors_ - [Joel Auerbach](github.com/joelauerbach)


March 17
-----
_Rework waterfall churn for Tim_ - [Will Goldstein](github.com/wrgoldstein)

_Submission events in unfiied session facts_ - [Will Goldstein](github.com/wrgoldstein)

_Liaison scoring / relationship between churn and MRR_ - [Will Goldstein](github.com/wrgoldstein)

_OH Followups: What partners are getting suggestions in CMS_ - [Will Goldstein](github.com/wrgoldstein)
> - add artwork categories
- add artist bios
> https://artsy.looker.com/sql/r4br9rp37fjfq7

_[4] Add drop off rates to funnels in Filtration_ - [Will Goldstein](github.com/wrgoldstein)

_Spec instrumentation for new collect page_ - [Will Goldstein](github.com/wrgoldstein)

_[6] Export artworks for Sailthru_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/collector-experience/issues/11#issuecomment-284805119

_[2] Assess PSM variance_ - [Joel Auerbach](github.com/joelauerbach)

_[0] add partner_genome.updated_at to looker_ - [Joel Auerbach](github.com/joelauerbach)


March 10
-----
_[1] Check performance on popular artists on /collect_ - [Ani Petrov](github.com/anipetrov)
> [this](https://artsy.looker.com/sql/xyfs37hfjbkqv4) is a quick funnel query for the last 100 days; looks like over that time period we have had 1826 distinct people click on the feature, 19 of them submitted an inquiry within 30 minutes of interacting with the feature, and none of these inquiries turned into a "known" purchase.

_[6] New LookML!!!_ - [Joel Auerbach](github.com/joelauerbach)

_[4] High-level thinking about messaging/inquiry retention_ - [Joel Auerbach](github.com/joelauerbach)


March 3
-----
_[2] Perform PartnerRepresentation migration_ - [Will Goldstein](github.com/wrgoldstein)

_[4] Gallery Segmentation_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/document/d/17T7TrWS3a3dDGSJW4w12xdmvoxr-NUAbp_ysxLpGxWI/edit?ts=5796133c
> Are current tier 4s the same as tier 4s a year ago? talk to GP

_[4] joel <> taya optimal time to respond to an inquiry for partners_ - [Joel Auerbach](github.com/joelauerbach)

_[1] add partner subscriptions to fairs explore so we can tell the status of their last subscription (did they church, non-renew, are they active currently, etc.)_ - [Joel Auerbach](github.com/joelauerbach)

_[6] Clean up PSM_ - [Joel Auerbach](github.com/joelauerbach)

_[2] better naming in unified pages + pagetype of internal referrer_ - [Ani Petrov](github.com/anipetrov)

_Performance reviews_ - [Ani Petrov](github.com/anipetrov)

_[1] Add number of messages in impulse thread to inquiry requests explore_ - [Ani Petrov](github.com/anipetrov)
> Don't include "bulk messages"

_Initial exploratory processing of burden data_ - [Ani Petrov](github.com/anipetrov)


February 24
-----
_[1] Jennifer Pratt Asia stats_ - [Will Goldstein](github.com/wrgoldstein)

_[4] Finish modeling Representations in Gravity_ - [Will Goldstein](github.com/wrgoldstein)

_[4] gallery partnership application funnel_ - Jesse Kedy, [Ani Petrov](github.com/anipetrov)
> Here are the details but lmk if it needs clarification. This is only for galleries.
> **1st question**: How is this funnel performing (per step & overall)?
> 1. visited /gallery-partnerships* (url contains `artsy.net/gallery-partnerships`)
2. completed step-1 form
3. completed step-2 form
4. completed step-3 form (submitted gallery application)
> **2nd question**: Same as above for mobile vs web.
> **Answers**:
> force in the last 100 days, 30 mins to complete: https://artsy.looker.com/sql/msmtrnxfz4tth9
> force in the last 100 days, 7 days to complete: https://artsy.looker.com/sql/8bfdntpc3wq7qx
> mG in the last 100 days, 30 mins to complete: https://artsy.looker.com/sql/wkrwfvvpvwwchz
> mG in the last 100 days, 7 days to complete: 
https://artsy.looker.com/sql/73vxby9bp48srs
> 
Additionally:
> bounce rate on mobile is 45% from marketing campaigns yet we mostly drive people there 

_[1] User attribution should be by session of account creation, or both_ - [Joel Auerbach](github.com/joelauerbach)
> In the analytics.users table

_GMV product work_ - [Ani Petrov](github.com/anipetrov)
> * Check in if all analytics are firing well after the force/microgravity merge


_[2-4] automate companywide kpis weekly email numberz_ - 55df730aa2e88a6cb1cb3423, [Ani Petrov](github.com/anipetrov)

_[1] Swap out outdated automated career_stage for real career_stage for artists_ - [Madeleine Boucher](https://trello.com/madeleineboucher), [Joel Auerbach](github.com/joelauerbach)
> ## Use case
In Redshift, we understand that there's a source for information about artists that Auctions—and going forward, Bearden—can use to determine the market desirability of artists based on certain data points.
> ### Currently
At least in Looker, what's called `career_stage` for artists is not actually the career stage that genomers lovingly select for every artist; it's a very, very outdated automated model that I don't think anyone uses or really can use. 
> **My ask:** Can we replace whatever is the source of the field (`career_stage`) with the value of the artist's "Career Stage Gene" from the artist's genome (`artist.genome.Career Stage Gene`) ?
> https://github.com/artsy/gravity/pull/10835

_[4] Prep GRCD migration_ - [Will Goldstein](github.com/wrgoldstein)

_[∞] Ugh Katarina_ - [Ani Petrov](github.com/anipetrov)

_[2] Plan for future of marketing attribution on the B2B side_ - [Will Goldstein](github.com/wrgoldstein), [Ani Petrov](github.com/anipetrov)

_Performance reviews_ - [Joel Auerbach](github.com/joelauerbach)


February 17
-----
_[1] cleanup of force schema_ - [Will Goldstein](github.com/wrgoldstein)

_[2] check what fraction is known bot activity_ - [Joel Auerbach](github.com/joelauerbach)
> look at user agents

_[6] Deep dive on how gallery inquiry response time affects conversion rates_ - [Joel Auerbach](github.com/joelauerbach)
> We have the internal belief that the faster the time to first gallery response, the more likely the inquiry is to turn into a sale. Before we prioritize product features and GR outreach to improve response time, we'd like to validate this belief when controlled for potentially related factors like inventory quality, price point, volume of inquiries, etc.
> Some questions:
> - Does time to first response differ depending on characteristic of gallery? (location, artwork average price, artist lifestage represented, gallery tier, subscription tier, etc.) 
- Do galleries have consistent response behavior for all their inventory? E.g. do galleries respond equally quickly to all their inquiries, or do some types of merchandise, like exact price works under $10k, drive faster response times?
- How does time of day/day of week/seasonality affect response time? E.g. weekends are slow, fair season is slow...
- Do galleries respond more quickly to ACBs?
- Does gallery response times improve over time as they get more familiar with CMS?
- What's the max timeframe that is considered "acceptable" (e.g. CVR remains constant for up to 24 hours gallery response, then drops off)
- How does time to first gallery response relate to time to 3-day handshake?
> (Even if response time doesn't have as big an effect as we expect, we will still likely prioritize this work to improve the collector experience but in that case we'll have different success metrics to track these initiatives)

_[2] Scope Looker cleanup_ - [Joel Auerbach](github.com/joelauerbach)

_Add pageview "events" in belvedere_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein)
> https://github.com/wrgoldstein/belvedere/pull/4

_[4] GMV Product work_ - [Ani Petrov](github.com/anipetrov)
> * events around modals: https://github.com/artsy/collector-experience/issues/148
> * schema and QA for new eigen onboarding https://github.com/artsy/eigen/issues/2178


_[8] Pull article bodies and perform NLP transformations_ - [Ani Petrov](github.com/anipetrov)
> * collaborative (what audiences share an audience)
* NLP
* look at what people who buy are reading

_Random requests_ - [Ani Petrov](github.com/anipetrov)
> * Get Jesse set up with Workbench
* Overview of multitouch for marketing
* Start the conversation around path to scale


February 9
-----
_funnel for sarahg on sign up flow_ - 

_Document and operationalize multitouch attribution_ - [Ani Petrov](github.com/anipetrov)
> Documentation: https://github.com/artsy/minotaur/blob/master/doc/reference/multitouch_attribution.md
> Looker: https://github.com/artsy/looker/pull/677
> Basic updates to the tables: https://github.com/artsy/fulcrum/pull/468

_Not for sale works can now be inquired: start recording availability status at time of inquiry and enrich inquiry requests tables in fulcrum and looker_ - [Ani Petrov](github.com/anipetrov)

_Pair on Artist page sign up prompt analytics with Matt Z_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/collector-experience/issues/34#issuecomment-271702686
https://github.com/artsy/collector-experience/issues/92

_Artist page AB test_ - [Ani Petrov](github.com/anipetrov)

_criteo_ - [Joel Auerbach](github.com/joelauerbach)
> Try to approximate criteo's 30 day window, or use multi-touch attribution
> how many inquiries can we attribute to criteo within a 30-day window?
best way to do 30-day windows?
are people inquiring on the thing that they clicked on?

_Auctions model feature requests_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/presentation/d/1aXkgIiMF5cW1kxrv3QJG-pS-cHCqzUc9bmxzgkHTkwc/edit?ts=588b8315#slide=id.g1ba316cd48_0_108

_Sailthru click/open data -> Redshift_ - [Joel Auerbach](github.com/joelauerbach)
> Sara,
> Another suggestion to try is the blast_export Job. I believe this is what you are looking for.
> Sample syntax:
> POST/Job
> {
    "job":"blast_query",
    "blast_id":12345
}
The result will be a CSV file containing user level data (open_time, click_time, etc) for the specified campaign.
> Let me know if you have any further questions regarding this.
> Thanks!
> Karbao Szeto
Engineer, Select Support


January 28
-----
_Eigen logged in events and funnels: mixpanel funnel vs raw numbers are vastly different_ - [Ani Petrov](github.com/anipetrov)

_african auction partner analysis_ - 
> from @sureyya: hi team. i need some analysis of our African user base for a potential auction partnership. Any demographics for our users on the continent? number of subscribers? Top cities? How have the page views for these pages increased in the last 2 years/1 year: CONTEMPORARY AFRICAN ART, AFRICAN ART, AFRICA, EAST AFRICAN ART.
> [12:33]  
Also specifically searches /followers for these artist names: El Anatsui, Julie Mehretu, Wangechi Mutu

_automated email to finance + auctions about last month's sales + hammer prices etc_ - [Joel Auerbach](github.com/joelauerbach)

_Sailthru: prepare a one-off upload of our proposed user data import to ensure that the data is usable for the use cases Marketing is envisioning_ - [Joel Auerbach](github.com/joelauerbach)

_Fair KPIs followup_ - [Joel Auerbach](github.com/joelauerbach)
> onsite signups, update dash

_Look into popular artists feature on the /collect page performance_ - [Ani Petrov](github.com/anipetrov)

_we stopped sorting user devices into mobile web since the last week of november, why?_ - [Ani Petrov](github.com/anipetrov)
> https://artsy.looker.com/explore/artsy/users?qid=5Ms0XeKIqIUUaYpFm42UYx
> Seems to be a bug introduced with the server events firing (where force/mG users’ user agents were overwritten and now look like this: `node-superagent/1.8.5`)
> Craig instrumented a fix!
force: https://github.com/artsy/force/pull/780#event-938702088
microgravity: https://github.com/artsy/microgravity/pull/106#event-938702266

_[2] fix sql bug in minotaur_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/blob/master/jobs/price_inference.py#L32

_Artist page cta AB test instrumentation w/ Matt Z_ - [Ani Petrov](github.com/anipetrov)

_add first time vs repeat on inquiry level_ - [Ani Petrov](github.com/anipetrov)

_ML review_ - [Ani Petrov](github.com/anipetrov)
> Present Naive Bayes



January 20
-----
_add partner contacts to purchases explore_ - [Joel Auerbach](github.com/joelauerbach)
> Allow Finance to invoice institutions for purchased works (?)

_Jessica help with how many times a liaison should talk to a gallery in a month to forestall churn_ - [Will Goldstein](github.com/wrgoldstein)

_Jessica and Ginji want historic look at liaison MRR and churn over time_ - [Will Goldstein](github.com/wrgoldstein)

_Fulcrum slug length issue_ - [Will Goldstein](github.com/wrgoldstein)

_[5] LTV validation_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein)
> Signals that drive inquiries/auction activity

_[2] Fair KPIs_ - [Joel Auerbach](github.com/joelauerbach)

_[4] Elena help Gallery Insights_ - [Joel Auerbach](github.com/joelauerbach)

_[2] On the inquiry level indicate if the user created an account to inquire_ - [Joel Auerbach](github.com/joelauerbach)

_[4] QA auction gmv_ - [Joel Auerbach](github.com/joelauerbach)
> Don't forget currency conversions

_[4] Check in and report on purchase requests AB test_ - [Ani Petrov](github.com/anipetrov)

_[1] Recreate live sale reports in Looker_ - [Joel Auerbach](github.com/joelauerbach)
> add highest bid on each lot

_List of logged in users looking up a gallery phone number + their inquiry status for that work_ - [Ani Petrov](github.com/anipetrov)

_Requests_ - [Ani Petrov](github.com/anipetrov)
> * New artwork count: https://github.com/artsy/looker/pull/660
* Users with access to institutional partners that are not listed as contacts: https://github.com/artsy/minotaur/blob/master/queries/institutional_partners/access_users_not_contacts.sql
* Show phone number events: https://artsy.looker.com/sql/xw5cyb6wn6jryc
https://artsy.looker.com/sql/cpy6nyvnnygbxw
* Monthly investor updates: redo custom graphs
* Board deck questions: GMV, inquiry value, etc
* Proper inquiry hook for criteo (inquiry:sync)


_[6] ML Review_ - [Ani Petrov](github.com/anipetrov)
> SVG 


January 13
-----
_[1] QA auction analysis deck_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/presentation/d/1zABWnSk9iKREGuKce-t7ShFXT_ER1lrmH1SPt8P1ozo/edit#slide=id.p

_[2] Automate reporting for GW weekends_ - [Ani Petrov](github.com/anipetrov)
> Maja used to manually count artworks and look for pageviews URL by URL for all gallery weekends. We automated this significantly with a few looks and a query. 
> https://github.com/artsy/minotaur/blob/master/queries/gallery_partnerships/gallery_weekends_stats.sql

_[2] OH requests_ - [Joel Auerbach](github.com/joelauerbach)

_Schema for Artist page CTA AB test_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/collector-experience/issues/92
> + pair with Matt on implementing this

_[2] Editorial CTA AB test_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein)

_[2] Identify how many active users we've got on Artsy who auth with a Twitter account_ - [Joel Auerbach](github.com/joelauerbach)

_[6] Pull numbers for UBS: young, wealthy, UK-based art collectors who have interacted with UBS-sponsored content_ - [Ani Petrov](github.com/anipetrov)


January 6
-----
_Think through interviewing rubrik_ - [Will Goldstein](github.com/wrgoldstein)

_Build first draft of ad buying calculator_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/presentation/d/1hzQE5C7XjOVRxyV91QuLlrXaYNLhCpJB_ilIeXcqkdc/edit?ts=586bd0e0#slide=id.p

_LTV analysis_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/issues/168

_Popular Artists on /collect_ - [Ani Petrov](github.com/anipetrov)
> QA: https://github.com/artsy/collector-experience/issues/82
Analytics: https://github.com/artsy/collector-experience/issues/83

_Eigen retention in Fulcrum and Looker_ - [Ani Petrov](github.com/anipetrov)
> Fulcrum PR: https://github.com/artsy/fulcrum/pull/443
[End result](https://artsy.looker.com/looks/3106):
![image](https://cloud.githubusercontent.com/assets/8701687/21699699/f4203440-d36a-11e6-8a07-099164b0f9f4.png)

_Add mG_production.pages as a source table in pagetype rake_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/444

_[4] Editorial email retention (force + mG)_ - [Ani Petrov](github.com/anipetrov)
> This was actually done before the holidays; 
fulcrum PR: https://github.com/artsy/fulcrum/pull/431
> end result: https://artsy.looker.com/explore/analytics/force_mg_account_creation_retention?qid=rpjUUueUCwswIyN9uSbHvk&toggle=vis

_Add os, device, device_type from browsers to session level_ - [Ani Petrov](github.com/anipetrov)


December 16
-----
_QA on EOY analytics_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/force/pull/496

_[3] Show the 26B inventory number (undeleted artworks) over time and including FX._ - [Will Goldstein](github.com/wrgoldstein)

_[2] Created account QA_ - [Ani Petrov](github.com/anipetrov)
> getting client and server tracking synced:
> force https://github.com/artsy/force/pull/432
mG https://github.com/artsy/microgravity/pull/67 

_[2] Queries for GMV_ - [Ani Petrov](github.com/anipetrov)

_[3] Figure out eventing around purchase requests + QA_ - [Ani Petrov](github.com/anipetrov)
> design and overall setup: https://github.com/artsy/collector-experience/issues/7
> differentiate inquiry requests: https://github.com/artsy/collector-experience/issues/46#issuecomment-264999057
> eventing: https://github.com/artsy/force/issues/463
> AB test detailed setup: https://github.com/artsy/force/issues/434
> test length: 
> * if we are measuring the inquiry rate per pageview for exact priced works and want a minimal detectable effect of 20%, we are looking at ~8 weeks (we need a sample of 154,981 pageviews per variation which we would expect to see in about 16 weeks)  minimal detectable effect of ~20% in this case means detecting +/- 75 inquiries monthly
> * if we are measuring the inquiry rate per pageview for exact priced or displayed price range works and want a minimal detectable effect of 15% we are looking at ~4 weeks; minimal detectable effect of ~15% in this case means detecting +/- 80 inquiries monthly

_Rework retention graph (by Tuesday)_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/431

_Some adjustments for marketing queries_ - [Ani Petrov](github.com/anipetrov)

_EOY promotion on home page analytics_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/force/issues/568

_[6] Looker II prep and class_ - [Ani Petrov](github.com/anipetrov), [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach)


December 9
-----
_[4] Looker I prep and class_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein), [Ani Petrov](github.com/anipetrov)

_[2] Add postgres to Jenkins AMI_ - [Will Goldstein](github.com/wrgoldstein)
> 
william [4:00 PM]  
hey humans, could anyone take some time to pair with me on making fulcrum tasks a little more robust to failures with `apt`
> slackbot Custom Response 	[4:00 PM]  
:couple:
> william [4:01 PM]  
http://joe.artsy.net/job/fulcrum-load-after-extract/782/console
> [4:01]  
 ```00:00:36.565 E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
00:00:36.566 E: Unable to lock directory /var/lib/apt/lists/
00:00:36.575 Build step 'Execute shell' marked build as failure
```
> [4:04]  
http://askubuntu.com/questions/335794/could-not-get-lock-var-lib-apt-lists-lock looks like it usually means another process is using `apt` at the same time
 askubuntu.com
Could not get lock /var/lib/apt/lists/lock
when I try to apt-get update I'm getting the below error,E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)E: Unable to lock directory /var/lib/apt/lists/ 
 
 
> barry [4:04 PM]  
yeah, hadn't gotten to typing that since I'm eating :smile:
> [4:06]  
can you re-run that?
> joey [4:07 PM]  
@william you can avoid `apt` calls by having the required prerequisites installed in the AMI already.
> [4:07]  
The job will be much faster too. I highly recommend it.
> https://github.com/artsy/jenkins-cookbooks

_[4] Core users in looker_ - [Joel Auerbach](github.com/joelauerbach)

_[4] Auction signals analysis_ - [Joel Auerbach](github.com/joelauerbach)

_Looker I class!_ - 


December 2
-----
_[4] Churn forecasting_ - [Will Goldstein](github.com/wrgoldstein)

_[3] Enriched pageviews_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/421

_[4] Looker II curriculum_ - [Joel Auerbach](github.com/joelauerbach)
> https://docs.google.com/presentation/d/1d_6wYHKDoonfXiHRKh7LyCyoaygNwRbO1ytUlB1w2B4/edit#slide=id.g13cb24746d_0_152

_[4] Write up inquiry cycle findings_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/166

_[3] Examine CMS usage trends as it pertains to gallery health / churn_ - [Joel Auerbach](github.com/joelauerbach)

_[6] Marketing: cohort analysis_ - [Ani Petrov](github.com/anipetrov), [Joel Auerbach](github.com/joelauerbach)

_[4] Marketing: miami signup modal_ - [Ani Petrov](github.com/anipetrov)
> final reporting: 
https://artsy.looker.com/sql/zgqbctggsqbp7b


_[3] Marketing: generate lists of partners for inquiry retargeting_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/blob/master/queries/marketing/partners_inq_retargeting.sql

_[4] AB test specs for purchase requests_ - [Ani Petrov](github.com/anipetrov)

_[2] Investor deck graphs_ - [Ani Petrov](github.com/anipetrov)


November 25
-----
_[2] Remove references to auction_bids and delete table_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/410
https://github.com/artsy/looker/pull/617

_[4] Followups on auctions refactor_ - [Joel Auerbach](github.com/joelauerbach)
> * Add reserve check to winning bids
* Separate out postsales completely
* Finalize Looker components, reflecting these changes
> https://github.com/artsy/fulcrum/pull/410
https://github.com/artsy/looker/pull/617

_[6] Marketing: miami signup modal_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/minotaur/blob/master/knowledge/Nov2016_miami_user_acquisition.md

_[0] Q: A/B test for works with exact prices (shipping on top reminder)_ - [Ani Petrov](github.com/anipetrov)


November 18
-----
_[1] Official report on forced sign up at inquiry AB test_ - [Will Goldstein](github.com/wrgoldstein)
> https://github.com/artsy/force/issues/401

_[1] Close out forced sign up at inquiry AB test_ - [Will Goldstein](github.com/wrgoldstein)

_[2] Update Candela tables in Fulcrum to allow sending early analytics emails for fairs_ - [Will Goldstein](github.com/wrgoldstein)

_[3] Interview three candidates for editorial_ - [Will Goldstein](github.com/wrgoldstein)

_[4] Make "Internal" traffic go away and clean up sessions: part 2_ - [Ani Petrov](github.com/anipetrov)
> PR: https://github.com/artsy/fulcrum/pull/406
1. Clean out old funnels that we have no use of anymore
  * `application_funnel`
  * `inquiry_funnel`
  * various helpers for the above funnels
  * auctions funnels will be cleaned out when the auction traffic dashboards and definitions are restructured to point to new core tables
  * fair funnels need to be retired, too, but they are too deeply connected 
> Note that the looker cleanup to make sure that nothing points to the new tables has already been done: https://github.com/artsy/looker/pull/611
> 2. Remove old event aliasing that used to support the outdated funnels
  * `mapped_registrations`, `mapped_inquiries` are deprecated in favor of the new `enriched_event` tables
  * note that `force_mapped_experiment_viewed` has also been retired; you can use `force_enriched_experiment_viewed` and `microgravity_enriched_experiment_viewed` instead; both of these tables exclude events from people that have been placed in multiple variation buckets
> 3. Remove internal traffic: for all "internal" sessions, point to the source and landing information of the last non-internal session for that visitor.
> 4. Rename and restructure tables
> TODOs:  
- [ ] Once this PR is in, we need to go back and drop all `analytics.` tables that are no longer needed
- [ ] Auctions traffic tables refactor
- [ ] Fairs traffic tables refactor
> 
cc @joelauerbach @wrgoldstein 

_[2] Push notifications I_ - 51c260740fb65f9753001561, [Ani Petrov](github.com/anipetrov)
> Explore different solutions to our push needs

_[1] Add reporting responsibilities to analytics mlp doc_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/pull/163

_[3] Social: auction campaigns_ - [Joel Auerbach](github.com/joelauerbach)

_How should we represent pageviews in looker_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/616

_[2] New sign up modal eventing_ - [Ani Petrov](github.com/anipetrov)
> **Analytics**
  
**Front-end (client AND server-side) `created_account` event**:
- acquisition_initiative: ["Miami 2016", "Organic search artist page"]
    - marketing triggered modals: admin tool should allow for setting initiative (from a dropdown menu?); one acquisition_initiative can have multiple modals associated with it
    - other source triggered modals: hard-coded
    - activity/intent triggered modals: do not have an acquisition_initiative set; they have `context` instead
- modal_id: [574, 2]
    - marketing modals automatically generated by admin tool when a modal is created by a marketer; other source/activity/intent modals generated for hard-coded modals; we will need to maintain a db of these
- signup_service: [email, facebook, twitter]
> **Other front-end (client) events:**
- open/show_signup_modal: modal_id, acquisition_initiative
- dismiss/close_signup_modal: modal_id, acquisition_initiative, modal_stay_length (in seconds)
- failed_to_create_account: modal_id, acquisition_initiative, errors
- clicked_login: modal_id, acquisition_initiative
- successfully_logged_in: modal_id
 
**Back-end modal model:**
- id
- title
- subtitle
- cta
- image
- acquisition_initiative
- type
- size
- destination (after signup)
> will need QA and figuring out the server/client event thing


_QA inquiry flow w Brian_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/force/issues/404

_GMV check-ins_ - [Ani Petrov](github.com/anipetrov)

_[4] Eigen retention, inquiry rate, etc exploration_ - [Ani Petrov](github.com/anipetrov)


November 11
-----
_[0.5] Analytics/Looker intro for Forbes_ - [Joel Auerbach](github.com/joelauerbach)

_[4] Break down and code auctions dashboards_ - [Joel Auerbach](github.com/joelauerbach)
> Fulcrum PR:
https://github.com/artsy/fulcrum/pull/410
> Original dashboards
https://artsy.looker.com/dashboards/72
https://artsy.looker.com/explore/analytics/sales?qid=iJj1v9TBFIZIqxq1mwPqUK
https://artsy.looker.com/explore/analytics/sales?qid=g4aKMnq1mkLSjwdN7Htdq8

_Looker classes planning: Looker I presentation_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein), [Ani Petrov](github.com/anipetrov)

_[1] Volt analytics intro_ - [Ani Petrov](github.com/anipetrov)
> Chatted with Brent and Garren, looked into some looker dashes and CMS-related views, started GA integration for volt

_[6] Make "Internal" traffic go away and clean up sessions: part 1_ - [Ani Petrov](github.com/anipetrov)
> PR: https://github.com/artsy/fulcrum/pull/406
1. Clean out old funnels that we have no use of anymore
  * `application_funnel`
  * `inquiry_funnel`
  * various helpers for the above funnels
  * auctions funnels will be cleaned out when the auction traffic dashboards and definitions are restructured to point to new core tables
  * fair funnels need to be retired, too, but they are too deeply connected 
> Note that the looker cleanup to make sure that nothing points to the new tables has already been done: https://github.com/artsy/looker/pull/611
> 2. Remove old event aliasing that used to support the outdated funnels
  * `mapped_registrations`, `mapped_inquiries` are deprecated in favor of the new `enriched_event` tables
  * note that `force_mapped_experiment_viewed` has also been retired; you can use `force_enriched_experiment_viewed` and `microgravity_enriched_experiment_viewed` instead; both of these tables exclude events from people that have been placed in multiple variation buckets
> 3. Remove internal traffic: for all "internal" sessions, point to the source and landing information of the last non-internal session for that visitor.
> 4. Rename and restructure tables
> TODOs:  
- [ ] Once this PR is in, we need to go back and drop all `analytics.` tables that are no longer needed
- [ ] Auctions traffic tables refactor
- [ ] Fairs traffic tables refactor
> 
cc @joelauerbach @wrgoldstein 

_[2] Intro to Analytics for new GMV leads_ - [Ani Petrov](github.com/anipetrov)

_[1] Present conversion rate re-definition for GMV_ - [Ani Petrov](github.com/anipetrov)


November 4
-----
_Add tracking to marketo pages (apply.artsy.net)_ - [Will Goldstein](github.com/wrgoldstein)
> insights.artsy.net and the other

_Enriched core users table_ - [Joel Auerbach](github.com/joelauerbach)

_[6] Finish auctions tables restructure_ - [Joel Auerbach](github.com/joelauerbach)

_Looker classes blab_ - 
> Agreed upon organizing principles and frequency.  Essentially, 3 levels, the first two presenting concepts from "What data do we have?" to talking about joins.  The third level will be team specific.

_Look pretty_ - [Zack Gow](github.com/zackgow)

_Prediction Games: How many inquiries will there be on Wednesday, November 2, 2016?_ - [Will Goldstein](github.com/wrgoldstein), [Ani Petrov](github.com/anipetrov), [Zack Gow](github.com/zackgow), [Joel Auerbach](github.com/joelauerbach)
> - deliviered inquiries only
> #### Results
> Ani: 560, Will: 550, Zack and Joel: 450


_[4] Commission Calculation_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach)
> Presented, folks are excited.  There's follow up work todo which I'll make a new card for.

_[0] Communicate with communications about whether they need fairs separate from referrals_ - [Will Goldstein](github.com/wrgoldstein)
> Outcome: Reincorporated fair traffic.

_[4] Eigen 3.0 launch data_ - [Ani Petrov](github.com/anipetrov)

_Forced log in inquiry AB test followups_ - 


October 28
-----
_Present at GMV meeting_ - [Ani Petrov](github.com/anipetrov)
> Presentation slides: https://docs.google.com/a/artsymail.com/presentation/d/1qIun-H92xnzJAIh44X9_0pJtvXuzVBaGOZaWQZSPvBY/edit?usp=sharing

_[3] End of year feature data pulls_ - [Joel Auerbach](github.com/joelauerbach)
> Parsed out UBS data and updated pulls from Artsy and Semrush.

_[12] Restructure auctions base tables_ - [Joel Auerbach](github.com/joelauerbach)
> New tables:
> * `online_sale_bidder_positions`
* `sale_artwork_outcomes`
* `sale_outcomes` (needs some followup after meeting with Ginji and Devang about auctions KPIs next week)
* `enriched_users` (broader than auctions, still needs some followup)
> 
> I believe we can now get rid of `analytics.auction_bids`

_Board deck support_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach), [Ani Petrov](github.com/anipetrov)

_Estimating cost benefit for inquiry campaigns with marketing (retargetting analysis)_ - [Ani Petrov](github.com/anipetrov)

_Restart editorial CTA AB test_ - 


Oct 21
-----
_[2] Eigen onboarding eventing QA_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/eigen/issues/1459#issuecomment-242344130

_[2] Present to GFI for Fairs/Inquiries_ - [Zack Gow](github.com/zackgow), [Joel Auerbach](github.com/joelauerbach)

_[1] Why is qeckoboard still on the screens on 25?_ - [Zack Gow](github.com/zackgow)
> Not sure why Geckoboard was still on the screen, as I changed it like two months ago.
> I updated the bottom screen with https://artsy.looker.com/dashboards/125

_[2] pairing with Isac to schedule price-inferencing_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/150#pullrequestreview-3709512

_[3] Present to GMV for Inquiries/User acquisition_ - [Ani Petrov](github.com/anipetrov)
> https://docs.google.com/presentation/d/1d6xiqvnMQ69yp-DNa18sppR3vMZ6R0SMsiJkleCAm6Q/edit#slide=id.g1125549076_0_100

_Board deck support_ - [Joel Auerbach](github.com/joelauerbach), [Will Goldstein](github.com/wrgoldstein), [Ani Petrov](github.com/anipetrov)


Oct 14
-----
_Looker cleanup_ - [Zack Gow](github.com/zackgow)

_[6] inquiry slice and dice_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/152

_[3] Remove `mobile_and_desktop_combined_pages` from looker_ - [Zack Gow](github.com/zackgow)
> Sarah pointed out this: https://files.slack.com/files-tmb/T02531TU5-F2JTGBDSN-8f3b8cc44f/pasted_image_at_2016_10_03_09_34_pm_1024.png

_[8] Monthly investor updates_ - [Ani Petrov](github.com/anipetrov)

_[1] Finishing touches on publishing dashboard_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/589

_[1] Fix collect pagetype (and look for other errors)_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/377

_[2] UBS followup_ - [Joel Auerbach](github.com/joelauerbach)

_[2] Eigen projections_ - [Ani Petrov](github.com/anipetrov)

_GMV Product roadmapping_ - [Ani Petrov](github.com/anipetrov)

_Looker slack bot_ - [Ani Petrov](github.com/anipetrov)


Oct 7
-----
_[0] add notebook for gallery scoring_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/151

_"Slice and dice" inquiries and purchases_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/152

_[1] Add partner inventory id in artworks table in redshift and looker_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/gravity/pull/10459

_[1] Sailthru for MG for Sara_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/fulcrum/pull/366


_[8] Price Inferencing Updates_ - [Will Goldstein](github.com/wrgoldstein), [Zack Gow](github.com/zackgow), [Joel Auerbach](github.com/joelauerbach)
> - checking whether adding medium will make a difference
- check whether gradient boosting performs better on logged price
- make a separate production-requirements.txt that contains just the minimal dependencies
> https://github.com/artsy/minotaur/pull/150

_Lead scoring (initial exploration)_ - [Joel Auerbach](github.com/joelauerbach)
> Life cycle questions:
> time to first inquiry
time between first seeing artwork and inquiring on it

_[6] Qualified collectors for Miami_ - [Joel Auerbach](github.com/joelauerbach)
> Collector level 2 or 3
Signups from auction results pages
Visits to auction results pages
Price dropdowns
> Compare to other big fair months - Armory, Miami last year
> -----
> Initial estimates look to be around 4-6K (based largely on collector levels, due to small contributions from other factors represented here. Needs some followup related to ongoing lead-scoring work.


_[2] Follow up on Criteo attribution_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/369
https://github.com/artsy/fulcrum/pull/373

_Multi-touch attribution blab_ - [Ani Petrov](github.com/anipetrov)
> Next steps: figure out some stats about sale cycle and continuous user engagement before we get organize a wider brainstorm with domain experts


_[2] Forced inquiry sign up A/B test_ - [Ani Petrov](github.com/anipetrov)
> Analytics instrumentation is up to speed; note that if a visitor inquiries for the first time currently they will get a reminder to personalize their message to the gallery, so if the inquiry goes through, they click send more than once -- will be important for analysis.
> Test duration will be 2-3 weeks to check the inquiry drop. Conversion rate of (sessions with inquiry/sessions with artwork pv) for logged out/partial sessions where the user did NOT have an account prior to the session, is calculated as follows: https://artsy.looker.com/sql/6p8krrw2nm6kzt
> Related issues:
Test set-up: https://github.com/artsy/force/issues/80
QA round 1: https://github.com/artsy/force/issues/191
QA round 2: https://github.com/artsy/force/issues/228


_[1] Instrumentation around show inquiries_ - [Ani Petrov](github.com/anipetrov)
> We receive very few of those, 10-30 a month https://artsy.looker.com/sql/pjyj6vzhpk3wpc; however, we should have instrumentation around it
> Instrumentation issue: https://github.com/artsy/force/issues/236


_[3] Add unique Artsy buyers stats and graphs (Tim's most recent requests) to looker_ - [Ani Petrov](github.com/anipetrov)

_One-offs_ -


Shipped Sept 30
-----
_[4] Candela follow up work_ - [Will Goldstein](github.com/wrgoldstein)
> Also check in on renewal reports.


_[2] Fix account creations/logged in_ - [Joel Auerbach](github.com/joelauerbach), [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/349


_[2] break "retargeting" into its own attribution medium_ - [Joel Auerbach](github.com/joelauerbach), [Zack Gow](github.com/zackgow)
> https://github.com/artsy/fulcrum/pull/350


_[1] Funnels for Brian_ - [Zack Gow](github.com/zackgow), [Ani Petrov](github.com/anipetrov)
> - logged in user > filters to artists you follow > goes to an artwork page > inquiries

> - logged in user > filters to artists you follow > goes to an artwork page > saves artwork (edited)

> Brian wants to investigates these behaviors (Mixpanel, Looker, separate queries -- what's best?)

> uggliest query on the face of the earth: https://github.com/artsy/minotaur/blob/master/queries/collector_gmv/collect-click-artwork-inquiry.sql


_[1] maybe retire mixpanel?_ - [Zack Gow](github.com/zackgow)
> *Is there any data in there that you think we should export before kicking it (like the events we collected prior to the Segment integration)? Are there any other reasons you can think of for keeping it around?*

> **Joey**:  Anil was using it for search queries and related click/select events, but possibly only used it because he couldn’t find the equivalent data in our modern systems. I don’t care much for the old data. I _do_ care about ensuring we’re tracking everything via modern methods that we used to track via Mixpanel.

> **Dylan**: There’s a project called github.com/artsy/phonon that may only publish data to Mixpanel. Ilya, Joey and Alexander built it years ago. It provides widgets that galleries can embed on their own pages such as "follow us on Artsy".  The data is potentially neat because it’s a view that Artsy has uniquely into our partners’ own website traffic.

> 1) unsure of how many galleries have set up the widget
2) if the eventing happens via segment :pray:, we may be ok to just dump the data in mixpanel to s3 or somewhere and handle the switcheroo
3) Talk to whatever the equivalent team is to “partner success” about it (ultimately it may be a question for Robert since basically nobody own the service)

> **Eloy**: Eloy has not ever really used it.

> **Orta**: Nope.

> **Craig**: No good reasons for keeping it off the top of my head. You all will know better than I if we should try an export old Mixpanel data. So :+1: to dropping it on my end. Let me know if I should do anything to help make it happen on my end—pretty sure we're just using it through Segment, so should be as simple as toggling it off integrations.

> **Anil**: Would prefer a GUI with saved graphs; especially since he is trying to bring all search in house. Mostly just needs basic time series graphs that can be faceted.  Let us know when you plan to get rid of MP as there's also a heat job using search and pageview data from there that we might need to move to Spark.

> The front-end events he's looking at are:

> 'searched from header, with results'
'searched from header, with no result'
'selected item from search'
'focused on search input'

> and:

> 'hit enter on fair search'
'selected item from fair search'

> ex. https://mixpanel.com/report/82115/segmentation/#action:segment,arb_event:'Selected%20item%20from%20search',bool_op:and,chart_analysis_type:linear,chart_type:line,from_date:-29,ms_checked:('Selected%20item%20from%20search':!t),ms_values:!('Selected%20item%20from%20search'),to_date:0,type:general,unit:day

> https://mixpanel.com/report/82115/segmentation/#action:segment,arb_event:'Searched%20from%20header,%20with%20results',bool_op:and,chart_analysis_type:linear,chart_type:line,from_date:-29,ms_checked:('Searched%20from%20header,%20with%20results':!t),ms_values:!('Searched%20from%20header,%20with%20results'),to_date:0,type:general,unit:day

> https://mixpanel.com/report/82115/segmentation/#action:segment,arb_event:'Searched%20from%20header,%20with%20no%20results',bool_op:and,chart_analysis_type:linear,chart_type:line,from_date:-167,ms_checked:('Searched%20from%20header,%20with%20no%20results':!t),ms_values:!('Searched%20from%20header,%20with%20no%20results'),to_date:0,type:general,unit:week

>
Solution: Add front-end events back to Looker (as needed) and only give devs/designers permissions. Will allow Brian, Anil, etc. to investigate front-end events they care about.


_[8] Gallery Scoring_ - [Zack Gow](github.com/zackgow)
> - meet with jesse for expectations for meeting
- tweak scores


_[1] add additional info to sailthru explore_ - [Zack Gow](github.com/zackgow)
> https://artsy.looker.com/explore/analytics/sailthru?qid=vD7mvszpGDBMgJex7L4TWu

> There's cases where a single person is sending lots of inquiries, bids, etc. Sara would like to see unique people doing these actions.


_Add conversion measures to article_tracks_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/looker/pull/577


_[9] Looker FAQ_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/minotaur/blob/master/knowledge/looker_faq.md


_[1] (Before Wednesday) Make a auctions bidding dashboard_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/dashboards/analytics::live_bidding_report


_Minor tweaks to PM funnel queries_ - [Joel Auerbach](github.com/joelauerbach)
> Following fixes/improvements made in
https://github.com/artsy/fulcrum/pull/340
https://github.com/artsy/fulcrum/pull/349

> Final queries

> A. Signup funnel

> 1. By landing page type: https://artsy.looker.com/sql/kbngy2sytygr8d
2. By medium: https://artsy.looker.com/sql/ybnksmrcw9txqc

> B. Professional buyer program

> 1. Pageviews through applications
a. By medium: https://artsy.looker.com/sql/f8vhsmgjncdprv
b. By source: https://artsy.looker.com/sql/vvxfsvxsgz7hbm
c. By campaign: https://artsy.looker.com/sql/qjsxzhrrbcs2g9

> 2. Professional buyer inquiries and purchases
a. By medium: https://artsy.looker.com/sql/gxzcvyfrxhwfw8
b: By source: https://artsy.looker.com/sql/6c6ssyw6fqppq7
c: By campaign: https://artsy.looker.com/sql/87cdcsspf8wzny



_Add  `is_sale_artwork` to artworks explore in looker_ - [Ani Petrov](github.com/anipetrov)

_[1] Add total inquiries to attribution dashboard (in addition to # sessions with inquiries)_ - [Ani Petrov](github.com/anipetrov)

_One-offs_ -

_Multi-touch round 1_ - [Ani Petrov](github.com/anipetrov)
> A basic model where all touches 28 days prior to conversion receive credit equally. Note that this model is typically used when no one particular interaction is known to convert customers, and the goal is ongoing marketing engagement.

> https://github.com/artsy/fulcrum/pull/359




Shipped Sept 23
-----
_includes fix feature calculations in price inferencing_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/147


_Investigate and fix fallout from changed price for standard subscriptions_ - [Will Goldstein](github.com/wrgoldstein)

_Talk to GR about test galleries in production_ - [Zack Gow](github.com/zackgow)
> Also check with GP.

> Ideally they're not creating any and we can delete the old ones.  They certainly should not be getting paid commission on them.  If they _need_ test galleries in production, remove them from commission calculation.


_Auctions dash reconciliation_ - [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/dashboards/artsy::auctions_kpis?filter_date=24%20months&filter_config=%7B%22filter_date%22:%5B%7B%22type%22:%22past%22,%22values%22:%5B%7B%22constant%22:%2224%22,%22unit%22:%22mo%22%7D,%7B%7D%5D,%22id%22:1%7D%5D%7D

> sell through rate by value, exclusively online totals 3.949MM for total low estimate and it should be ~8.949 (tomorrow 11.949)


_Retire `analytics.radiation_conversations`_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/fulcrum/pull/341


_Move partner subscription sequence logic from gravity to fulcrum_ - [Joel Auerbach](github.com/joelauerbach)
> https://github.com/artsy/gravity/pull/10413
https://github.com/artsy/fulcrum/pull/344


_Check PSM definitions for consistency_ - [Joel Auerbach](github.com/joelauerbach)
> Make sure a churn in one month doesn't later become a non-churn;

> - if a partner ends a subscription then two months later reactivates, the first subscription should have be marked churn


_Add new article events / impressions to looker_ - [Joel Auerbach](github.com/joelauerbach)
> Current implementation:
https://github.com/artsy/force-private/issues/5375

> New issues logged:
https://github.com/artsy/force/issues/143
https://github.com/artsy/microgravity/issues/21


_Unique purchasers/ACBs_ - [Ani Petrov](github.com/anipetrov)
> Live auctions are logged into Purchases, so are post-auction sales -- everything is manual so far. The team is working on automating it. Considering this and some other caveats (eg. )

>
number of distinct buyers to date: https://artsy.looker.com/sql/vcq48rzzhxc3pk
number of distinct buyers in august 2016: https://artsy.looker.com/sql/gx5brjsqz5zd6v
number of distinct repeat buyers in august 2016: https://artsy.looker.com/sql/mffsq6wmb2dwgk
number of first-time buyers in August 2016:
https://artsy.looker.com/sql/chcj9fzbmy9cvz


_Purchase request data support_ - [Ani Petrov](github.com/anipetrov)
> Look through examples of exact price conversations that received 3wh but no purchase: https://artsy.looker.com/sql/d5ftrd6d8q3549

> Inquiry request "funnel": https://artsy.looker.com/sql/xsx7v7wxv8rbsf

> Writeup: https://github.com/artsy/minotaur/blob/master/knowledge/purchase_requests.md



Shipped Sept 16
-----
_Dashboard for Matt Domino (Editorial)_ - [Joel Auerbach](github.com/joelauerbach)
> Matt's raw table: https://artsy.looker.com/x/9Yns2Yq

> Completed LookML dashboard: https://artsy.looker.com/dashboards/analytics::editorial_weekly_metrics


_[1] new_account metrics for ab test_ - [Zack Gow](github.com/zackgow)

_Looker Cleaning_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/looker/pull/558

> Removed old derived tables (taking ~50 minutes build time each night)
Removed joins from explores
Fixed typos


_psm updates_ - [Will Goldstein](github.com/wrgoldstein), [Joel Auerbach](github.com/joelauerbach)
> - Add concept of re-activation for galleries that let the grace period lapse but sign on again before 6 months (at which point they become a reup)
- Add "not re-up" to upgrade definitions
- Use "first_completed_charge_date" for 24 month period calculations
  * 24 month periods needs to reset if a gallery is off platform for 6 months

> https://github.com/artsy/fulcrum/pull/334
https://github.com/artsy/looker/pull/554


_Funnels blab_ - [Ani Petrov](github.com/anipetrov)

_Funnels 2.0_ - [Ani Petrov](github.com/anipetrov)

_pull the trigger on reserved instances_ - [Will Goldstein](github.com/wrgoldstein)

_Drill into medium -> source -> campaign -> referring URL_ - [Ani Petrov](github.com/anipetrov)



Shipped Sept 9
-----
_Continued reporting on home page AB Test results_ - [Zack Gow](github.com/zackgow)
> queries and average per visitor per group for the following:
- inquiries
- artist follow counts
- gallery follow counts
- artwork saves within rail / globally

> reported on ab test results to gmv team

_Add editions info to redshift_ - [Will Goldstein](github.com/wrgoldstein)
> Some artworks have [editions](https://github.com/artsy/gravity/blob/master/app/models/domain/edition_set.rb) and their price information lives on the edition_set object rather than on the artwork object. We should model this so as to capture prices for edition artworks.

> Added `edition_sets` and `priced_edition_sets` dimensions:  https://github.com/artsy/gravity/pull/10360


_double counting in auctions issue still exists (ginji, erin)_ - [Will Goldstein](github.com/wrgoldstein)

_Partner Subscription Metrics work_ - [Zack Gow](github.com/zackgow), [Will Goldstein](github.com/wrgoldstein)
>
### Renewals:
https://cl.ly/38422A221r0Z

> up_for_renewal dimension is not accurate

> ### Upgrades:

> There are currently many false positives for upgrades (by our definition in PSM).

> Apparently, galleries are leaving the platform for some time, and when they return to the platform, they are being counted as an upgraded subscription.

> https://docs.google.com/spreadsheets/d/1Nfbmb4FvPh9J2y9LGciW8Mj2BW2-KGddcjnDFZldMP4/edit?ts=57b5fe8b#gid=1734972351

> ### Renewal threshold

> Currently there are several metrics that represent partners being on the platform for <25 months.

> Jessica wants this to be calculated from the `first_completed_charge_date`


_/collect filter usage for barbara_ - [Will Goldstein](github.com/wrgoldstein)
> following up on my question above ^, I have a gallery that is interested in seeing numbers for how popular figurative art is on the site. Is there anyway I could pull that?

> barbara.carvalho


_[2] update projections for inbounds_ - [Zack Gow](github.com/zackgow)
> meet with nicholas to discuss numbers for July in SF;
applications that are submitted but arent really galleries


_[0] Clearbit data into Looker_ - [Zack Gow](github.com/zackgow)
> stas [2:19 PM]
Hi Analytics, wanted to coordinate with you. Matt Z worked his magic, and now we are able to save all the clearbit data we get any time anyone places and inquiry—this is a first step into enriching our existing database. I understand that the data will be available in Admin—User. I also want to make sure that all this data is available in Looker.


_instrument /consign page_ - [Zack Gow](github.com/zackgow)
> Gallery liaison handoff


_Funnels for PM dashboards refactor_ - [Ani Petrov](github.com/anipetrov), [Joel Auerbach](github.com/joelauerbach)
> Fixed pagetypes:
https://github.com/artsy/fulcrum/pull/326

> Decided to build tables as SQL runner queries rather than Looker dashboards.

> A. Signup funnel

> 1. By landing page type: https://artsy.looker.com/sql/hpxpqvqvxpprjw
2. By medium: https://artsy.looker.com/sql/z8gpdq2bxqs3ht

> B. Professional buyer program

> 1. Pageviews through applications
a. By medium: https://artsy.looker.com/sql/tdqgy4dcbq3k8k
b. By source: https://artsy.looker.com/sql/zhf42gjjjgqp69
c. By campaign: https://artsy.looker.com/sql/hsqrtrj5qrw7qt

> 2. Professional buyer inquiries and purchases
a. By medium: https://artsy.looker.com/sql/yztcwby4yyg5jt
b. By source: https://artsy.looker.com/sql/3cvfxbkwdwhgyk
c. By campaign: https://artsy.looker.com/sql/wkcqfgqm8wtwsh



_Switch out radiation data with impulse data_ - [Ani Petrov](github.com/anipetrov), [Joel Auerbach](github.com/joelauerbach)
> https://artsy.looker.com/explore/artsy/partner_subscriptions_metrics_daily?qid=2yGZfLZvFpjhfXsMascEcZ

> Moved impulse + purchase data to new inquiry_requests table:
https://github.com/artsy/fulcrum/pull/328

> Switched out old radiation data with impulse data:
https://github.com/artsy/looker/pull/551


_create/edit prepay dimension in PSM_ - [Zack Gow](github.com/zackgow), [Joel Auerbach](github.com/joelauerbach)
> Prepay is defined as `>=6 months paid up front`

> https://github.com/artsy/looker/pull/548




Shipped August 26
-----
Note both Ani and Will were on vacation.

_[2] Looker Cleanup_ - [Zack Gow](github.com/zackgow)
> Removed board_meeting_kpis dashboard


_[3] Investigate Partner Applications_ - [Zack Gow](github.com/zackgow)

_[6] Homepage AB test cleanup_ - [Zack Gow](github.com/zackgow)
> cleaned up AB test and sent over preliminary metrics to Robert, Brian, and Cab.


_[3] Changes to renewals/re-ups-churn_ - [Zack Gow](github.com/zackgow)
> Investigated the following problem from GR:

> -----------------------
If a gallery comes back on the platform >182 from their last subscription end date, we should call this a "Reactivation within 6 months".

> When their second to last subscription ends, it should still count as a churn or non renewal in the month in which their contract expired. In other words, 'later renewals' should not count as renewals.

> For example:
Coates & Scarry
contract expired Feb 5 2016
Gemma re-activated them June 27th

> However, they are not displaying as a churn or non-renewal in Looker https://artsy.looker.com/x/7m27Bbc

> The way that we handle such cases is that they count as a churn and then a reactivation within 6 months.

> -----------------------

>
To get some more insight into some of the issues here you can look at:
https://artsy.looker.com/x/Cy5qNpN (which is using the wrong active subscription number)
https://artsy.looker.com/x/6XcwR88 (where the partner is being counted as subscribed and unsubscribed simultaneously)




Shipped August 5
-----

Offsite week

Shipped July 29
-----

_[1] Editorial numbers: how many inquiries come from readers, etc. (overlap not causation)_ - [Will Goldstein](github.com/wrgoldstein)
> Hey Matt,

> Hope you had a good week. Here's a quick way to see a comparison of various key metrics between sessions that landed on article pages vs. the others.  This is the last 90 days (defining editorial traffic as sessions that began with an article view):

> https://artsy.looker.com/x/9Yns2Yq

> Note you can also add "medium" in the left hand bar to see that while social is neck and neck with email in terms of traffic to article pages, it's much less effective in terms of driving inquiries.

> Also note that direct traffic to non article pages are more than twice as likely as social traffic to eventually end up on an article.  You can see that here:

> https://artsy.looker.com/x/ZR6QPBz

> We can dig in a bit to notice that while editorial traffic has been fairly strong through the summer, the commercial activity of those readers is dropping due to seasonal effects (this is inquiries per session since March against total sessions):

> https://artsy.looker.com/x/gTGgjKw

> I hope you'll be able to play around a bit in Looker, and look forward to talking through any questions you might have.


_[0] remove google translate cache(?) and vanity from referrals_ - [Will Goldstein](github.com/wrgoldstein)

_[inf] presentation_ - [Will Goldstein](github.com/wrgoldstein)

_[1] BMW numbers_ - [Ani Petrov](github.com/anipetrov)
> First time ever inquirers per month: https://artsy.looker.com/sql/qfznqb64rphkzf
Distinct inquirers per month:  https://artsy.looker.com/sql/n52wwpptgtf9nq
All time distinct inquirers: https://artsy.looker.com/sql/f5rf4yfqmsqm6p
Number of all-time inquiry requests: https://artsy.looker.com/x/kHczVgc
Bidder positions from auctions all-time: https://artsy.looker.com/x/qHyHkWD
Bids from live auctions:



_[1] Expose new utm params (p-social etc)_ - [Ani Petrov](github.com/anipetrov)
> Expose new utm params according to the [utm-tagging schema](https://github.com/artsy/fulcrum/pull/292)

> https://github.com/artsy/fulcrum/pull/292


_[1] Eventing around new artwork module that follows you around_ - Brian Waterson, [Ani Petrov](github.com/anipetrov), 5106bed940cedfd825006af1
> https://github.com/artsy/force/pull/5409
https://github.com/artsy/force/pull/5413
https://github.com/artsy/force/pull/5415
https://github.com/artsy/force/pull/5417
https://docs.google.com/a/artsymail.com/spreadsheets/d/17oqFli15x1SmNBu_-fPZhFifMw2BNSPJe9VdOgs1aKs/edit?usp=sharing


_[1] Artists You Follow checkbox: https://www.artsy.net/collect_ - [Ani Petrov](github.com/anipetrov), Brian Waterson, 5106bed940cedfd825006af1
> https://github.com/artsy/force/pull/5410


_[3] Gallery Relations Asks_ - [Zack Gow](github.com/zackgow)

_[4] How having an Artsy account impacts gallery applications / the listings funnel_ - Jesse Kedy, [Zack Gow](github.com/zackgow)
> https://artsy.looker.com/sql/pwjbjxwn5xst8n

> - Number of sessions from first session to submitting gallery application
- Number days from first session to submitting gallery application
- Unique applications divided by unique views of /gallery-partnerships (if session included that page)
- Qualified gallery applications divided by total gallery applications
- Closed (won) contracts divided by qualified applications


_[2] Writeup for Photography Image Size analysis_ - [Zack Gow](github.com/zackgow)
> **Summary:
 - No significant signal between image size and number of inquiries.
 - Low correlation between pageviews and installation images; Pearson coefficient of 0.11 (0.15 after dropping 2 outliers).
 **

>
Inquiries in themselves rare events, and don't show any strong correlation with size.
![](https://dlh7x4sj1uwv2.cloudfront.net/items/1Z3X2S313u1z2D3N1B1p/Image%202016-07-28%20at%2010.38.50%20AM.png?v=6f212b3a)

> As for evidence to support the claim that shows with installation images have more pageviews, I looked at shows from June onwards (1523 of them at the time of the analysis).

>
At first I looked at if any installation images were present at all and compared them to the set having none:

>
 ![](https://dlh7x4sj1uwv2.cloudfront.net/items/143B3I2h1K2Z2L1q1f1l/Image%202016-07-28%20at%2010.35.35%20AM.png?v=ecc1715e)

>

> To see a visual relationship of installation images and pageviews:
 ![ ](https://dlh7x4sj1uwv2.cloudfront.net/items/1Z3X2S313u1z2D3N1B1p/Image%202016-07-28%20at%2010.38.50%20AM.png?v=6f212b3a)

> View the notebook:(https://github.com/artsy/minotaur/blob/master/sandbox/zack/andrew_gallery_photography.ipynb)



_[6] AB Testing Cleanup with Personalized Homepage_ - [Zack Gow](github.com/zackgow)
> - cleaned up AB testing by compartmentalizing script into functions
- cleaned up output by placing data into dataframes

> https://github.com/artsy/minotaur/pull/136


_[2] price inferencing_ - [Zack Gow](github.com/zackgow)
> Compared to original model by Will after adding these features per artist:
 - 25th%
 - 50th%
 - 75th%
 - min price_listed
 - max price_listed

> Additionally, we re-label works with a price_listed of <=100 to be NaN; as they are likely mislabeled. This model ignores ~90k works with price information for other currencies.

> Here, KNN with N=1 far outperforms GBT:

>  - MSE average artist price: 37.3197 (billion)
 - MSE KNN:                  2.0906 (billion)
 - MSE GBT:                  11.0874 (billion)

>  - MAE average artist price: 32687.2077786
 - MAE KNN:                   2660.86444149
 - MAE GBT:                   11032.2025468

>  - R2 average: -3.92560820852e-05
 - R2 KNN:     0.943977763278
 - R2 GBT:     0.702895317492

>  - median absolute error average artist price: 21298.4271189
 - median absolute error KNN:                  0.0
 - median absolute error GBT:                  1454.76250831

>  - explained_variance_score average artist price: 0.0
 - explained_variance_score KNN:                  0.944019737232
 - explained_variance score GBT:                  0.702898690591

>  - Total difference (simple average): -0.0502
 - Total difference (KNN model):      0.0520
 - Total difference (GBT model):      0.0147

> After converting all currencies to USD, and recalculating features, performance greatly drops (due to very high priced works, where both models perform poorly on here; example - there was a 100M work that was); if we remove artworks greater than 10M, 50M, etc., we see improvements across all metrics.

> In this example, we compare the training and test sets with the KNN predictions (k=5) and GBT predictions including all high priced works

> ![descriptive stats](https://dlh7x4sj1uwv2.cloudfront.net/items/2f2O1I3H193d362o2G3m/Image%202016-07-28%20at%2011.36.56%20AM.png?v=3344520f)

> https://github.com/artsy/minotaur/pull/134


_[6] Microgravity force tracks in microgravity rollups_ - [Ani Petrov](github.com/anipetrov)
> **Problem**: Some important conversions happen in borrowed force views in mG. We need to identify which these tracks are in force and bring them back to mG to roll with the mG sessions.

> **Solution**: Look at all tracks in `force_production.tracks` that are coming from a `device_type = 'Mobile'` and which come from an `anonymous_id` that we have seen in mG. In the process of figuring out how to scope the force tracks that should belong to mG, I looked at a few different breakdowns. Here is some of this work:

> Checking for the anonymous_ids that we have seen associated with a mobile browser in force but which we have _not_ seen in mG (meaning that even if we send them to mG, we would still not be able to associate them with sessions):

```sql
-- 42,935 anon_ids in force tracks coming from a supposedly mobile browser are not seen in mG
SELECT count(DISTINCT anonymous_id)
FROM force_production.tracks t
  LEFT JOIN util.browsers b ON b.user_agent = t.context_user_agent
WHERE t.event <> 'artwork_impressions'
AND   anonymous_id not IN (SELECT DISTINCT anonymous_id
                       FROM microgravity_production.pages
                       UNION
                       SELECT DISTINCT anonymous_id
                       FROM microgravity_production.tracks)
AND   device_type = 'Mobile';
```

> Checking for the anonymous_ids that we have seen associated with a mobile browser in force and which we have seen in mG:

```sql

> -- 43,367 anon_ids in force tracks coming from a supposedly mobile browser are seen in mG. looks like they are all tablets
SELECT COUNT(DISTINCT anonymous_id)
FROM force_production.tracks t
  LEFT JOIN util.browsers b ON b.user_agent = t.context_user_agent
WHERE t.event <> 'artwork_impressions'
AND   anonymous_id IN (SELECT DISTINCT anonymous_id
                       FROM microgravity_production.pages
                       UNION
                       SELECT DISTINCT anonymous_id
                       FROM microgravity_production.tracks)
AND   device_type = 'Mobile';
```
And the anonymous_ids that we have seen in both force and mG but are parsed as coming from a `device_type = 'Desktop'`, meaning tracks that we might be able to attribute to a mG session if we were not checking the device type:

```sql

> -- 1,913 anonymous_ids in force tracks coming from a desktop browser are seen in mG.
-- The number is small enough for us not to consider joining them into the microgravity_force_tracks table
SELECT COUNT(DISTINCT anonymous_id)
FROM force_production.tracks t
  LEFT JOIN util.browsers b ON b.user_agent = t.context_user_agent
WHERE t.event <> 'artwork_impressions'
AND   anonymous_id IN (SELECT DISTINCT anonymous_id
                       FROM microgravity_production.pages
                       UNION
                       SELECT DISTINCT anonymous_id
                       FROM microgravity_production.tracks)
AND   device_type = 'Desktop';
```

> Thus this PR is the first step towards proper track attribution. It does a few things:
1. Better device_type parsing
2. Create a `microgravity_force_tracks` and `microgravity_force_pages` tables for borrowed views
3. Add the new track and pages tables to the rollups

>
https://github.com/artsy/fulcrum/pull/296



_[4] Microgravity inquiry funnel_ - [Ani Petrov](github.com/anipetrov)
> https://github.com/artsy/fulcrum/pull/299

> Following up on https://github.com/artsy/fulcrum/pull/296, this PR builds microgravity inquiry funnels.

> * Build `microgravity_mapped_account_creations` based on all microgravity_production.created_account events and all `force_production.created_account` events that we have defined as belonging to microgravity. We achieve this by requiring:
```sql
WHERE created_account.id IN (SELECT DISTINCT LEFT (event_id,36)
                             FROM analytics.microgravity_force_tracks
                             WHERE event = 'created_account')
```
* Similarly, build `microgravity_mapped_inquiries` but this time only using the microgravity events in `force_production.sent_artwork_inquiry`, since that event only happens in force.

> * Build `microgravity_mapped_pages` by aliasing the union of `microgravity_production.pages` and `analytics.microgravity_force_pages`

> * Remove tracks and pages that we have defined as coming from microgravity (all tracks and pages in `microgravity_force_tracks` and `microgravity_force_pages`) from `force_tracks` and `force_pages`. Previously, we naively excluded all tracks and pages that came from `Mobile` or Eigen user agents.

> * Remove microgravity tracks according to our new definition from `force_mapped_inquiries`, `force_mapped_account_creations`.

> **TO DO**: Build the remaining funnels while making sure the force counterparts respect the new scoping conditions:

```sql
-- excluding force events that we have decided belong to microgravity
AND event.id NOT IN (SELECT DISTINCT LEFT (event_id,36)
                     FROM analytics.microgravity_force_tracks
                     WHERE event = 'event_name')
 -- excluding events that belong to Eigen
   AND   browsers.device_type NOT IN ('Eigen iPod', 'Eigen iPad', 'Eigen iPhone')
 -- excluding admin tracks
    AND   (users.is_admin IS FALSE OR u.is_admin IS NULL)
```



Shipped July 22
-----

_[8] price inferencing_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/pull/81


_Build auction_bids in fulcrum and update joins and looker tables_ - [Will Goldstein](github.com/wrgoldstein), [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/fulcrum/pull/283
https://github.com/artsy/fulcrum/pull/284
https://github.com/artsy/looker/pull/514
https://github.com/artsy/fulcrum/pull/288


_Dwell time on auctions page (in auctions traffic dashboard)_ - [Shiya Wang](github.com/shiyawang), [Will Goldstein](github.com/wrgoldstein)
> https://github.com/artsy/fulcrum/pull/289
https://github.com/artsy/looker/pull/519



_Live Auctions Dashboard_ - [Shiya Wang](github.com/shiyawang)
> [Live auctions dashboard (Philips)](https://artsy.looker.com/dashboards/artsy::live_auctions_summary?sale_slug=phillips-20th-century-and-contemporary-art-day-sale)

> https://github.com/artsy/looker/pull/505
https://github.com/artsy/looker/pull/509
https://github.com/artsy/fulcrum/pull/279
https://github.com/artsy/looker/pull/510
https://github.com/artsy/looker/pull/511
https://github.com/artsy/looker/pull/516


_Gallery Photography_ - [Zack Gow](github.com/zackgow)
> - Is there a correlation between image size (pixels) and number of inquiries (e.g. the higher the resolution, the better the inquiries)?
- Is there evidence to support the claim that shows with installation images have more pageviews or longer engagement time?
- Is there evidence to support the idea that galleries with installation images see higher click through rates than those that don't?


_Integrate causality data in looker_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/looker/pull/499
https://github.com/artsy/looker/pull/506
https://github.com/artsy/auctions/issues/91

>
Remember to check in with Alan on implementing business logic in Causality instead of Looker.


_Auctions (not live integration) summary dashboard_ - [Shiya Wang](github.com/shiyawang)
> [Heather James](https://artsy.looker.com/dashboards/artsy::non_live_auctions_summary?sale_slug=heather-james-fine-art-benefit-auction-2016) as an example.

> https://github.com/artsy/looker/pull/515


_Auctions anlaytics presentation_ - [Shiya Wang](github.com/shiyawang)

_Fairs analytics presentation_ - [Shiya Wang](github.com/shiyawang)

_[6] Web Professional Buyer Applications attribution funnel_ - 51004f1e3f7a0db31a00021b, [Ani Petrov](github.com/anipetrov), 55f264c0727ed33a7ab69fe3, 51c260740fb65f9753001561




Shipped July 15
-----

This week we spent considerable time on longer range projects, most notably QA and instrumentation of microgravity (m.artsy.net), and prepared for a board meeting.

_[2] Sessions that land on auction (in fulcrum)_ - [Shiya Wang](github.com/shiyawang)
> Session and source information for sessions that land on /auctions, auction page, and lot page. Tables built in fulcrum.

> https://github.com/artsy/fulcrum/pull/264


_[6] Auctions Traffic Dashboard_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/looker/pull/490
https://github.com/artsy/fulcrum/pull/267
https://github.com/artsy/looker/pull/496

> [Auctions traffic dashboard](https://artsy.looker.com/dashboards/analytics::auctions_traffic?sale_slug=rago-auctions-makers-collect)


_[1] LookML dashboard building for email_ - [Ani Petrov](github.com/anipetrov)

_[2] New article-related schema (force and microgravity)_ - [Ani Petrov](github.com/anipetrov)

_[4] Retention_ - [Ani Petrov](github.com/anipetrov), 55a338c6f8e5d95575eb7bf1



Shipped July 8
-----

This week we suffered and recovered from poor data pipeline health, benefited from @joeyaghion's improvements to our reporting infrastructure, started adding in data from a new system (causality), performed some minor cleanup to utility tables and attribution (medium parsing), prepared for a board meeting, contributed to (ongoing) marketing efforts to build a database of gallery contact information and a prequalification system, and worked to improve the sanity and quality of application instrumentation, especially on microgravity (m.artsy.net).

_One-offs_ -

_Fulcrum Load should respect schemas_ - 4e70b25f248564000000126c
> when new services export their data to s3, a path like `schema.tablename `should prompt fulcrum to
1. create that schema if necessary (with permissions)
2. copy data into that tablename in that schema


_[0] Update util.country_codes_ - [Shiya Wang](github.com/shiyawang)
> Change country name from China, Republic of (Taiwan) to Taiwan


_[1] Additional medium parsing clean-up_ - [Shiya Wang](github.com/shiyawang)
> Make sure that fairs are correctly categorized in force sessions and that medium parsing between force and microgravity sessions are consistent.

> https://github.com/artsy/fulcrum/pull/263


_[1] Causality data integration prep_ - [Shiya Wang](github.com/shiyawang)
> Move causality to redshift via ETL pipeline in fulcrum:

> - State (the latest state for each lot after the auction closes): lotID (unique), saleID, max bid amount, etc.

> - Events (information on bidding): type, lot ID, sale ID, payload: JSON, createdAT (only successful events, for unsuccessful events will be available in prediction).


_[2] Auctions pvs cleanup_ - [Shiya Wang](github.com/shiyawang)
> Retire the old way of counting auction pages (aka via the derived table `mobile_and_desktop_combined_pages`) and replace it with the daily roll-ups of auction pageviews (/auctions, auction page, lot page). Clean up Looker joins, explores, and dashboards.

> https://github.com/artsy/looker/pull/485


_[4] Discrepancy between GA fairs pv versus Segment fairs pv roll ups_ - [Shiya Wang](github.com/shiyawang)
> **Problem**:
GA pageviews are lower than daily pageview roll-ups from Segment.

> For example, number of pageviews to arteBA 2106 from 2016-05-05 to 2016-06-05 [is 26896 from Segment daily roll-ups](https://artsy.looker.com/x/9DgVcrw) and [is 21841 from GA](https://analytics.google.com/analytics/web/#report/content-pages/a12450662w26614972p25248350/%3F_u.date00%3D20160505%26_u.date01%3D20160605%26explorer-table.filter%3Darteba-2016%26explorer-table.plotKeys%3D%5B%5D%26explorer-table.rowCount%3D100/).

> **Solution**:
This is because GA and daily roll-ups are counting pageviews differently. GA is counting urls that strictly contain a given fair slug, whereas the daily roll-ups are counting urls (more specifically, context page paths that are stripped from the urls) that contain the fair slug, partner show slug and partner show artwork slug that belong to a given fair. In cases where a user viewed an artwork page (that belonged to a fair) without having being referred to from the fair microsite, this pageview would be counted towards the daily roll-ups from Segment, but not in GA.

> For example, on 2016-06-01, GA counts [81 pageviews](https://analytics.google.com/analytics/web/#report/content-pages/a12450662w26614972p25248350/%3F_u.date00%3D20160601%26_u.date01%3D20160601%26explorer-table.filter%3Darteba-2016%26explorer-table.plotKeys%3D%5B%5D%26explorer-table.rowCount%3D100%26explorer-table.rowStart%3D0/) to arteBA 2016 whereas the daily roll-up counts [120 pageviews](https://artsy.looker.com/x/djSjHsm). When we expose the context page path, we can see that the urls, including the artwork urls, in GA contain the fair slug "arteba-2016," whereas the context page paths in the daily roll-ups contain artworks or shows that are part of the fair without explicitly referring to the fair slug.

> The daily roll-up from Segment therefore is a more lenient and comprehensive way of counting fair pageviews, meaning it counts urls that contain shows and artwork slugs that belong to the fair regardless of how the user ended up there, as long as the page is viewed from two weeks before the fair starts and two weeks after the fair ends.

>
https://github.com/artsy/fulcrum/pull/262
https://github.com/artsy/looker/pull/487


_[2] update gallery application forecasting model_ - [Zack Gow](github.com/zackgow)

_[2] clean up ab testing / looker dashboards_ - [Zack Gow](github.com/zackgow)

_[2] GP team stats_ - [Zack Gow](github.com/zackgow)
> https://docs.google.com/spreadsheets/d/1Ch9aiUcJO5N6vLEFlIco-OA37ZKD-7Qg7q5vuIb0sZ8/edit?ts=5745f992#gid=0


_[4] Schema update: click and form flow_ - [Ani Petrov](github.com/anipetrov)



Shipped July 1
-----

_one-offs_ -

_directions for utm parameters (social, email, comms, etc)_ - [Will Goldstein](github.com/wrgoldstein)

_Take s3 errors, t.tumblr, fairs out of referral_ - [Will Goldstein](github.com/wrgoldstein)

_[2] project inbound applications for Q3_ - [Zack Gow](github.com/zackgow)

_[1] Deliverability/open rate issues with Radiation_ - [Zack Gow](github.com/zackgow)

_[1] GR KPI dashboard update_ - [Zack Gow](github.com/zackgow)

_[4] Partner Success Goal Setting/Project Impact_ - [Zack Gow](github.com/zackgow)

_[2] Upgrade public analytics screens with Looker / something better than Geckoboard_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/minotaur/issues/119


_[6] MG fair landing source (fulcrum + looker + dashboard)_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/fulcrum/pull/243
https://github.com/artsy/looker/pull/480

> How the fair_landing_sessions folder in fulcrum looks:
![image 2016-06-29 at 10 12 01 am](https://cloud.githubusercontent.com/assets/6482254/16455352/f912c8c4-3de1-11e6-9134-d45d21f43257.png)

> https://artsy.looker.com/dashboards/analytics::fairs_traffic
![screen recording 2016-06-29 at 12 43 pm](https://cloud.githubusercontent.com/assets/6482254/16462447/55ff9798-3dff-11e6-8098-9b7b4bc30307.gif)



_[4] Reorganizing the fair pageview tables_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/fulcrum/pull/242
https://github.com/artsy/looker/pull/477

> This is how the folder fair_daily_pageviews is organized:

> ![image 2016-06-28 at 1 46 13 pm](https://cloud.githubusercontent.com/assets/6482254/16426368/bfb0bb82-3d36-11e6-8177-5febbe4f3d96.png)

> Aggregate pageviews from 2 weeks before fair starts to 2 weeks after fair ends, pivot by both page and device types ([link](https://artsy.looker.com/x/m5ZvQKt)):
![image 2016-06-28 at 2 44 51 pm](https://cloud.githubusercontent.com/assets/6482254/16428229/f4987ee0-3d3e-11e6-839f-0f79432cf8f8.png)



_[4] Additional changes to the fairs dashboards_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/looker/pull/475
https://github.com/artsy/looker/pull/480

> https://artsy.looker.com/dashboards/analytics::fairs_traffic
https://artsy.looker.com/dashboards/artsy::fairs_summary
https://artsy.looker.com/dashboards/artsy::fairs_inquiries_and_sales


_[2] Artsy buyers (registered users: both logged-in and logged-out geo and device info_ - [Shiya Wang](github.com/shiyawang)
> Device type for inquiries that resulted in purchases for logged-in and logged-out users. Location information for users that are logged-in and logged-out.

> Walked through the looks in the checklist.


_[4] Reorgnize/enrich auction daily pageviews in fulcrum_ - [Shiya Wang](github.com/shiyawang)
> We used to have in fulcrum the daily roll-ups of the individual auction pages with the url `/auction/[auction_slug]`, but we don't have roll-ups for lot pages or the general auctions page: artsy.net/auctions.

> The way we've been getting lot page pvs and /auctions pvs is through filtering the `context_page_path` dimension in a derived table in Looker called `mobile_and_desktop_combined_pages`. As the name implies, eigen pageviews are missing from this table.

> This pr reorganizes the way auction pvs are counted and ensures that all auction pageviews are in one place. Now we account for these three types of auction pageviews that happen on force, mg, and eigen:

> - /auctions
- auction page: /auction/[sale_slug]
- lot page: /artwork/[sale_artwork_slug]

> Here is how the `auction_daily_pageviews` folder is organized:

> ![image 2016-06-30 at 4 23 45 pm](https://cloud.githubusercontent.com/assets/6482254/16503092/62c83184-3edf-11e6-9146-9f6d9e90e6b2.png)

> https://github.com/artsy/fulcrum/pull/248


_[2] Document purchases table quirkiness_ - [Shiya Wang](github.com/shiyawang)
> https://github.com/artsy/looker/pull/483


_[1] Auction push notification stats_ - [Shiya Wang](github.com/shiyawang)
> How many push notifications per auction, starting with Julien's for now. For Chloe & Barry.

> ![image 2016-07-01 at 12 55 02 pm](https://cloud.githubusercontent.com/assets/6482254/16528460/20fd514c-3f8b-11e6-8eb7-0023c8c8ac9f.png)

> https://artsy.looker.com/sql/gnt8bbh3fwqmmr


_[2] Personalized homepage (with 7 rails) AB test design and analysis_ - Brian Waterson, [Ani Petrov](github.com/anipetrov)

_[4] mG schema + QA + cleanup_ - [Ani Petrov](github.com/anipetrov)



Shipped June 24
-----

_[1] Conversion rate from sessions that viewed an artist page to inquiring_ - [Zack Gow](github.com/zackgow)
> https://github.com/artsy/gravity/issues/10158

_[1] Partner Success Goal Setting/Project Impact_ - [Zack Gow](github.com/zackgow)

_[3] Professional buyer funnels_ - [Ani Petrov](github.com/anipetrov)

_[1] mG borrowed cookie id_ - [Ani Petrov](github.com/anipetrov)

_[2] Fair team presentation_ - [Ani Petrov](github.com/anipetrov)

_[2] Inquiries by campaign source_ - [Shiya Wang](github.com/shiyawang)
> Get campaign source and session information for inquiries placed on force.

> https://github.com/artsy/fulcrum/pull/237
https://github.com/artsy/looker/pull/471

_[4] Fairs dashboard second pass_ - [Shiya Wang](github.com/shiyawang)
> See [this doc](https://docs.google.com/a/artsymail.com/document/d/1tmevcbhNMNtS2O6-hfI36BTqVuwGGB5-tjNrsuxnJEA/edit?usp=sharing) for all follow-up questions on the summary dashboard, fairs inquiries & sales dashboard, and fairs traffic dashboard.

> https://github.com/artsy/fulcrum/pull/236
https://github.com/artsy/looker/pull/470

_[4] Logged-out users vs. anon inquirers in purchases_ - [Shiya Wang](github.com/shiyawang)
> The goal is to identify and distinguish logged-out registered users from anon cookies in the purchases explore. Each purchase ID has an email dimension and a user id dimension. However, not every purchase object has both dimensions. This [doc](https://docs.google.com/a/artsymail.com/document/d/1zaHBmK-dP8dGXUF04brdUntgITDUWUu0qLznzwMbJ3g/edit?usp=sharing) walks through all the possible scenarios and is used to infer how to identify and distinguish logged-out registered users.

> https://goo.gl/upr0UX
https://github.com/artsy/looker/pull/467
https://github.com/artsy/looker/pull/468


_[3] Enrich Sailthru Funnel by Blast ID_ - [Ani Petrov](github.com/anipetrov)

Shipped June 17
-----
_[1] Learning team requests adding fields to Genes table_ - [Madeleine Boucher](https://trello.com/madeleineboucher), [Shiya Wang](github.com/shiyawang), [Will Goldstein](github.com/wrgoldstein)
> **Context**:
Request from Learning team: add `gene_type`, `gene_family`, and `has_description` to the genes table.

> **PRs**:
https://github.com/artsy/gravity/pull/10113
https://github.com/artsy/looker/pull/449


_[4] Fairs summary dashboard_ - [Shiya Wang](github.com/shiyawang)
> Build a Looker dashboard to display an aggregate view, with ability to filter information by date, of the following metrics. This information can be found on columns G-N of the [spreadsheet](https://docs.google.com/spreadsheets/d/1a_IHID3wkj5KuewCVjR8tC6Yml4mqZZSfw2alx61wkY/edit#gid=2088975450) and the aggregate view is on line 3.

> https://github.com/artsy/looker/pull/453
https://artsy.looker.com/dashboards/artsy::fairs_summary



_[4] Fair inquiries/sales dashboard_ - [Shiya Wang](github.com/shiyawang)
> Build a Looker dashboard showing number of inquiries and sales for art fairs (aggregate view, filtered by date) in comparison to the rest of inventory available on Artsy. Reiterate on this [dashboard](https://artsy.looker.com/dashboards/68).

> https://github.com/artsy/looker/pull/455
https://artsy.looker.com/dashboards/artsy::fairs_inquiries_and_sales


_[3] Source/session info for fair traffic_ - [Shiya Wang](github.com/shiyawang)
> Session and source information for fairs, specifically, sessions that land on fair microsite, partner show pages, and partner show artwork pages. Build tables in fulcrum.

> https://github.com/artsy/fulcrum/pull/224


_[4] Fair traffic and source (force) dashboard_ - [Shiya Wang](github.com/shiyawang)
> Dashboard displaying an aggregate view across different fairs over extended periods of time, with breakdown of traffic by country and source. As we monetize fairs we have partners requesting more analytics info and we also want to compare the traffic we generate on our own (SEO, social media, emails, etc.) vs. traffic generated by fairs via banners on their website and email campaigns.

> https://github.com/artsy/looker/pull/457
https://artsy.looker.com/dashboards/artsy::fairs_traffic



_[3] We are experiencing a ~40% boost in conversion from inquiry to sale from last month. Did the QFU had an impact in moving the conversation forward?_ - [Zack Gow](github.com/zackgow)

_[3] Partner Success Roadmapping_ - [Zack Gow](github.com/zackgow)

_[2] Close out artwork ab test_ - [Ani Petrov](github.com/anipetrov), [Zack Gow](github.com/zackgow)

_[1] Inquiries per partner per liaison_ - [Ani Petrov](github.com/anipetrov)

_[4] Inquiry forced login numbers_ - [Ani Petrov](github.com/anipetrov)

_[1] Milestones diary in minotaur_ - [Ani Petrov](github.com/anipetrov)

_[2] Artworks that do not see much traffic_ - [Ani Petrov](github.com/anipetrov)

_[1] Dig into personalized email source attribution_ - [Ani Petrov](github.com/anipetrov)

_[4] Inquirer retention followups_ - [Ani Petrov](github.com/anipetrov)
> update ipython notebook;
how is this influenced by whether or not the gallery responds, etc?


_One-offs_ -


Shipped June 10
-----
_[4] Fair microsite daily pageview rollup_ - 54c2936a8ab794081fb926f9, [Shiya Wang](github.com/shiyawang)
> **Context**:
Daily rollup of these three kinds of pageviews for fair microsites: landing page pageviews, partner show pageviews, and partner show artwork pageviews. Breakdown by device type.

> **PRs**:
https://github.com/artsy/fulcrum/pull/216



_[8] Follow-up questions on anon inquirers_ - [Shiya Wang](github.com/shiyawang)
> **Context**:
Part of the larger effort to rethink the inquiry flow and account creation. Questions such as comparing their gallery response and 3-way handshake rates with logged-in users, why is it not the same as the conversion rate in mixpanel, signed in first time buyers, etc.

> **PRs**:
https://github.com/artsy/minotaur/pull/72
https://github.com/artsy/minotaur/pull/73
https://github.com/artsy/minotaur/pull/75



_[2] Genomer pay restructure 2.0_ - [Shiya Wang](github.com/shiyawang)
> **Context**:
Maintain the same pay with the padded bonus, but changing the artist to artwork ratio from 7:93 to 20:80. Update the required number of genomes for each pay tier.

> **See [spreadsheet](https://docs.google.com/a/artsymail.com/spreadsheets/d/183E6Hm9l8fWsRTTkkU-zruKvo5ZIAGs4Ni1zo29kHVM/edit?usp=sharing)**


_[4] Live auction analytics first pass_ - [Shiya Wang](github.com/shiyawang)
> For the upcoming auctions, get raw data from causality and analyze. If time permitting, getting lot detail analytics in by this quarter but not urgent.



_[2] Competitive Landscape support_ - [Shiya Wang](github.com/shiyawang)
> **Context**:
dblock: "I’d love some help with https://trello.com/b/cnXbb22V/competitive-landscape on the Data side. Ultimately I’d like that board to have the completely current list of data startups that relate to art and a presentation that goes over the list to a group of maybe 5-10 people. Maybe you can volunteer someone from your team?"


_[4] Inquirer retention: what % of users who inquire come back and inquire again?_ - [Ani Petrov](github.com/anipetrov)

_Listings meeting analytics presentation_ - [Will Goldstein](github.com/wrgoldstein)

_[2] Learning Team needs a new sessions dashboard_ - [Zack Gow](github.com/zackgow)
> Their old one used the looker-based session rollups (that are now deleted):

> https://artsy.looker.com/spaces/181

- Desktop and mobile monthly search sessions to gene pages

- Desktop and mobile monthly sessions to -the-art-genome-project pages by medium

> - Desktop and mobile monthly sessions to gene pages by medium

- Desktop and mobile monthly sessions to tag pages by medium

- Mobile and Desktop Total Gene Pageviews


_[2] Get museum data from LoC LCNA, or from DBPEDIA_ - [Madeleine Boucher](https://trello.com/madeleineboucher), [Zack Gow](github.com/zackgow)
> **Two possible approaches:**
1. Download Library of Congress Name Authority File database, query it locally to get museum/gallery names (CorporateEntities) and all their associated data, put it in a CSV.
2. Go through dbpedia, use their SPARQL endpoint to gather all this same information ([example query](http://stackoverflow.com/questions/17174439/dbpedia-sparql-query-returns-multiple-and-duplicate-records))

> **Goal**
Get a list of museum names, alternate names, and locations in order to populate a controlled list for entering artist exhibition histories.


_[4] Artwork page AB test report_ - [Zack Gow](github.com/zackgow), [Ani Petrov](github.com/anipetrov)
> Discuss

> - best practices, what to report, what success looks like

> at blab


_[4] Single source of truth for session numbers: GA - inhouse numbers discrepancies_ - [Ani Petrov](github.com/anipetrov)
> do not exclude admin sessions from rollups, just mark them as such


_[4] Q3 prioritization for GMV 2.0_ - [Ani Petrov](github.com/anipetrov)

_[2] Liaisons FAQ_ - 51c23fcd23b744af0f00635a, [Ani Petrov](github.com/anipetrov)

_[1] Forced login if we detect your email has an account_ - [Ani Petrov](github.com/anipetrov)

_Device type for purchases (attribute GMV to mobile)_ -



Shipped June 3
-----
~~~~ note this has been automated, hence the different format ~~~~~

_One-offs_ -

_[6] User retention (force account creation)_ - [Ani Petrov](github.com/anipetrov)
> Typical inquiry request rate, follow rate, etc by cohort (week?)

> Wants to measure impact of recent changes to daily emails (dumping everyone in it as of april 17 ish)


_[2] Professional buyers program page schema_ - [Ani Petrov](github.com/anipetrov)

_Artist page schema_ - [Ani Petrov](github.com/anipetrov)

_GMV: Q3 prioritization questions I_ - [Ani Petrov](github.com/anipetrov)

_Queries for gallery partnerships_ - [Shiya Wang](github.com/shiyawang)
> **Context**:
Need to pull quickly the artist demand metrics for artists in one or more galleries, as well as the top performing artists site-wide by a given metric (for example, the number of acb's)

> **PRs**:
https://github.com/artsy/minotaur/pull/69
https://github.com/artsy/minotaur/pull/71


_Fairs participation rate discrepency_ - [Shiya Wang](github.com/shiyawang)
> Reconcile discrepancy between the fair metrics dashboard and the fair participation rate table




##### 2016-05-27

Short week:  Zack and Shiya were both out, and Ani and I had a lot of investor work.  We shipped a fix to our pagetypes index and created a partner categories report in gravity, as well as pulled some demographic data for Melanie and investigated why GA and Looker had different numbers for pageviews (turns out MicroG double reports some pageviews).  The bulk of the work was in looking at Probable Sales, an attempt to understand what level of GMV flows through Artsy that isn't reported or recorded.  Our validations here ended without much success, as expected.

##### 2016-05-20

- Created a scalable way to get artist demand reports - [Shiya](github.com/shiyawang)
- Major institutional artist pageview analysis - [Shiya](github.com/shiyawang)
  * [pr](https://github.com/artsy/minotaur/pull/62)
- Anonymous inquirers analysis - [Shiya](github.com/shiyawang)
  * [pr](https://github.com/artsy/minotaur/pull/63)
- Purchases breakdowns for collector experience - [Will](github.com/wrgoldstein)
  * https://artsy.looker.com/x/78H7P9p
  * https://artsy.looker.com/x/g4Gvp42
- Quick Follow Up analysis - [Zack](github.com/zackgow)
- Removed mobile pageviews from force rollups - [Ani](github.com/anipetrov)
- Follow Modal and Personalized Email performance analysis - [Ani](github.com/anipetrov)
- First pass at new AB Testing framework - [Zack](github.com/zackgow) and [Ani](github.com/anipetrov)
  * [link](https://github.com/artsy/minotaur/pull/59)

##### 2016-05-13

This was a short week with investor asks and goal setting.

- [Shiya](github.com/shiyawang) worked on an auctions business retrospective ([looker dash](https://artsy.looker.com/dashboards/121)) and shipped some session funnel updates ([link to pr](https://github.com/artsy/fulcrum/pull/186)).

- [Ani](github.com/anipetrov) completed an investigation into potential GMV from purchases not recorded ([link](https://gist.github.com/wrgoldstein/0e19db5b8ab6cdfa1c12f641d350b1c7)) and some volt Looker updates ([link to pr](https://github.com/artsy/looker/pull/410)).

- [Zack](github.com/zackgow) continued work on partner success goal setting and an a/b test framework built on redshift.

##### 2016-05-06

- Session roll-ups for Volt - [ani](github.com/anipetrov)
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/175)
- Visitor roll-ups for Force - [ani](github.com/anipetrov)
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/164)
- iOS Artist page analytics schema - [ani](github.com/anipetrov)
  * [eigen issue](https://github.com/artsy/eigen/issues/1469)
- Auctions Q1 Retrospective - [shiya](github.com/shiyawang)
  * [looker dashboard](https://artsy.looker.com/dashboards/109)
- ARS renegotiations support - [shiya](github.com/shiyawang)
  * [google sheet](https://docs.google.com/spreadsheets/d/1eHOqcTf32dgZJkElX_HzDz3wuQjv0ETicsWS0yMWgW0/edit#gid=1923954852)
- Major sessions cleanup in Looker - [shiya](github.com/shiyawang)
  * Looker:
    - https://github.com/artsy/looker/pull/400
    - https://github.com/artsy/looker/pull/402
    - https://github.com/artsy/looker/pull/403
    - https://github.com/artsy/looker/pull/407
  * Fulcrum:
    - https://github.com/artsy/fulcrum/pull/172
    - https://github.com/artsy/fulcrum/pull/174
    - https://github.com/artsy/fulcrum/pull/178
  * Minotaur:
    - https://github.com/artsy/minotaur/pull/50
- Artwork page ab test setup - [ani](github.com/anipetrov)
- Auctions funnel enrichment - [shiya](github.com/shiyawang)
  * [fulcrum PR 1](https://github.com/artsy/fulcrum/pull/167)
  * [fulcrum PR 2](https://github.com/artsy/fulcrum/pull/169)


##### 2016-04-27

- Gallery Applications funnel (force only) finalized in Looker ([anipetrov](https://github.com/anipetrov))
  * [looker PR](https://github.com/artsy/looker/pull/384)
- Similar funnel for auctions related activity ([shiyawang](https://github.com/shiyawang))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/162)
  * [looker PR](https://github.com/artsy/looker/pull/390)
- Similar funnel for inquiries by source ([anipetrov](https://github.com/anipetrov) and [shiyawang](https://github.com/shiyawang))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/159)
  * [looker PR](https://github.com/artsy/looker/pull/386)
- First pass at user-engagement lifecycle analysis ([shiyawang](https://github.com/shiyawang))
  * [minotaur PR](https://github.com/artsy/minotaur/pull/46)
- User level rollup of activity (force only) with multichannel attribution ([anipetrov](https://github.com/anipetrov))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/164)
- iOS signup analytics schema ([anipetrov](https://github.com/anipetrov))
  * [eigen issue](https://github.com/artsy/eigen/issues/1459)
- better device type parsing for mail clients ([shiyawang](https://github.com/shiyawang))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/160)
- Q1 retrospective for auctions business ([shiyawang](https://github.com/shiyawang))
  * [gist](https://gist.github.com/shiyawang/8e42c6f3e3a837d834ddc6501f4dfb61)
  * [looker dashboard](https://artsy.looker.com/dashboards/109)
- Radiation conversations logic moved to fulcrum ([anipetrov](https://github.com/anipetrov))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/157)
- Queries for auctions source attribution ([shiyawang](https://github.com/shiyawang))
  * [minotaur PR](https://github.com/artsy/minotaur/pull/47)
- Removed admins from all rollups ([anipetrov](https://github.com/anipetrov))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/161)
- Sailthru data in Looker ([sperle](https://github.com/sperle) and [wrgoldstein](https://github.com/wrgoldstein))
  * [fulcrum PR](https://github.com/artsy/fulcrum/pull/163)
  * [looker PR](https://github.com/artsy/looker/pull/389)
- Usual one-offs


##### 2016-04-22

- Goal setting
- AB Test: Contact Gallery ([link](https://github.com/artsy/minotaur/blob/master/ab-test-force/20160330_contact_gallery_link.md)) - [shiya](github.com/shiyawang)
- Documentation for borrowed views in front end instrumentation ([link](https://github.com/artsy/minotaur/blob/master/doc/front_end_analytics/borrowed_view.md)) - [ani](github.com/anipetrov)
- Session roll-ups for MicroG ([link](https://github.com/artsy/fulcrum/pull/149)) - [ani](github.com/anipetrov)
- GI newsletter analysis ([link](https://github.com/artsy/minotaur/pull/34)) - [shiya](github.com/shiyawang)


##### 2016-04-15

(Goal setting, skeleton crew)

##### 2016-04-8

- Cleared charges look for billing ([link](https://artsy.looker.com/explore/artsy/failed_charges?dynamic_fields=%5B%5D&f%5Bfailed_charges.billed_date%5D=after%200%20months%20ago&f%5Bfailed_charges.cleared_failed_charge%5D=Yes&f%5Bfailed_charges.plan%5D=Standard,Preferred,Premium&filter_config=%7B%22failed_charges.billed_date%22:%5B%7B%22type%22:%22after%22,%22values%22:%5B%7B%22date%22:%222016-04-05T21:19:25.076Z%22,%22unit%22:%22mo%22,%22tz%22:true,%22constant%22:%220%22%7D,%7B%22date%22:%222016-04-05T21:19:25.076Z%22,%22unit%22:%22day%22,%22tz%22:true%7D%5D,%22variant%22:%22relative%22,%22id%22:0%7D%5D,%22failed_charges.cleared_failed_charge%22:%5B%7B%22type%22:%22is%22,%22values%22:%5B%7B%22constant%22:%22Yes%22%7D,%7B%7D%5D,%22id%22:2%7D%5D,%22failed_charges.plan%22:%5B%7B%22type%22:%22%3D%22,%22values%22:%5B%7B%22constant%22:%22Standard,Preferred,Premium%22%7D,%7B%7D%5D,%22id%22:1%7D%5D%7D&look_id=1879&query=Htj7htD&show=data&title=cleared%20charges&vis=%7B%7D)) - [zack](github.com/zackgow)
- Added fair pages to `util.referrers` ([pr](https://github.com/artsy/fulcrum/pull/145)) - [zack](github.com/zackgow)
- First pass at Gallery Applications by source funnel - [will](github.com/wrgoldstein), [ani](github.com/anipetrov)
  * ([spreadsheet](https://docs.google.com/spreadsheets/d/1i9EyybWack_83Hj19qYHLj__-nOPjOV4uMF8Isza5oU/edit#gid=0))
  * ([gist](https://gist.github.com/wrgoldstein/9748b85c856a1aa5fc1f725ac1fa2697))

##### 2016-03-28

- Auctions pageview rollups allow more efficient querying - [shiya](github.com/shiyawang)
  * https://github.com/artsy/fulcrum/pull/144#issue-144030576
- AB Test: Artwork page masonry sort order - [shiya](github.com/shiyawang)
- Much additional documentation


##### 2016-03-21

- Minor fix to sessions rollup - [@anipetrov](github.com/anipetrov)
  * https://github.com/artsy/fulcrum/pull/143
- Force instrumentation session with @craigspaeth!
   - Added homepage banner instrumentation - [@zackgow](github.com/zackgow)
     * https://github.com/artsy/force/pull/4642
- New Redshift table `util.browsers` for mapping user_agent strings to browser info - [@wrgoldstein](github.com/wrgoldstein)
  * https://github.com/artsy/fulcrum/pull/140
- Investigated Force issue where `user_id` isn't passed to `page` events [@wrgoldstein](github.com/wrgoldstein)
  * https://github.com/artsy/force/issues/4580
- Moved "atomic", a rough ab test analysis notebook, into minotaur - [@wrgoldstein](github.com/wrgoldstein)
  * https://github.com/artsy/minotaur/pull/19
- Investigated discrepancies with "Follow Artist" event in Force - [@shiyawang](github.com/shiyawang)
  * https://github.com/artsy/force/issues/4626
- AB Test: Personalized Email - [@shiyawang](github.com/shiyawang)
  * https://github.com/artsy/minotaur/pull/23
- Define Artist performance - [@shiyawang](github.com/shiyawang)
  * https://github.com/artsy/minotaur/pull/25

##### 2016-03-14

- Sessions rollup for Force - [@anipetrov](github.com/anipetrov)
  - and auctions flow
- Auctions front end events QA - [@anipetrov](github.com/anipetrov)
- Vacuuming redshift nightly - [@wrgoldstein](github.com/wrgoldstein)
  * https://github.com/artsy/fulcrum/pull/141
- Analytics minimum launchable product checklist - [@wrgoldstein], [@anipetrov](github.com/anipetrov)(github.com/wrgoldstein)
  * https://github.com/artsy/minotaur/pull/13
- Gallery insights Fairs edition [@shiyawang](github.com/shiyawang)
  * https://www.artsy.net/article/elena-soboleva-art-fair-insights-for-galleries-part-i)
  * Including metadata migration of 700+ artists into Redshift
- AB Test: Commercial Filtering - [@shiyawang](github.com/shiyawang)
  * https://github.com/artsy/minotaur/pull/23
