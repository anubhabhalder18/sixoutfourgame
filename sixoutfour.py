'''
Author-anubhabanubhab92

created on 12-11-2022

'''


import random
choice=["six","out","four"]
mode=0


def toss():
    a=int(input("Enter 1 for head 0 for toss"))
    t=random.randint(0,1)
    print("coin>>",t)
    if(a==t):
        mode=int(input("Enter 0 for bowling first 1 for batting"))
    else:
        mode=random.randint(0,1)
        if(mode==0):
            print("PC chose to bat first")
        if(mode==1):
            print("PC chose to bowl first")

toss()
        




target=0
i=0
innings=0
pc_run=0
user_run=0
wickets=3
overs=10

def print_score(pc):
    global mode,i
    print("pc>> ",pc)
    print("target\t",target)
    if(mode==1):
        print("User batting\n","User run\t",user_run,"Wickets",3-wickets)
        print("balls left",overs*6-i)

    if(mode==0):
        print("PC batting\n","User run\t",pc_run,"Wickets",3-wickets)
        print("balls left",overs*6-i)

def pc_batting(input):
    global wickets,pc_run,i
    pc=random.choice(choice)
    if(input==pc):
        wickets+=-1
    elif(pc=="out"):
        pc_run+=0
    elif(pc=="six"):
        pc_run+=6
    elif(pc=="four"):
        pc_run+=4
    else:
        print("Invalid input")
    print_score(pc)

def user_batting(input):
    global wickets,user_run,i
    pc=random.choice(choice)
    if(input==pc):
        wickets+=-1
        i+=1
    elif(input=="out"):
        user_run+=0
        i+=1
    elif(input=="six"):
        user_run+=6
        i+=1
    elif(input=="four"):
        user_run+=4
        i+=1
    else:
        print("Invalid input enter again ")
    print_score(pc)

def rc(text):
    try:
        if(text=="a"):
            a="six"
        elif(text=="b"):
            a= "four"
        elif(text=="c"):
            a= "out"
        return a
    except:
        print("invalid input")

if(wickets==0):
    if(mode==1):
        mode=0
        i=0
        target=user_run
    if(mode==0):
        mode=1
        i=0
        target=pc_run
    innings+=1
    wickets=3
if(i==60):
    if(mode==1):
        mode=0
        i=0
        target=user_run
    if(mode==0):
        mode=1
        i=0
        target=pc_run
    innings+=1
    wickets=3

if (mode==1):
    i=0
    while(i<overs*6):
        user=input("Enter a for six b for four c for out\t")
        user_batting(rc(user))

if (mode==0):
    i=0
    while(i<overs*6):
        user=input("Enter a for six b for four c for out\t")
        pc_batting(rc(user))


    
