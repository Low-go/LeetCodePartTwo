class DBManager:
    def open_connection(self):
        """Call this prior to reading from/writing to the DB"""
        print(f'Connecting to DB')

    def close_connection(self):
        """Call this after having completed reading from/writing to the DB"""
        print(f'Closing connection to DB')

    def save_to_database(self, rows):
        """Called to store the passed rows into the database
        Args:
            rows (list): A list of rows in the form of dictionaries to be stored
                        into the database
        """
        print(f'{len(rows)} row(s) of data saved successfully.')