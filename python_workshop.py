"""
Malte's Workshop in Python
    classes, strings, list comprehension, cool tricks

"""

#--------------Classes----------------#
#storing data and functions together - when it makes sense


class Greeter:
    def get_name(self):
        return "Malte"
    
    def greet(self):
        self.ask_server_for_advice()
        print("Hello " + self.get_name())
    
    def ask_server_for_advice(self):
        print("IMPORTANT INGO")
        pass

malte = Greeter()
malte.greet()

#Inherit all greeter class properties, which can be modified
class DoorGreeter(Greeter):
    def __init__(self, name):
        self.name = name
    def greet(self):
        self.ask_server_for_advice()
        print("Hello "+ self.name)
    def ask_server_for_advice(self):
        print(" /n is this the right server?")
    pass

anita = DoorGreeter("Anita")
anita.greet()




#--------------String formatting----------------#
var = 123
print(f"test{var}") #prints test123

listofletters = ["h", "e", "y"]
''.join(listofletters)
"_".join(listofletters)


string1 = "abc"
string2 = "123"

string1+string2




#List comprehension
mylist = ["a", "b", "d"]
x = "d"
mylist2 = [z for z in mylist if z != x]

#map/apply a function to elements of the list
mylist2 = [f(x)+2 for x in mylist]



#--------------Unpacking---------------#

#returns tuples
#enumerate(["a", "b"]) --> [(0, "a"), (1, "b")]

for i, item in enumerate(mylist):
    do_something_with(i)
    do_something_with(item)



def some_fun(*args):
    for arg in args:
        do_something

#dictionary
mydict = {'key1': 2, 'b':3}
mydict['b']
for key, value in mydict.items():
    print(key)
    print(value)

if 'cucumber' in list_of_fruits:
    do_something()
else:
    do_something_else()


#Exercise 2
def string_combine(input_list, input_string):
    return([str(number) + input_string for number in input_list])

string_combine([1,2,3], "test")


#Exercise 3

def print_game_summary(*args):
    winner = [index+1 for index, item in enumerate(args) if item == max(args)]
    points_diff = max(args) - min(args)
    print(f"The winner is Player {winner[0]} with {points_diff} points of difference from the last player")


print_game_summary(2, 18, 33, 90)