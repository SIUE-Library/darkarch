import sys
import string
import os
from treelib import Node, Tree
from collections import Counter
import time

if len(sys.argv) < 2:
        print("Usage:\npython3 convert.py <text file>")
        sys.exit(1)
filename = sys.argv[1]

def DFS(T):
    stack = []
    visited = []
    uniqueFolder = 0
    totFolder = 0
    stack.append(T.get_node("Old Archive/"))
    while len(stack) > 0:
        next = stack.pop()
        for child in next.fpointer:
            stack.append(T.get_node(child))
            if T.get_node(child).is_leaf():
                print(T.get_node(child).data.clone)


        unique = 0
        for child in next.fpointer:
            if str(T.get_node(child).tag) == "True":
                unique = 1
        if not next.is_leaf():
            next.tag = str(unique == 1)
            uniqueFolder += unique
            totFolder += 1

    print(uniqueFolder)
    print(totFolder)

def toPrune(T):
    stack = []
    visited = []
    stack.append(T.get_node("Old Archive/"))
    while len(stack) > 0:
        next = stack.pop()
        if next.tag != "False":
            for child in next.fpointer:
                stack.append(T.get_node(child))
        else:
            print(next.identifier)



class line(object):
	path = ""
	md5 = ""
	clone = ""
	isUnique = True #assume there are no copies until proven otherwise

	def __init__(self, p, h):
		self.path = p
		self.md5 = h



tree = Tree()

file = open(filename, "rb")
arr = []
hashes = []

for l in file:
    if len(l) > 48:
        arr.append( line(l[100:], l[0:94]) )
        hashes.append(l[0:94])


c = 0
l = len(arr)
for a in arr:
    for r in arr:
        if a.path != r.path and a.md5 == r.md5:
            a.isUnique = False
            a.clone = r.path
    print("Completed iteration "+str(c)+" of "+str(l))
    c+=1
    
prev= None
master = ""
print("Deduping done")
tree.create_node("Old Archive", "Old Archive/")

for a in arr[1:]:
    prev = None
    a.md5 = str(a.md5).replace("\\x00", "")[2:-1]
    a.path = str(a.path).replace("\\x00", "")[2:-5]
    a.path = str(a.path).replace("\\\\", "/")
    a.path = str(a.path).replace("\r", "")
    a.path = str(a.path).replace("\n", "")

    a.clone = str(a.clone).replace("\\x00", "")[2:-5]
    a.clone = str(a.clone).replace("\\\\", "/")
    a.clone = str(a.clone).replace("\r", "")
    a.clone = str(a.clone).replace("\n", "")

    master = ""
    for folder in a.path.split("/")[0:-1]:
        master += folder + "/"
        if tree.get_node(master) == None:
            tree.create_node(folder, master, parent=prev)
        prev = master
    folder = a.path.split("/")[-1:][0]
    master += folder + "/"
    if tree.get_node(master) == None:
        tree.create_node(str(a.isUnique), master, parent=prev, data=a)
    prev = master


#print(tree.show())
print(tree.depth())
#time.sleep(1)


DFS(tree)
toPrune(tree)
