def madlib(name1 = "1",bignum1 = "2",food1 = "3",place1 = "4",verb1 = "5",place2 = "6", adjictive1 = "7", like1 = "8", hobby1 = "9", nickname1 = "10"):
    print("")
    print("Let me introduce you to my dragon frend, " + name1 + "! They are " + bignum1 + " years old, their favorite food is " + food1 + ".")
    print("When I was little, I traveled to " + place1 + " with my mom and dad, and met them when I was " + verb1 + ". Because I was " + verb1 + " all")
    print("day long. When " + name1 + " flew right into " + place2 + " and landed right next to me, my mom fainted! But I didnt")
    print("I thought my dragon frend looked " + adjictive1 + ", and I burst out laughing, and then they did too! We started talking about")
    print("how we both like " + like1 + " and " + hobby1 + " so i started calling them " + nickname1 + " and swaped phone numbers to saty in touch!")
    print("")
def banana(x,y):
    for i in range(y):
        if x != 1:
            name1 = input("Noun: ")
            bignum1 = input("Big number: ")
            food1 = input("Noun: ")
            place1 = input("Place: ")
            verb1 = input("Past tense verb: ")
            place2 = input("Place: ")
            adjictive1 = input("Adjictive: ")
            like1 = input("Somthing you like: ")
            hobby1 = input("Hobby: ")
            nickname1 = input("Nickname: ")
            madlib(name1,bignum1,food1,place1,verb1,place2,adjictive1,like1,hobby1,nickname1)
        else:
            madlib()
banana(1,3)