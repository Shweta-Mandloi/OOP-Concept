class Food:
    def taste(self):
        print("General taste")

class Pizza(Food):
    def taste(self):
        print("Pizza is cheesy")

class IceCream(Food):
    def taste(self):
        print("IceCream is sweet")

f = Food()
p = Pizza()
i = IceCream()

f.taste()
p.taste()
i.taste()
