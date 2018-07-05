class Employee():
    def __init__(self, first_name,last_name,salery):
        self.first_name = first_name
        self.last_name = last_name
        self.salery = salery
    def default_salery():
        print(self.salery)
    def give_raise(self,up=5000):
        self.salery += up
        return self.salery
# sample1 = Employee("lili","calisy",30000)
# sample1.give_raise(4000)