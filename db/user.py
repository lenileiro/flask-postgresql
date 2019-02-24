from datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Base


class UserModel:
    @staticmethod
    def insert_user(params):
            created_at = '%s' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            hashed_pwd = generate_password_hash(params["password"])

            national_id = Base.insert(
              'user',
              national_id=params["national_id"],
              firstname=params["firstname"],
              lastname=params["lastname"],
              othername=params["othername"],
              email=params["email"],
              isadmin=params["isadmin"],
              phone=params["phone"],
              passporturl=params["passporturl"],
              password=hashed_pwd,
              created_at=created_at
               )
               
            return Base.get('user', national_id=national_id)
