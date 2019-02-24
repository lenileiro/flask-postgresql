class Validate:

    @staticmethod
    def init_data(data):
        try:
            return Validate.is_valid(
                firstname=data["firstname"],
                lastname=data["lastname"],
                othername=data["othername"],
                email=data["email"],
                isadmin=data["isadmin"],
                phone=data["phone"],
                passporturl=data["passporturl"],
                password=data["password"]
                )

        except KeyError as e:
            return f"{e} field is required"

    @staticmethod
    def is_valid(**kwargs):
        '''checks if any required field is blank'''
        for key, val in kwargs.items():
            if val.strip() == '':
                return f'{key} field cannot be blank'
