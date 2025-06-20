import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    count = string.count("z")
    if count == 0:
        print("none")
    else:
        for _ in range(count):
            print("z")
