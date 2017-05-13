sizes = [1, 19, 13, 24, 30]
print("These are my sheep sizes:",','.join(str(a) for a in sizes))
best = sizes[1]
pos = 0
for i in range(len(sizes)):
    if sizes[i] >= best:
        best = sizes[i]
print("My biggest sheep has size",best)
sizes[sizes.index(best)] = 8
print("After shearing, here is my flock")
print(','.join(str(a) for a in sizes))
for i in range (1,5):
    month = [ size + 50 for size in sizes]
    sizes = month
    print("MONTH", i , ":")
    print("One month has passed, now here is my flock's sizes")
    print(month)
    for i in range(len(sizes)):
        if sizes[i] >= best:
            best = sizes[i]
    print("My biggest sheep has size",best)
    sizes[sizes.index(best)] = 8
    print("After shearing, here is my flock")
    print(','.join(str(a) for a in sizes))
total = 0
for i in range (len(sizes)):
    total = total + sizes[i]
print("My flock has size in total:",total)
money = total *2
print("I would get",total,"*2 =", total*2) 
