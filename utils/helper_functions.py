import sqlite3
import pandas as pd
from typing import List, Tuple


def connect_to_database(database: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Connect to a SQLite Database

    Parameters:
    - database (str): The path to the SQLite database.

    Returns:
    Tuple[sqlite3.Connection, sqlite3.Cursor]: A tuple containing the SQLite connection and cursor.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return conn, cursor


def get_primary_keys(table_name: str, database: str = "./data/mental_health.sqlite") -> List[str]:
    """
    Get the Primary Keys for a table in a SQLite database

    Parameters:
    - table_name (str): The name of the table.
    - database (str, optional): The path to the SQLite database. Default is "mental_health.sqlite".

    Returns:
    List[str]: A list of primary key column names.
    """
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        primary_keys = [column[1] for column in columns if column[5] == 1]
    return primary_keys


def get_foreign_keys(table_name: str, database: str = "./data/mental_health.sqlite") -> List[Tuple]:
    """
    Get the Foreign Keys for a table in a SQLite database

    Parameters:
    - table_name (str): The name of the table.
    - database (str, optional): The path to the SQLite database. Default is "mental_health.sqlite".

    Returns:
    List[Tuple]: A list of foreign key information as tuples.
    """
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA foreign_key_list({table_name})")
        foreign_keys = cursor.fetchall()
    return foreign_keys


def query_to_df(query: str, database: str = "./data/mental_health.sqlite") -> pd.DataFrame:
    """
    Read a table from the database and return a Pandas DataFrame

    Parameters:
    - query (str): The SQL query to execute.
    - database (str, optional): The path to the SQLite database. Default is "mental_health.sqlite".

    Returns:
    pd.DataFrame: A Pandas DataFrame containing the query result.
    """
    with sqlite3.connect(database) as conn:
        return pd.read_sql_query(query, conn)


def close_connection(conn: sqlite3.Connection) -> None:
    """
    Close the connection to a SQLite database

    Parameters:
    - conn (sqlite3.Connection): The SQLite database connection to be closed.
    """
    conn.close()
