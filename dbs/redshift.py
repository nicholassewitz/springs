import yaml
import pandas as pd
import numpy as np
import psycopg2
import os


def connect():
    global cur, conn
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'etc/redshift.yml'), 'r') as f:
        config = yaml.load(f)
    params = "dbname={dbname} user={user} host={host} port={port} password={password}".format(**config)
    conn = psycopg2.connect(params)
    cur = conn.cursor()


def execute(q):
    try:
        cur.execute(q)
    except (NameError, psycopg2.InternalError, psycopg2.OperationalError):
        try:
            conn.rollback()
        except:
            connect()
        cur.execute(q)
    out = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    if cur.rowcount == 0:
    	return pd.DataFrame()
    return pd.DataFrame(out, columns=colnames)


def reset(q):
    global conn
    conn.reset()


def close():
    conn.close()
