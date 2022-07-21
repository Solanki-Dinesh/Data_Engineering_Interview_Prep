# Newsapi.org
# REST APIs : REpresentational State Transfer API
# API : Application Programming Interface
import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import json


# Space news link
# response = requests.get(url)
#
# content = response.json()

# print and check
# print(type(content))
# print(content)

# print(content["articles"][0])
# print(content["articles"][0].keys())
#
# print(content["articles"][0]['publishedAt'])
# print(content["articles"][0]['title'])
# print("\n")
# print(content["articles"][0]['description'])

# store content in a variable and print
# articles = content["articles"]
# print(type(articles))
#
# for article in articles:
#     print('Title\n', article['title'],
#           '\nDescription\n', article['description'])

def get_news(topic, from_date, to_date, language="en",
             api_key=""):

    url = f'https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'

    response = requests.get(url)
    # print(response)
    content = response.json()

    # print(content)

    # store articles content in a list and return
    articles = content["articles"]
    results = []
    for article in articles:
        results.append({"Title": article['title'], "Author": article['author'], "PublishedDate": article['publishedAt'], "Description": article['description'], })

    return results


def news2db(url_details, dbcreds, table):

    topic = url_details["topic"]
    from_date = url_details["from_date"]
    to_date = url_details["to_date"]
    language = url_details["language"]
    api_key = url_details["api_key"]
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'

    response = requests.get(url)
    # print(response)
    content = response.json()

    articles = content["articles"]
    results = []
    for article in articles:
        results.append({"Title": article['title'], "Author": article['author'], "PublishedDate": article['publishedAt'], "Description": article['description'], })

    # create pandas dataframe
    news_df = pd.DataFrame(results)
    print(type(news_df))
    print(news_df.head())

    # Create a connection object
    engine = connection(dbcreds)

    # create and insert into table
    insert_table(engine, news_df, table)
    print("Table \"{}\" was created".format(table))

    # Print rows count
    records = num_records(engine, table)
    print("{} records imported".format(records))


# Define function to establish connection using SQLAlchemy
def connection(dbcreds):

    connect_string = "mysql+pymysql://%s:%s@%s/%s" % (dbcreds['user'], dbcreds['password'],
                                    dbcreds['host'], dbcreds['database'])

    try:
        print('Connecting to the MySQL...........')
        engine = create_engine(connect_string)
        print("Connection successfully..................")
    except SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)
        # set the connection to 'None' in case of error
        engine = None
    return engine


def insert_table(engine, datafrm, table):
        datafrm.to_sql(table, con=engine, index=False, if_exists='append', chunksize=1000)


# returns number of records from the database table
def num_records(engine, table):

    """Return number of records"""

    count = engine.execute('select count(*) from {}'.format(table)).scalar()

    return count


if __name__ == "__main__":

    url_details = {"topic": "stock", "from_date": "2022-6-21", "to_date": "2022-6-22", "language": "en", "api_key": ""}
    dbcreds = {"host": "localhost", "user": "root", "password": "", "database": "news"}
    table = "news_v1"

    print(get_news("stock", "2022-6-21", "2022-6-22", language="en", api_key="17aed235c475429ab6ded45298b2097c"))
    # news2db(url_details, dbcreds, table)
