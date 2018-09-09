import pickle


class Person:

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def greet(self):
        print(f'Hi, i am {self.first_name} {self.last_name}'
              f' and my ID is {self.id}')


people = [
    Person('John', 'Kennedy', 454),
    Person('Gearge', 'Bush', 1236)
]

#Save data in binary format to a file
with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

#Load data from a file
with open('data.pickle', 'rb') as stream:
    peeps = pickle.load(stream)
    for person in peeps:
        person.greet()
