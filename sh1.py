class Bank_Account:
    def __init__(self, account_name, balance_account_name=0):
        self.minus = None
        self.add = None
        self.__account_name = account_name
        self.__balance_account_name = balance_account_name

    def get_name(self):
        return self.__account_name

    def set_name(self, text):
        self.__account_name = text

    def set_balance(self, text):
        self.__balance_account_name = text

    def deposit(self):
        print(f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance_account_name + self.add}")

    def winthdraw(self):
        print(f"თანხსი გატანა შესრულებულია, ამჟამად თქვენ ანგრიშზე გაქვთ {self.__balance_account_name - self.minus}")

    name = property(get_name, set_name)


bank = Bank_Account("name", )
name = bank.name = input("შეიტანეთ კლიენტის სახელი გვარი: ")
bal = bank.set_balance = int(input("შეიტანეთ ამჟამინდელი თანხა: "))
bank = Bank_Account(name, bal)
a = int(input("შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულება გსურთ:\nთანხის შეტანა: 1, თანხის გამოტანა: 2\n "))
while True:
    a = int(input("აირჩიეთ მითითბული რიცხვები: 1 - თანხის შეტანა 2 - თანხის გამოტანა "))
    if a == 1:
        bank.add = int(input("რა თანხის შეტანა გსურთ? "))
        print(bank.deposit())
        break
    elif a == 2:
        bank.minus = int(input("რა თანხის გატანა გსურთ? "))
        print(bank.winthdraw())
        break
