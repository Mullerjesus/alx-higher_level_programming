#!/usr/bin/python3
"""
This script retrieves and displays all cities from the hbtn_0e_4_usa database,
using a JOIN operation to combine data from states and cities tables.

Arguments:
    mysql_username: Username for MySQL access.
    mysql_password: Password for MySQL access.
    db_name: Name of the database to connect to (hbtn_0e_4_usa).
"""

import MySQLdb


def main():
    """
    Connects to the database, executes the query, and displays results.
    """

    username, password, db_name = get_arguments()
    connection = connect_to_database(username, password, db_name)
    cursor = connection.cursor()

    # Single query using JOIN to fetch city data and state name
    query = """
    SELECT cities.id, cities.name, states.name AS state_name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()


def get_arguments():
    """
    Retrieves username, password, and database name from arguments.
    """

    import sys
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    return sys.argv[1], sys.argv[2], sys.argv[3]


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
