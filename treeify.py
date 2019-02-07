import sys
import string
import os
from treelib import Node, Tree
from collections import Counter

if len(sys.argv) < 2:
        print("Usage:\npython3 convert.py <text file>")
        sys.exit(1)
filename = sys.argv[1]

class line(object):
	path = ""
	md5 = ""
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

dic = Counter(hashes)

for a in arr:
    if dic[a.path] > 1:
        a.isUnique = False
    

prev= None
master = ""

tree.create_node("Old Archive", "Old Archive/")

for a in arr[1:]:
    prev = None
    a.path = str(a.path).replace("\\x00", "")[2:-5]
    a.md5 = str(a.md5).replace("\\x00", "")[2:-1]
    a.path = str(a.path).replace("\\\\", "/")
    a.path = str(a.path).replace("\r", "")
    a.path = str(a.path).replace("\n", "")
    print(a.path)
    print(a.md5)
    master = ""
    for folder in a.path.split("/")[0:-1]:
        master += folder + "/"
        if tree.get_node(master) == None:
            tree.create_node(folder, master, parent=prev)
        prev = master
    folder = a.path.split("/")[-1:][0]
    print(folder)
    master += folder + "/"
    if tree.get_node(master) == None:
        tree.create_node(folder, master, parent=prev)
    prev = master


print(tree.show())
print(tree.depth())

