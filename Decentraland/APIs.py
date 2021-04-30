import requests
import json
from gql import gql, Client
import pandas as pd
import time
from datetime import date, datetime, timedelta
import urllib.request
import json

from gql.transport.requests import RequestsHTTPTransport
# Select your transport with a defined url endpoint
transport = RequestsHTTPTransport(url="https://api.thegraph.com/subgraphs/name/decentraland/marketplace")
# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

mystring2 = """
{{
  orders (first: 100 orderBy: updatedAt, orderDirection: desc where: {{ status:sold category:parcel updatedAt_gt:"{0}"}}) {{


    category
    price

    status
    updatedAt


  }}

}}"""

def Dailyparcel():
    df = pd.DataFrame()

    #update parameter used in mystring to start querying the database at the earliest update date of sale. The update
    #date is specified in epoch date and needs to be converted to datetime for human consumption.
    update = 1

    while True:

        #query the data using GraphQL python library.
        query = gql(mystring2.format(update))
        result = client.execute(query)

        #if there is no data returned it means you reached the end and should stop querying.
        if len(client.execute(query)['orders']) <= 1:
            break

        else:
            #Create a temporary dataframe to later append to the final dataframe that compiles all 1000-row dataframes.
            df1 = pd.DataFrame()
            df1 = pd.DataFrame(result['orders'])
            #unfold a subdict into a series of columns.


            #append your temp dataframe to your master dataset.
            df = df.append(df1)

            #Pass into the API the max date from your dataset to fetch the next 1000 records.
            update = df['updatedAt'].max()

    #reformat the update date in human-readable datetime format.
    df['updatedAt_dt'] = df['updatedAt'].apply(lambda x: time.strftime('%Y-%m-%d', time.localtime(int(x))) )

    df['updatedAt_dt']=pd.to_datetime(df['updatedAt_dt'])
    df['price']=df['price'].astype(float)
    df['price']=df['price']/1000000000000000000
    date_price=df.groupby('updatedAt_dt').mean().round()

    result=date_price.loc[str(datetime.today().strftime("%Y%m%d"))]
    return result

def Historydetail(Wdate):
    pd.read_csv('parcel_trend.csv')

    a=pd.read_csv('parcel_trend.csv')

    a.set_index('Date',inplace = True)

    a=a.round()

    result=a.loc[Wdate]
    return result

def Dailymanawon():
    url='https://api.coingecko.com/api/v3/coins/decentraland'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)
    result=response_body.decode('utf-8')

    result=json.loads(result)

    return result["market_data"]['current_price']['krw']


