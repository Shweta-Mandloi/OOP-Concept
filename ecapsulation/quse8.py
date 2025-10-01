class Phone:
    def __init__(self, model):
        self.__model = model

    def show_model(self):
        print("Phone Model:", self.__model)

ph = Phone("Samsung Galaxy")
ph.show_model()
