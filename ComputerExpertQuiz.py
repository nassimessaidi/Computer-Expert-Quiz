from os import system, name
import sys
from time import sleep
from colorama import Fore, Back, Style

def pattren():
    x="----------------------------------------------------------------------------------------------------"
    x=x.replace('-','=')
    print(Fore.BLUE+Back.WHITE+x)
    print(Style.RESET_ALL,end='')

def err():
    print(Fore.RED+"[*] Input Error !! [*]")
    print(Style.RESET_ALL,end='')
    sleep(1)

def clear():
    if name== 'nt':
        return system('cls')
    else:
        return system('clear')

score=0

# Q1
count=1
while count==1:
    count=0
    clear()
    pattren()
    print("Do you know what operating system you're using?")
    print("1- Windows")
    print("2- Mac")
    print("3- Linux")
    print("4- I dont know")
    try:
        x = int(input(">> "))
    except Exception as e:
        err()
        count = 1
        continue
    if x==1:
        score+=1
    elif x==2:
        score-=2
    elif x==3:
        score+=5
    elif x==4:
        print(Fore.WHITE+Back.RED+"You just automatically failed !! \nI don't know how you even function on your computer")
        sleep(10)
        sys.exit()

    else:
        err()
        count=1

# Q2
clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know what version operating system you're using?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1

# Q3
clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Are you someone who asks others for computer help?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score-=1
    elif x==2:
        continue
    else:
        err()
        count=1

#Q4:
clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Are you the one who gives computer help?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Are you a hunt and peck typer?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score-=5
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do  you know how big your hard drive is?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know your current screen resolution?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know how many cores your CPU has?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        count1=1
        while count1==1:
            count1=0
            try:
                x1=int(input("How many cores do you have: "))
                if x1>0:
                    score=score+0.5*x1
                else:
                    err()
                    count1=1
            except Exception as e:
                err()
                count1=1
    elif x==2:
        score-=1
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you still use your computer's default browser?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        score-=1
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever opened up your computer case?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=2
    elif x==2:
        continue
    else:
        err()
        count=1

clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever used Linux?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=2
    elif x==2:
        continue
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you backup your hard drive?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        score-=3
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know whether your computer is Intel or AMD?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever changed your browser homepage?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        continue
    elif x==2:
        score-=1
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever change your Wi-Fi password from the default?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=2
    elif x==2:
        continue
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know what USB stands for?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=2
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know the difference between a megabit and a megabyte ?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("How many hour do you spend on the computer daily?(Not counting when you working)")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x>=0:
        score=score+x
    elif x<0:
        err()
        count=1
    else:
        err()
        count=1


clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever used the command prompt(cmd)?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=2
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know the difference between Java and Javascript?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do your password contain special characters?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever installed new hardware in your computer?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=3
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("How many monitor you have?")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x>=0:
        score=score+x
    elif x<0:
        err()
        count=1
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do your know the difference between HTTP and HTTPS?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever build a computer?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=4
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you overclocked your CPU manually?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=5
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do your know what RAM timings are and how they work?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=3
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("I'm going to name some famous computer people and for every one that you know you get 1 pt")
    names=["Steve Wozniak","Dennis Ritchie","Richard Stallman","Grace Hopper","Kevin Mitnick","Linus Torvalds","John Carmack","Christopher Zechhauser"]
    print("Answer with yes or no")
    for i in range(0,8):
        count1=1
        while count1==1:
            count1=0
            try:
                p=input(names[i]+"\n>> ").lower()
                if i!=7:
                    if p=='yes':
                        score+=1
                    elif p=='no':
                        continue
                    else:
                        err()
                        count1=1
                else:
                    score-=10
            except Exception as e:
                 err()
                 count1=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do your know what the insert key in your keyboard does?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=1
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do your know what scroll lock key on your keyboard does?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=3
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you not have a computer virus in the past 6 months?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=3
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you not need an Antivirus?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score-=5
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you encrypt your hard drive?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=4
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you have a home server?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=5
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you have a network switch?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue
    if x==1:
        count1=1
        while count1==1:
            count1=0
            try:
                x1=int(input("How many network switch has in your house: "))
                if x1>=0:
                    score=score+2*x1
                else:
                    err()
                    count1=1
            except Exception as e:
                err()
                count1=1
    elif x==2:
        score-=1
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever edited the Windows regitry?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=5
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Can you write a 'Hello World' program in any programming languages?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=5
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever spend more than 1/3rd of your monthly income on a computer part?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=5
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you know about Google Ultron?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=3
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("How many extra web browser you have installed: ?")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x>=0:
        score=score+x
    elif x<0:
        err()
        count=1
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever made your own ethernet cable(RJ45 )?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=8
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever installed a custom firmware on your router?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=10
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever resized a drive partition?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=10
    elif x==2:
        continue
    else:
        err()
        count=1




clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Have you ever used SSH to remotely access a computer ?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=10
    elif x==2:
        continue
    else:
        err()
        count=1



clear()
count=1
while count==1:
    count = 0
    clear()
    pattren()
    print("Do you use custom DNS server?")
    print("1- Yes")
    print("2- No")
    try:
        x=int(input(">> "))
    except Exception as e:
        err()
        count=1
        continue

    if x==1:
        score+=10
    elif x==2:
        continue
    else:
        err()
        count=1




# result

if score<0:
    print(Fore.RED+"You completely failed and I'm surprised you're even able to turn on the computer")
    print(Style.RESET_ALL)
elif score<19:
    print(Fore.YELLOW + "I'm sorry you're just illiterate but somehow still barely functional\n"
                        "You most likely just use your computer exclusively for Microsoft Office programs")
    print(Style.RESET_ALL)
elif score>=19 and score<=49:
    print(Fore.LIGHTMAGENTA_EX + "You're still a complete computer noob\nBut you most likely have used "
                     "computers enough to pick up some knowledge here and there\nBut you probably haven't gone out of"
                     "your way to learn anything more about them")
    print(Style.RESET_ALL)

elif score>49 and score<109:
    print(Fore.LIGHTGREEN_EX + "You can consider yourself a computer experts but you're wrong this "
                               "actually just above average\nIf you're at the higher end of this range you definitely have the"
                               "potential for becoming an expert with enough effort in time ")
    print(Style.RESET_ALL)
elif score>=109 and score<=139:
    print(Fore.GREEN+"you are definitely computer expert but maybe not professionally "
                     "chances are you picked up a lot of knowledge from spending countless hours sitting in front of "
                     "a monitor\nAt this point you're probably think you're sort of  computer genius so you "
                     "could probably get a low-level IT job with little to no training as long as you sound like "
                     "you know what you're doing")
    print(Style.RESET_ALL)
elif score>139:
    print(Fore.BLUE+"You are a computer God you're literally Steve Jobs reincarnate at this level you're either extremely"
                    " interested in computers have a professional comouter job\nOr you're a complete loser with "
                    "no social skills if you ever had to you could probably walk in off the street and get a pretty decent IT job anywhere and "
                    "with enough training to experience sysadmin job now obviously")
    print(Style.RESET_ALL)
else:
    print(Fore.LIGHTCYAN_EX+"OMG how you did it")
    print(Style.RESET_ALL)

pattren()
print("This was a very well developed scientific test of course it's extremely accurate ")
pattren()


input("\n\nPress any key to Exit....")














