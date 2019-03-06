import sys

if len(sys.argv) < 2:
	print("Usage:\npython3 identify_dup.py <text file>")

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
	li = str(l).replace("\\x00", "")
	li = li.replace("\\\\", "/")
	li = li.replace("\r", "")
	li = li.replace("\n", "")
	arr.append( line(li[94:-1], li[2:94]) )

print("Hash,File A,File Two")
for l in range(1, len(arr)-1):
	if arr[l-1].md5 == arr[l].md5 and arr[l-1].path != arr[l].path:# and arr[l-1].path.split("\\")[-1] !=  arr[l].path.split("\\")[-1]:
		print(str(arr[l-1].md5)+","+str(arr[l-1].path)[:-4].rstrip()+","+str(arr[l].path)[:-4].rstrip())
		arr[l-1].isUnique = False
		arr[l].isUnique = False
