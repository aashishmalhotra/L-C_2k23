class Human:
    def __init__(self):
        self.__head = 1
        self.__arms = 2
        self.__legs = 2

    def introduce(self):
        print(f"I have a {self.__head} head, {self.__arms} arms, and {self.__legs} legs.")

class Person(Human):
    def __init__(self, name, age, occupation):
        super().__init__()  # Call the constructor of the parent class
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def get_occupation(self):
        return self.__occupation

    def introduce(self):
        super().introduce()
        print(f"Hello, I am {self.__name}, and I am {self.__age} years old.")
        print(f"My occupation is: {self.__occupation}")

person = Person("Ashish", 30, "teacher")
person.introduce()
