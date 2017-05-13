

print(" Create: 'C' , Read: 'R', Update: 'U', Delete: 'D'")
while True:
    print(" Welcome t’o our shop,")
    item_no = 1
    for clothe in clothes:
        print("{0}. {1}".format(item_no, clothe))
        item_no+= 1
    action = input("What do you want (C, R, U, D)?") # Dung vong while lai de doi lenh tiep theo
    action = action.upper()
    if action == "C":
        item = input(" Item to create?")
        clothes.append(item)
        print ("Our items:",clothes)

    elif action == "R":
        print ("Our items:",clothes)
    elif action == "U":
        position = int(input("Update position:"))
        if position > len (clothes):
            print ("There's no item number")
            print()
        else:
            item = input("New item:")
            clothes[position-1] = item
            print ("Our items:",clothes)
    else:
        position = int(input("Delete position:"))
        if position > len (clothes):
            print ("There's no item number")
            print()
        else:
            del clothes[position-1]
            print ("Our items:",clothes)
        
    print ()
time.sleep(3)

