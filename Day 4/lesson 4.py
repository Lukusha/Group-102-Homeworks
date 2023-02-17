# print(10/3)
# print(10//3) #daabrunebs mtel ricxvs.moachris wertilis mere ricxvebs

# print(5**2) # ** aris xarisxi





                                
                            #############  LOOPS  #############


# my_name = ("Luka")

#     #char agvnishnet saiteracio cvladi
# for char in my_name:
#     print(char)



#print("i" in "Luka")



                            ############ CLASS WORK ############


            #მომხმარებელს შემოვატანინებთ ორ სახელს და იმას დავპრინტავთ რომელის სახელშიც მეტი ხმოვანი იქნება


# name1 = input("Enter first name : ")
# name2 = input("Enter second name : ")

# xmovnebi_in_name1 = 0
# xmovnebi_in_name2 = 0

# for char in name1 :
#     if char in "aeiou" :
#         xmovnebi_in_name1 += 1

# for char in name2 :
#     if char in "aeiou" :
#         xmovnebi_in_name2 += 1


# if xmovnebi_in_name1>xmovnebi_in_name2 :
#     print("Amount of vowels in name 1 contains {} vowels and is more than the second name".format(xmovnebi_in_name1))
# elif xmovnebi_in_name2>xmovnebi_in_name1 :
#     print("Amount of vowels in name 2 contains {} vowels and is more than the second name".format(xmovnebi_in_name2))
# else :
#     print("They have equal amount")



                            ########## CLASS WORK N2 ###########
            
            #შემოიტანეთ რაღაც წინადადება და დათვალეთ რამდენი ა გვხვდება


# my_setnence = input("Write a sentence : ")
# count_a = 0

# for char in my_setnence :
#     if char == "a": 
#          count_a += 1

# print('We have {} a -s in "a" sentence you entered'.format(count_a))




# num = 12

# if num > 5 :
#     print("bigger than 5")
#     if num <= 47 :
#         print("Between 5 and 47")







name1 = input("Enter first name : ")
name2 = input("Enter second name : ")

tanxmovnebi_in_name1 = 0
tanxmovnebi_in_name2 = 0

for char in name1 :
    if char not in "aeiou" :
        tanxmovnebi_in_name1 += 1

for char in name2 :
    if char not in "aeiou" :
        tanxmovnebi_in_name2 += 1


if tanxmovnebi_in_name1>tanxmovnebi_in_name2 :
    print("Amount of vowels in name 1 contains {} consonants and is more than the second name".format(tanxmovnebi_in_name1))
elif tanxmovnebi_in_name2>tanxmovnebi_in_name1 :
    print("Amount of vowels in name 2 contains {} consonants and is more than the second name".format(tanxmovnebi_in_name2))
else :
    print("They have equal amount")