import sys
import string
import os

if len(sys.argv) < 2:
	print("Usage:\npython3 convert.py <text file>")

filename = sys.argv[1]

class line(object):
	path = ""
	md5 = ""
	isUnique = True #assume there are no copies until proven otherwise

	def __init__(self, p, h):
		self.path = p
		self.md5 = h



file = open(filename, "rb")
arr = []

for l in file:
    if len(l) > 48:
        arr.append( line(l[101:], l[0:94]) )
c = 0

for a in arr:
    for r in arr:
        if a.path != r.path and a.md5 == r.md5:
            a.isUnique = False
            a.clone = r.path
    c+=1
    print("One iter complete, this is "+str(c) +" of "+str(len(arr)))

print("Creating Files")
for a in arr:
#    print(type(a.path))
    a.path = str(a.path).replace("\\x00", "")[2:-5]
    a.md5 = str(a.md5).replace("\\x00", "")[2:-1]
    a.path = str(a.path).replace("\\\\", "/")
    a.path = str(a.path).replace("\r", "")
    a.path = str(a.path).replace("\n", "")
    print(a.path)
    print(a.md5)
    master = ""
    for folder in a.path.split("/")[:-1]:
        master += folder + "/"
        if not os.path.exists(master):
            os.mkdir(master)

    file = open(a.path+"_"+str(a.isUnique)+"_COPY.txt", "w+").write(a.md5)
