class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class MailSender:
    def send_mail(self):
        print(f"თქვენი მეილი გაიგზავნა ამ მისამართზე: {self.email}")


class Friend(Contacts, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email

    def send_mail(self):
        super().send_mail()


class Family(Contacts, MailSender):
    def __init__(self, name, phone, email, birthdate):
        self.email = email
        self.birthdate = birthdate
        super().__init__(name, phone)

    def send_mail(self):
        super().send_mail()

    def __str__(self):
        while True:
            if len(self.birthdate) == 10:
                print(self.birthdate)
                return False
            else:
                print("გთხოვთ თქვენი დაბადების დრო ჩაწეროთ შემდეგ მაგალითის სახით დღე/თვე/წელი მაგ:02/03/2000")
                break


friend = Friend("giorgi", 51844854, "giorgi.zardiashvili.1@btu.edu.ge")
#print(friend.send_mail())
family = Family("giorgi", 45444451, "giorgi.zardiashvili.1@btu.edu.ge", "02/05/200")
print(family.__str__())
