from datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Base


class UserModel:
    @staticmethod
    def insert_user(params):
            return Base.insert(
              'user',
              national_id=params["national_id"],
              firstname=params["firstname"],
              lastname=params["lastname"],
              othername=params["othername"],
              email=params["email"],
              isadmin=params["isadmin"],
              phone=params["phone"],
              password=params["password"],
              passporturl=params["passporturl"]
               )
