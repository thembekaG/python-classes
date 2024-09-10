class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes of the class
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print a message introducing the person
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old and I'm a {self.gender}.")


# Create an instance of the Person class
person_instance = Person(name="Thembeka", age=30, gender="Female")

# Call the introduce method to display the person's information
person_instance.introduce()
