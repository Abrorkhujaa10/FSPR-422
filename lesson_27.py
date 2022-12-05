class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if user ["email"] == email or user["password"] == password:
                return "Wrong email or password"
            else:
                break

        if not (name and email and password and card_code and card_balance):
            return "Empty values were given"
        if name.isalpha() and "@" in email and len(password) >= 6 and len(card_code) == 16:
            USERS.append(
                {
                    "name": name,
                    "password": password,
                    "email": email,
                    "purchases": [],
                    "card": {"code": card_code, "balance": card_balance}
                }
            )
            return cls(name, email, password, card_code, card_balance)
        else:
            return "Wrong credentails"

    @classmethod
    def login(cls, email, password):
        pass

enter_method = input("Chosse method: register or login: ")
if enter_method == "register":
    user_1 = Store.register("Behruz", "behruz@gmail.com", "777777", "1234567891234564", 1000)
elif enter_method == "login":
    # user_1 = Store.register("Behruz", "behruz@gmail.com", "777777", "1234567891234564", 1000)

 print(user_1)
 print(user_1.name, user_1.email, user_1.password)
 for user in USERS:
    print(user)