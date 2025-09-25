# 17. Email — Show Sender and Subject


class Email:
    def __init__(self, sender, subject):
        self.sender = sender
        self.subject = subject

    def show(self):
        print(f"From: {self.sender}\nSubject: {self.subject}")

email = Email("alice@example.com", "Hello!")
email.show()


