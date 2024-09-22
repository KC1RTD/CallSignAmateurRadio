import sqlite3
import pandas as pd

def create_connection(database_file: object = 'results.db') -> object:
    """

    :param database_file: the database file
    :return: if it connects sucessfully, then so be it
    """
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except sqlite3.Error as err1:
        print(f"Error: {err1}")
        return None


def create_results_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('\n'
                       '            CREATE TABLE IF NOT EXISTS results (\n'
                       '                id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                       '                level TEXT,\n'
                       '                name TEXT,\n'
                       '                callsign TEXT,\n'
                       '                original TEXT\n'
                       '            );\n'
                       '        ')
        connection.commit()
        cursor.close()
    except sqlite3.Error as err2:
        print(f"Error: {err2}")


def save_to_database(connection, level, name, callsign, original):
    """

    :param connection: connection string
    :param level: level of qualification
    :param name:
    :param callsign:
    :param original:
    """
    try:
        cursor = connection.cursor()
        cursor.execute('\n'
                       '            INSERT INTO results (level, name, callsign, original)\n'
                       '            VALUES (?, ?, ?, ?);\n'
                       '        ', (level, name, callsign, original))
        connection.commit()
        cursor.close()
    except sqlite3.Error as err2:
        print(f"Error: {err2}")


def radiodata():
    """

    :return:
    """
    csign = input("What callsign do you want to search? Enter it here\n")
    dframe = pd.read_json(f'https://callook.info/{csign}/json')
    level = dframe.iloc[1, 2]
    name = dframe.iloc[1, 5]
    callsign = dframe.iloc[0, 2]
    original = dframe.iloc[9, 8]

    # Save to SQLite database
    connection = create_connection()
    if connection:
        create_results_table(connection)
        save_to_database(connection, level, name, callsign, original)
        connection.close()

    results = f"{level}\n{name}\n{callsign}\n{original}"
    return results


result = radiodata()
print(result)



