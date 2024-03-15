#!/usr/bin/python3
"""
This script retrieves and displays states with names starting with 'N' from the hbtn_0e_0_usa database.

Arguments:
    mysql_username: Username for MySQL access.
    mysql_password: Password for MySQL access.
    db_name: Name of the database to connect to (hbtn_0e_0_usa).
"""

import MySQLdb


def main():
    """
    Connects to the database, executes the query, and displays results.
    """

    username, password, db_name = get_arguments()
    connection = connect_to_database(username, password, db_name)
    cursor = connection.cursor()

    # Query to filter states with names starting with 'N'
    query = """
    SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY states.id ASC
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()

    # ... (Remaining functions are identical to the previous script)
