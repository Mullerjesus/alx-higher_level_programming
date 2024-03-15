#!/usr/bin/python3
"""
This script retrieves and displays state data from the hbtn_0e_0_usa database,
using a parameterized query for secure input handling.

Arguments:
    mysql_username: Username for MySQL access.
    mysql_password: Password for MySQL access (**should not be entered on the command line!**).
    db_name: Name of the database to connect to (hbtn_0e_0_usa).
    state_name: The state name to search for.
"""

import MySQLdb


def main():
    """
    Connects to the database, executes the query securely, and displays results.
    """

    username, _, db_name, state_name = get_arguments()
    connection = connect_to_database(username, db_name)  # Avoid exposing password on command line
    cursor = connection.cursor()

    # Safely create the query using a placeholder for state_name
    query = """
    SELECT * FROM states
    WHERE name = %s
    ORDER BY states.id ASC
    """

    cursor.execute(query, (state_name,))  # Pass state_name as a query parameter

    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("Not found")

    cursor.close()
    connection.close()


def get_arguments():
    """
    Retrieves username, database name, and state name from arguments (avoid password).
    """

    import sys
    if len(sys.argv) != 4:
        print("Usage: ./2-my_filter_states.py <mysql username> <database name> <state name>")
        sys.exit(1)

    return sys.argv[1], None, sys.argv[2], sys.argv[3]


def connect_to_database(username, db_name):
    """
    Establishes a connection to the MySQL database, prompting for password securely.
    """

    try:
        password = get_password()  # Prompt for password securely
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        return connection
    except MySQLdb.Error as err:
        print("Error connecting to database:", err)
        exit(1)


def get_password():
    """
    Prompts the user for the MySQL password securely without echoing input.
    """

    from getpass import getpass
    password = getpass("Enter MySQL password: ")
    return password


if __name__ == "__main__":
    main()
