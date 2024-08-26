import pandas

print("pandas successfully imported")
import psycopg2

print("psycopg2 successfully imported")


def handler(event, context):
    """Function that checks whether psycopg2  and pandas are successfully imported or not"""
    return {"Status": "psycopg2 and pandas successfully imported"}
