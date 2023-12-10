import random
def display(boxes):
    count=0
    for i,x in enumerate(boxes):
        if count<2:
            print(x,"|",end=" "),
            count+=1
        elif count==2:
            print(x)
            count=0        
            if(i<7):
                print("---------")

def user_input(boxes,count):
    try:
        if count<4:
            choice=int(input("\nYour Turn.Enter your choice: "))
            if choice>0 and choice<10 and boxes[choice-1]==str(choice):
                int(choice)
                boxes[choice-1]="X"
                count+=1
                print("\nComputer's Turn.\n")
                winning(boxes,count)
            else:
                print("Invalid Input!")
                user_input(boxes,count) 
        else:
            for i,x in enumerate(boxes):
                if x==str(i+1):
                    boxes[i]="X"
            print("\nYour Turn\n")        
            display(boxes)        
            print("\nMatch Draw.")
    except ValueError:
        print("Invalid Input!")
        user_input(boxes,count)        

def winning(boxes,count):
    symbol1="O"
    symbol2="O"
    flag=row_search(boxes,symbol1,symbol2)
    if flag==1:
        display(boxes)
        print("\nComputer Wins!!\nGame Over.")
        exit(0)
    else:
        flag=col_search(boxes,symbol1,symbol2)
        if flag==1:
            display(boxes)
            print("\nComputer Wins!!\nGame Over.")
            exit(0)
        else:
            flag=diag_search(boxes,symbol1,symbol2)  
            if flag==1:
                display(boxes)
                print("\nComputer Wins!!\nGame Over.")
                exit(0)
            else:
                blocking(boxes,count)    

def blocking(boxes,count):
    symbol1="X"
    symbol2="O"
    flag=row_search(boxes,symbol1,symbol2)
    if flag==1:
        display(boxes)
        user_input(boxes,count)
    else:
        flag=col_search(boxes,symbol1,symbol2)
        if flag==1:
            display(boxes)
            user_input(boxes,count)
        else:
            flag=diag_search(boxes,symbol1,symbol2)  
            if flag==1:
                display(boxes)
                user_input(boxes,count)
            else:
                stategy(boxes,count)

def stategy(boxes,count):
        if boxes[4]=="5":
            boxes[4]="O"
        elif boxes[0]=="1" or boxes[2]=="3" or boxes[6]=="7" or boxes[8]=="9":
            flag=0
            while flag==0:
                r=random.randint(0,8)
                if r==0 or r==2 or r==6 or r==8:
                    comp_choice=r
                    if(boxes[comp_choice]!=str(comp_choice+1)):
                        flag=0   
                    else:
                        flag=1 
            boxes[comp_choice]="O"   
        else:    
            flag=0
            while flag==0:
                comp_choice=random.randint(1,9)
                if(boxes[comp_choice-1]!=str(comp_choice)):
                    flag=0   
                else:
                    int(comp_choice)
                    flag=1 
            boxes[comp_choice-1]="O"   
        display(boxes)    
        user_input(boxes,count)         

def row_search(boxes,symbol1,symbol2):
    i=0
    flag=0
    while(i<9 and flag==0):
        if boxes[i]==boxes[i+1]==symbol1 and boxes[i+2]==str(i+3):
            boxes[i+2]=symbol2
            flag=1
        elif boxes[i+1]==boxes[i+2]==symbol1 and boxes[i]==str(i+1):
            boxes[i]=symbol2
            flag=1
        elif boxes[i]==boxes[i+2]==symbol1 and boxes[i+1]==str(i+2):
            boxes[i+1]=symbol2
            flag=1
        else:
            i+=3    
    return flag    

def col_search(boxes,symbol1,symbol2):
    i=0
    flag=0
    while(i<3 and flag==0):
        if boxes[i]==boxes[i+3]==symbol1 and boxes[i+6]==str(i+7):
            boxes[i+6]=symbol2
            flag=1
        elif boxes[i+3]==boxes[i+6]==symbol1 and boxes[i]==str(i+1):
            boxes[i]=symbol2
            flag=1
        elif boxes[i]==boxes[i+6]==symbol1 and boxes[i+3]==str(i+4):
            boxes[i+3]=symbol2
            flag=1
        else:
            i+=1    
    return flag    

def diag_search(boxes,symbol1,symbol2):
    i=0
    flag=0
    if i==0 and flag==0:
        if boxes[i]==boxes[i+4]==symbol1 and boxes[i+8]==str(i+9):
            boxes[i+8]=symbol2
            flag=1
        elif boxes[i+4]==boxes[i+8]==symbol1 and boxes[i]==str(i+1):
            boxes[i]=symbol2
            flag=1
        elif boxes[i]==boxes[i+8]==symbol1 and boxes[i+4]==str(i+5):
            boxes[i+4]=symbol2
            flag=1
        else:
            i+=2   
    if i==2 and flag==0:
        if boxes[i]==boxes[i+2]==symbol1 and boxes[i+4]==str(i+5):
            boxes[i+4]=symbol2
            flag=1
        elif boxes[i+2]==boxes[i+4]==symbol1 and boxes[i]==str(i+1):
            boxes[i]=symbol2
            flag=1
        elif boxes[i]==boxes[i+4]==symbol1 and boxes[i+2]==str(i+3):
            boxes[i+2]=symbol2
            flag=1
    return flag    



boxes=["1","2","3","4","5","6","7","8","9"]
print("\nTIC-TAC-TOE\n")
display(boxes)
count=0
user_input(boxes,count)