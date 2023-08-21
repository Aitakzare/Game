import random
num = random.randint(1 , 10000)
a = 0
while True:
    a = int(input("Enter the number between (1 , 10000)...!\n"))
    a +=1
    if a == num:
        print("very good the number is" , a , "natijeh")
        break
    elif a < num:
        print("the number is grater than with number")
    else:
        print("the number is lower than with number")
