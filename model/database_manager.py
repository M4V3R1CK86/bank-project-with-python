
import psycopg2 as pg


class DatabaseManager:
    def __init__(self, database_config_model):
        # Configure your PostgreSQL connection parameters
        self.db_config = database_config_model

    def save_account(self, account_model):
        db_params = self.db_config.get_db_config()
        # print('db_params: ', db_params)
        try:

            # Create a database connection
            connection = pg.connect(**db_params)

            # print('connection: ',  connection=pg.connect(**db_params))

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL INSERT query to save the account data
            sql_query = '''
                INSERT INTO darkstarbank.accounts (first_name, last_name, email, password)
                VALUES (%s, %s, %s, %s)
            '''

            # Execute the SQL query with the data from the account model
            cursor.execute(sql_query, (
                account_model.first_name,
                account_model.last_name,
                account_model.email,
                account_model.password
            ))

            # Commit the changes to the database
            connection.commit()
            print('commit: ', connection.commit)

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return True  # Data saved successfully
        except Exception as e:
            print(f"Error saving account data: {str(e)}")
            return False  # Error occurred while saving data
