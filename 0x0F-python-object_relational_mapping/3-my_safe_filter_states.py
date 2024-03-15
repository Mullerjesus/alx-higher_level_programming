#!/usr/bin/python3
"""
This script retrieves and displays state data from the hbtn_0e_0_usa database,
securely preventing SQL injection attacks.

Arguments:
    mysql_username: Username for MySQL access.
    mysql_password: Password for MySQL access.
    db_name: Name of the database to connect to (hbtn_0e_0_usa).
    state_name: The state name to search for (safe from SQL injection).
"""

import MySQLdb


def main():
    """
    Connects to the database, executes the query securely, and displays results.
    """

    # ... (Identical to previous script until query formatting)

    # Safely create the query using query parameters
    query = """
    SELECT * FROM states
    WHERE name = %s
    ORDER BY states.id ASC
    """

    cursor.execute(query, (state_name,))  # Pass state_name as a query parameter
