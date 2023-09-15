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
                return True
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
