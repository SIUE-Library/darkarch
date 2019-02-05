import sys

class Node:
    childList = [    ]
    name = ""
    hash = ""

    def __init__(self, name, hash, childList):
        self.name = name
        self.hash = hash
        self.childList = childList

#enter execution
print("hello world")
