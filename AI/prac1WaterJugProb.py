def waterjug(x,y,target,initial_state):
    visited=set()
    queue=[(initial_state,[])]

    while queue:
        (a,b),path=queue.pop()

        if (a,b) in visited:
            continue

        visited.add((a,b))
        path=path+[(a,b)]

        if a==target:
            b=0
            path=path+[(a,b)]
            return path
        elif b==target:
            a=0
            path=path+[(a,b)]
            return path
            
        
        rules=[ 
            (x,b),       # Fill the first jug
            (a,y),       # Fill the second jug
            (0,b),                   # Empty the first jug
            (a,0),                   # Empty the second jug
            (a-min(a,y-b),b+min(a,y-b)),  # Pour from first to second jug
            (a+min(b,x-a),b-min(b,x-a))   # Pour from second to first jug
        ]

        queue.extend((r, path) for r in rules if r not in visited)
    
    return None    

def steps(x,y,result):
    flag=0
    for i,step in enumerate(result):
        if(step[0]==0 and step[1]==0):
            print(str(i+1)+". Initially both the jug are Empty.")
        elif(step[0]>=0 and step[1]==y and flag==0):
            print(str(i+1)+". Fill jug Y completely.")
            flag=1
        elif(step[0]==x and step[1]>=0 and flag==0):
            print(str(i+1)+". Fill jug X completely.")
            flag=1
        elif(step[0]==0 and step[1]%x==0 and flag==1):
            print(str(i+1)+". Pour water from jug X to Y.")
            flag=0  
        elif(step[0]%y==0 and step[1]==0 and flag==1):
            print(str(i+1)+". Pour water from jug Y to X.")       
            flag=0     
        elif(step[0]>0 and step[1]==y and flag==1):
            print(str(i+1)+". Pour water from jug X to Y.")          
            flag=0
        elif(step[0]==x and step[1]>0 and flag==1):
            print(str(i+1)+". Pour water from jug Y to X.")          
            flag=0
        elif(step[0]>0 and step[1]==0 and flag==0):
            print(str(i+1)+". Empty jug Y.")      
            flag=1      
        elif(step[0]==0 and step[1]>0 and flag==0):
            print(str(i+1)+". Empty jug X.")    
            flag=1        

x=int(input("Jug capacity of X = "))
y=int(input("Jug capacity of Y = "))
target=int(input("(Target should be less than equal to maximum of X and Y)\nTarget = "))
if target<0 or target>max(x,y):
    print("Invalid Input!")
else:
    initial_state=(0,0)
    result=waterjug(x,y,target,initial_state)
    if result:
        print("\nSteps to achieve the target:")
        steps(x,y,result)
        print("Target achieved!!\n\nWater in jug is shown by:")
        for s in result:
            print(s)
    else:
        print("The goal volume is not reachable.")