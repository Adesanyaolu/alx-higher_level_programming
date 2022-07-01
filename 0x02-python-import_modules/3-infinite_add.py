#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argLeng = len(sys.argv) - 1
    argSum = 0

    for i in range(argLeng):
        argSum = argSum + int(sys.argv[i+1])
    print(argSum)
