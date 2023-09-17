import bcrypt
import psycopg2 as pg


class DatabaseManager:
    def __init__(self, database_config_model):
        self.db_config = database_config_model

    def save_account(self, users_model):
        # Get the database configuration parameters
        db_params = self.db_config.get_db_config()
        try:
            # Establish a database connection
            connection = pg.connect(**db_params)
            cursor = connection.cursor()

            # SQL query to insert user information into the 'users' table
            sql_query = '''
                INSERT INTO dark_star_bank.users (first_name, last_name, email)
                VALUES (%s, %s, %s)
                RETURNING id
            '''

            # Execute the SQL query with user data and retrieve the user ID
            cursor.execute(sql_query, (
                users_model.first_name,
                users_model.last_name,
                users_model.email
            ))

            user_id = cursor.fetchone()[0]
            connection.commit()

            cursor.close()
            connection.close()

            # If user account is saved successfully, create authentication credentials
            if self.create_authentication_credentials(user_id, users_model.password):
                return user_id
            else:
                return False

        except Exception as e:
            print(f"Error saving account data: {str(e)}")
            return False

    def create_authentication_credentials(self, user_id, password):
        # Get the database configuration parameters
        db_params = self.db_config.get_db_config()
        try:
            # Establish a database connection
            connection = pg.connect(**db_params)
            cursor = connection.cursor()

            # SQL query to insert authentication credentials (user ID and password hash)
            sql_query = '''
                INSERT INTO dark_star_bank.authentication_credentials (user_id, password_hash)
                VALUES (%s, %s)
            '''

            # Execute the SQL query with user ID and password hash
            cursor.execute(sql_query, (user_id, password))
            connection.commit()

            cursor.close()
            connection.close()

            return True

        except Exception as e:
            print(f"Error creating authentication credentials: {str(e)}")
            return False

    def are_credentials_valid(self, email, password):
        # Get the database configuration parameters
        db_params = self.db_config.get_db_config()
        try:
            # Establish a database connection
            connection = pg.connect(**db_params)
            cursor = connection.cursor()

            # SQL query to validate user credentials based on email
            sql_query = '''
                SELECT users.id, users.first_name, users.last_name, authentication_credentials.password_hash
                FROM dark_star_bank.users
                INNER JOIN dark_star_bank.authentication_credentials
                ON users.id = authentication_credentials.user_id
                WHERE users.email = %s
            '''

            # Execute the SQL query with the provided email
            cursor.execute(sql_query, (email, ))
            user_data = cursor.fetchone()

            if user_data:
                user_id, first_name, last_name, stored_password_hash = user_data
                cursor.close()
                connection.close()
                # Verifique se a senha fornecida pelo usuário corresponde ao hash armazenado
                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    return user_id, first_name, last_name
                else:
                    return None
            else:
                cursor.close()
                connection.close()
                return None

        except Exception as e:
            print(f"Error validating credentials: {str(e)}")
            return None

    def create_account_bank(self, user_id):
        # Get the database configuration parameters
        db_params = self.db_config.get_db_config()
        try:
            # Establish a database connection
            connection = pg.connect(**db_params)
            cursor = connection.cursor()

            # Set the default values for the new account
            bank_code = 77  # Suponha que 1 é o código do banco padrão
            account_type = 'business_account'
            balance = 10000.00
            overdraft_limit = 1000.00

            # Determine the next account number with a checksum (you may need a more complex logic)
            last_account_number = self.get_last_account_number(cursor)
            next_account_number = last_account_number + 1
            # Preencher com zeros à esquerda
            account_number = f"{next_account_number:09d}-2"

            # Set a default branch number
            branch_number = "0001"

            # SQL query to insert account bank information
            sql_query = '''
                INSERT INTO dark_star_bank.account (user_id, bank_code, account_type, balance, overdraft_limit, account_number, branch_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''

            # Execute the SQL query with account bank data
            cursor.execute(sql_query, (user_id, bank_code, account_type,
                           balance, overdraft_limit, account_number, branch_number))
            connection.commit()

            cursor.close()
            connection.close()

            return True

        except Exception as e:
            print(f"Error creating account bank: {str(e)}")
            return False

    def get_last_account_number(self, cursor):
        try:
            # Query the database to get the highest account number
            sql_query = '''
                SELECT MAX(account_number)
                FROM dark_star_bank.account
            '''
            cursor.execute(sql_query)
            result = cursor.fetchone()[0]

            if result is not None:
                # Extract the numeric part of the last account number
                last_account_number = int(result.split('-')[0])
            else:
                # If no account exists, start with 1
                last_account_number = 0

            return last_account_number

        except Exception as e:
            print(f"Error getting last account number: {str(e)}")
            return 0

    def is_email_registered(self, email):
        # Get the database configuration parameters
        db_params = self.db_config.get_db_config()
        try:
            # Establish a database connection
            connection = pg.connect(**db_params)
            cursor = connection.cursor()

            # SQL query to check if the email is registered
            sql_query = '''
                SELECT COUNT(*) FROM dark_star_bank.users WHERE email = %s
            '''

            # Execute the SQL query with the provided email
            cursor.execute(sql_query, (email, ))
            count = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            return count > 0

        except Exception as e:
            print(f"Error checking if email is registered: {str(e)}")
            return False
