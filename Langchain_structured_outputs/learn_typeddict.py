from typing import TypedDict

class Person(TypedDict):

    name : str
    age : int


naved: Person = {'name' : 'Naved','age' : '26'}

print(naved)