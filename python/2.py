#######------ FUNCTIONS ------#####
def square(x):
    return x*x

print(square(9))

def foo(x):
 if x % 2 == 0:
    print(f'{x} is even!')
 elif x % 2 != 0:
    print(f'{x} is odd!')
 else:
    print("Did you type a number?")


invited = ["Alice", "Bob", "Carol"]
guest = "David"

# in works for string, list, tuple, dict(keys)
if guest in invited:
    print(f"Welcome, {guest}")
else:
    print(f"You are not invited, {guest}")


class Person:
    def __init__(self, name, inv):
        self.name = name
        self.inv = inv
    def is_invited(self):
        if self.inv:
            msg = f"Welcome, {self.name}"
        else:
            msg = f"You are not invited, {self.name}"
        return msg


persons = {}
guests = ["Alice", "Bob", "Carol", "David" ]
invites = [1] * 3 + [0] # first 3 guests invited, last not [1,1,1,0]

#pair guests with invite flag
# enumerate(): gives each pair a number no
for no, (guest, inv) in enumerate(zip(guests, invites)):

    #create new person object and add to dictionary
    persons[no] = Person(guest, inv)

for no, person in persons.items():
    print(f'Guest {no}: {person.is_invited()}')
