class User():
    def __init__(self, first_name,last_name,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
    def describe_user(self):
        print("your name is " + self.last_name.title() + "." + self.first_name.title() + ", and you are " + self.sex.title())
    def great_user(self):
        print("welcome! " + self.last_name.title() + "." + self.first_name.title())

# class Dog():
user1 = User("yujie","wang","girl")
user2 = User("jun","wang","boy")
user3 = User("kaixiu","xiong","woman")
user1.describe_user()