class FastFood:
    def _init_(self,price,size,orderNumber):
        self.price = price
        self.size = size
        self.orderNumber = orderNumber

    def set_size(self,size):
        self.size = size

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def get_orderNumber(self):
        return self.orderNumber

    def print_orderNumber(self):
        print(self.orderNumber)

class Tacos(FastFood):
    def tacosAttributes(self, meat, sauce):
        self.meat = meat #meat is a list of str
        self.sauce = sauce #sauce is a str

    def __str__(self):
        meats = ""
        for meat_list in self.meat:
            meats += meat +" "
        return "It is the tacos of order number " + str(get_orderNumber()) + "with : " + meats + "and : " + self.sauce

    def get_ingredient(self)
        return [ self.meat[i] for i in range(len(self.meat)), self.sauce[j] for j in range(len(self.sauce))]

class Burgers(FastFood):
    def burgersAttributes(self,name,sauce)
        self.name = name
        self.sauce = sauce

    def print_name(self):
        print(self.name)

    def get_sauce(self):
        return self.sauce
