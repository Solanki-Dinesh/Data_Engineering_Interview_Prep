# Get weather data using openweather api key
import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def get_weather(city, units="metrics",
             api_key=""):

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'

    response = requests.get(url)
    content = response.json()
    # print(content)

    lists = content["list"]
    results = []
    for dicts in lists:
        results.append({"City": city, "Date": dicts['dt_txt'], "Temp": dicts['main']['temp'], "Condition": dicts['weather'][0]['description']})

    return results


def weather2db(url_details, dbcreds, table):

    city = url_details["city"]
    units=url_details["units"]
    api_key = url_details["api_key"]
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'

    response = requests.get(url)
    content = response.json()
    # print(content)

    lists = content["list"]
    results = []
    for dicts in lists:
        results.append({"City": city, "Date": dicts['dt_txt'], "Temp": dicts['main']['temp'], "Condition": dicts['weather'][0]['description']})


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

    url_details = {"city": "San Diego", "units": "metrics", "api_key": ""}
    dbcreds = {"host": "localhost", "user": "root", "password": "", "database": "weather"}
    table = "weather_v1"

    # print(get_weather("San Diego"))
    weather2db(url_details, dbcreds, table)
