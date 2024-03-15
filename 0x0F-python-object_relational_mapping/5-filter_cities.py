#!/usr/bin/python3
"""
This script retrieves and displays cities for a given state from the hbtn_0e_4_usa database,
using a JOIN operation and parameterized query to prevent SQL injection.

Arguments:
    mysql_username: Username for MySQL access.
    mysql_password: Password for MySQL access.
    db_name: Name of the database to connect to (hbtn_0e_4_usa).
    state_name: The name of the state to filter cities for.
"""

import MySQLdb


def main():
    """
    Connects to the database, executes the query, and displays results.
    """

    username, password, db_name, state_name = get_arguments()
    try:
        connection = connect_to_database(username, password, db_name)
        cursor = connection.cursor()

        # Construct a parameterized query with JOIN and sort
        query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        cursor.execute(query, (state_name,))  # Use tuple for single parameter

        results = cursor.fetchall()

        # Formatted output as a comma-separated list
        cities = ", ".join(city[0] for city in results)
        print(cities)

    except MySQLdb.Error as err:
        print("Error:", err)

    finally:
        if connection:
            connection.close()


def get_arguments():
    """
    Retrieves username, password, database name, and state name from arguments.
    """

    import sys
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]


def connect_to_database(username, password, db_name):
    """
    Establishes a connection to the MySQL database.
    """

    try:
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        return connection
    except MySQLdb.Error as err:
        print("Error connecting to database:", err)
        exit(1)


if __name__ == "__main__":
    main()
