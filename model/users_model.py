import bcrypt


class UsersModel:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = None

    def set_password(self, password):
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Armazene a senha hash (hashed_password) no modelo
        self.password = hashed_password

    def check_password(self, password):
        # Verifique se a senha fornecida corresponde à senha hash armazenada
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
