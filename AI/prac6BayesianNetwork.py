def Joint_Distribution(S,D,A,B,F,Sophia,David,Alarm,Burglary,Fire):
    for s in Sophia:
        if(s[0]==A and s[1]==S):
            m=s[2] 
            break
    for d in David:
        if(d[0]==A and d[1]==D):
            n=d[2]
            break
    for a in Alarm:
        if(a[0]==B and a[1]==F and a[2]==A):
            o=a[3]
            break
    for b in Burglary:
        if(b[0]==B):
            p=b[1]
            break        
    for f in Fire:
        if(f[0]==F):
            q=f[1]
            break

    return m*n*o*p*q                        

Burglary=[["T",0.002],["F",0.998]]
Fire=[["T",0.001],["F",0.999]]
#[burglary,fire,alarm,prob]
Alarm=[
    ["T","T","T",0.94],
    ["T","T","F",0.06],
    ["T","F","T",0.95],
    ["T","F","F",0.05],
    ["F","T","T",0.31],
    ["F","T","F",0.69],
    ["F","F","T",0.001],
    ["F","F","F",0.999]]
#[alarm,call,prob]
David=[
    ["T","T",0.91],
    ["T","F",0.09],
    ["F","T",0.05],
    ["F","F",0.95]]
Sophia=[
    ["T","T",0.75],
    ["T","F",0.25],
    ["F","T",0.02],
    ["F","F",0.98]]

#[S,D,A,B,F]

for d in David:
    if(d[0]=="T" and d[1]=="T"):
        i=d[2]
        break
for a in Alarm:
    if(a[0]=="T" and a[2]=="T"):
        i*=a[3]
for b in Burglary:
    if(b[0]=="T"):
        b[0]=i
    else:
        b[0]==round(1-i,3)       

print("\nIf Alarm was triggered and David called then probability of happening of burglary will be:",round(i,3))

for a in Alarm:
    if(a[0]=="T" and a[1]=="T"):
        i=a[3]
for s in Sophia:
    if(s[0]=="T" and s[1]=="T"):
        i*=s[2]
for s in Sophia:
    if(s[0]=="T" and s[1]=="T"):
        s[2]=i
    elif(s[0]=="T" and s[1]=="F"):
        s[2]=round(1-i,3)    

print("\nIf Fire has occured and Alarm was triggered then probability of Sophia called is:",round(i,3),"\n")