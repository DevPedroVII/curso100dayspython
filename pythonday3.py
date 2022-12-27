#operators

#< greater than
#< less than
#>= greater than or equal to
#<= less than or equal to
#== equal to
#!= not equal to


#if sempre vem na frente do else

# if pode obter mais um if/else
# exp:
# if conditin:
   # if another cond:
   #    haha
   # else:
   #     ha
#else:
# NO HAHA
#**é bom utilizar de fluxograms**

# elif

# elif pode ser add varias vezes no mesmo codigo DIFERENTE do  if e do else
# IF / ELIFS / ELSE ex:

print ("Welcome to the Rollercoaster!")
height = int(input("what is  your height ib CM? "))
bill = 0

if height >= 120:
    print ("Good You can ride the rollercoaster !!!")
    age = (int(input("what is your age?")))

if  age < 12 :
    bill = 5
    print("Please pay $5")
elif  age <= 18 :
    bill = 7
    print("Please pay $7")
elif  age > 18 :
     bill = 12
     print("Please pay $12")

wants_photo = input("do you want a photo? y or n. ")
if wants_photo == "y":
    bill += 3
    print(f"your final bill is:  ${bill} ")

else:
    print("how bad you can't ride the roller coaster")








