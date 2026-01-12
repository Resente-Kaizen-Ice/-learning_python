import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="fast_api_test"
    )
