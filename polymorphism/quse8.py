class Loan:
    def interest(self):
        print("General loan interest")

class HomeLoan(Loan):
    def interest(self):
        print("Home loan interest 8%")

class CarLoan(Loan):
    def interest(self):
        print("Car loan interest 10%")

l = Loan()
h = HomeLoan()
c = CarLoan()

l.interest()
h.interest()
c.interest()
