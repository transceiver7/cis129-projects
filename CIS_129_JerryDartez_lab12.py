# Jerry Dartez
# CIS 129
# Module 12 Lab
# 5/16/24

# Class Pet (private fields: name, type, age)
class Pet:
    def __init__(self, name, type, age):
        self._name = name
        self._type = type
        self._age = age

    # Constructor
    # Public module Pet
    def Pet(self, n, t, a):
        self.name = n
        self.type = t
        self.age = a
        
    # Mutators (Public)
    def set_name(self, n):
        self.name = n

    def set_type(self, t):
        self.type = t

    def set_age(self, a):
        self.age = a

    # Accessors (Public)
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_age(self):
        return self.age


# Main function
def main():
    # declare input variables
    input_name = ''
    input_type = ''
    input_age = 0

    # class variable to hold a pet
    Animal = ''

    # create a Pet object
    Animal = Pet(input_name, input_type, input_age)

    # get values for a pet
    print()
    input_name = input('Enter a pet name: ')
    Animal.set_name(input_name)

    input_type = input('Enter a pet type: ')
    Animal.set_type(input_type)

    input_age = int(input('Enter a pet age: '))
    Animal.set_age(input_age)

    # show values for this pet
    print()
    print('The pet name is ', Animal.get_name())
    print('The pet type is ', Animal.get_type())
    print('The pet age is ', Animal.get_age())

main()