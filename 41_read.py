f = open('myfiles.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in marks is : {m1*2}")
    print(f"Marks of student {i} in marks is : {m2*2}")
    print(f"Marks of student {i} in marks is : {m3*2}")
    print(line)