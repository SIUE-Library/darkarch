import sys

if len(sys.argv) < 2:
	print("Usage:\npython3 identify_dup.py <text file>")
    sys.exit(1)

filename = sys.argv[1]
ls = []

for f in open(file, "w+"):
