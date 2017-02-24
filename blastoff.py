#project name: Blastoff
#programmer: Yang Tang
#date: 2/16/2017
#description: use print and recursion to display the picture of spaceship and countdown number
n=15
i=0
# initial value
def countdown(n):
    if n<=0:
        print("blastoff")
        # yt:print the blastoff text
    else:
        # yt: use else to determine the non 0 condition
        if n==8:
            print(n,"\t\t *")
        elif n==7:
            print(n,"\t\t/ \ ")
        elif n == 6:
            print(n,"\t\t| |")
        elif n == 5:
            print(n,"\t\t|Y|")
        elif n == 4:
            print(n,"\t\t|A|")
        elif n == 3:
            print(n,"\t\t|N|")
        elif n == 2:
            print(n,"\t\t|G|")
        elif n == 1:
            print(n,"\t\t/ \ ")
            # print the shape of the spaceship by using symbols
        else:
            print(n)
            # yt:use else statement to print the extra number of the countdown
        countdown(n-1)
        # yt: call function itself to do the next number
countdown(n)