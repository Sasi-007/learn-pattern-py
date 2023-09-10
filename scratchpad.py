rows=5

for i in range(rows):
    for j in range(2*(rows-i)-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()