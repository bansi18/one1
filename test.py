i: int = 1

while i <= 100:

    if i % 3 != 0 and i % 5 != 0:
        print(f"{i}",end=",")
    i = i + 1


j = 0

while j<5:
    print(5*'#')
    j=j+1