import pandas as pd
import datetime as dt
from pandas_datareader import data
import mplfinance as mpf
import torch
from torchvision.datasets import ImageFolder
from torchvision import models, transforms
import torch.nn as nn
import numpy as np
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def select_forex_by_name(db: Session,table_name:str):
    return get_class_by_table(Base,Base.metadata.tables.get(table_name))

def get_time_series(db: Session,table_name:str):
    df = select_forex_by_name( db=db, table_name=table_name)
    q = db.query(df).distinct(df.id).order_by(df.id).all()
    return [str(r.id).replace("-",".") for r in q]

def initialize():
    df1 = pd.read_csv(r'C://Users//User//Desktop//EURUSD.oj5k5.csv', sep=",",names=('date', 'time', 'open', 'high', 'low', 'close', 'volume'))
    df1.index = pd.to_datetime(df1['date']+" "+df1['time'])
    df1 = df1.drop(['date', 'time'], axis=1)

    df2 = pd.read_csv(r'C://Users//User//Desktop//EURUSD.oj5k30.csv', sep=",",names=('date', 'time', 'open', 'high', 'low', 'close', 'volume'))
    df2.index = pd.to_datetime(df2['date']+" "+df2['time'])
    df2 = df2.drop(['date', 'time'], axis=1)

    df3 = pd.read_csv(r'C://Users//User//Desktop//EURUSD.oj5k240.csv', sep=",",names=('date', 'time', 'open', 'high', 'low', 'close', 'volume'))
    df3.index = pd.to_datetime(df3['date']+" "+df3['time'])
    df3 = df3.drop(['date', 'time'], axis=1)

    TableM1= scheme +".forex2_m5"
    TableM5= scheme +".forex2_m30"
    TableM15= scheme +".forex2_m240"

    df1.to_sql("forex2_m5", con=engine, index=True, index_label='id', if_exists='replace',schema=scheme)
    df2.to_sql("forex2_m30", con=engine, index=True, index_label='id', if_exists='replace',schema=scheme)
    df3.to_sql("forex2_m240", con=engine, index=True, index_label='id', if_exists='replace',schema=scheme)