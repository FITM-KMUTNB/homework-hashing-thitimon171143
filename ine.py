more = "Y"
name = ["","","","","","","","","",""]
def input_name(names,i_d,num):
    global name
    data = {names:i_d}
    if name[num] == "":
        name[num]=data
    else:
        count = -1
        for i in name:
            count+= 1
            if i == "":
                name[count] = data
                break
    return name
def ran(names):
    index = hash(names)%10
    if index >= 10 :
        index = index % 10
    return index
while more == "Y":
    print('-----Hash-----')
    print("   1 INPUT    ")
    print("   2 SEARCH   ")
    print("   3 EXIT     ")
    print('--------------')
    enter = input("Enter 1,2,3 : ")
    if enter == "1":
        yes = "Y"
        while yes == "Y":
            if "" not in name:
                print("!!! List Full !!!")
                yes ="N"
            names = input("Enter name :")
            i_d = input("Number ID :")
            num = ran(names)
            input_name(names,i_d,num)
            yes = input("Do you want anymore (Y = Yes , N = No) : ")
    elif enter == '2':
        yes2= "Y"
        while yes2 == 'Y':
            names = input('Enter name :')
            num = ran(names)
            if names in name[num]:
                print("ID:",name[num].get(names))
            else:
                for i in name:
                    if names in i:
                        print("ID",i.get(names))
                        break
            yes2 = input("Do you want anymore (Y = Yes , N = No) : ")
    else:
        more = "N"