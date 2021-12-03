import pandas as pd
import numpy as np 
import csv

File=pd.read_csv("WEEK 4.csv", encoding="ISO-8859-1")
x=File.iloc[:,0].values
r=File.iloc[:,3].values

final_list=[]
writeheader=True
writeheader1=True
writeheader2=True
writeheader3=True
writeheader4=True
writeheader5=True
writeheader6=True
writeheader7=True

for z in range (len(x)):
    if (x[z] not in final_list):
        final_list.append(x[z])

for i in range (len(final_list)):
    count=0
    for j in range (len(x)):
        if(x[j] == final_list[i]):
            count=count+1
    data={'Author_id':[final_list[i]],"Count":[count]}
    df=pd.DataFrame(data,[i+1])
    #print(df)
    if writeheader is True:
        df.to_csv("Count44.csv", mode="a", header=True, index=False)
        writeheader=False
    else:
        df.to_csv("Count44.csv", mode="a", header=False, index=False)




File1=pd.read_csv("Count44.csv" ,encoding="ISO-8859-1")
y=File1.iloc[:,0].values#countauthorid

for i in range(len(y)):
    s=[]
    l=[]
    countN=0
    countNC=0
    countL=0
    countB=0

    for j in range(len(x)):
        if(y[i] == x[j]):
            s.append(r[j])
            l=s
    data={'Author_id':[final_list[i]],'Non_Lxi':[s]}
    df=pd.DataFrame(data)

    if writeheader1 is True:
        df.to_csv("Non-Lxi44.csv", mode="a", header=True, index=False)
        writeheader1=False
    else:
        df.to_csv("Non-Lxi44.csv", mode="a", header=False, index=False)

    
    for k in range(len(l)):
        if(l[k]=='N'):
            countN=countN+1
        elif (l[k]=='NC'):
            countNC=countNC+1
        elif(l[k]=='LxI'):
            countL=countL+1
        elif(l[k]=='blank'):
            countB=countB+1
        else:
            break

    data={'Author_id':[final_list[i]],'CountN':[countN]}
    df=pd.DataFrame(data)

    if writeheader2 is True:
        df.to_csv("COUNT_N4.csv", mode="a", header=True, index=False)
        writeheader2=False
    else:
        df.to_csv("COUNT_N4.csv", mode="a", header=False, index=False)


    data={'Author_id':[final_list[i]],'CountNC':[countNC]}
    df=pd.DataFrame(data)

    if writeheader3 is True:
        df.to_csv("COUNT_NC4.csv", mode="a", header=True, index=False)
        writeheader3=False
    else:
        df.to_csv("COUNT_NC4.csv", mode="a", header=False, index=False)


    data={'Author_id':[final_list[i]],'CountLXI':[countL]}
    df=pd.DataFrame(data)

    if writeheader4 is True:
        df.to_csv("COUNT_LXI4.csv", mode="a", header=True, index=False)
        writeheader4=False
    else:
        df.to_csv("COUNT_LXI4.csv", mode="a", header=False, index=False)


    data={'Author_id':[final_list[i]],'CountBLANK':[countB]}
    df=pd.DataFrame(data)

    if writeheader5 is True:
        df.to_csv("COUNT_Blank4.csv", mode="a", header=True, index=False)
        writeheader5=False
    else:
        df.to_csv("COUNT_Blank4.csv", mode="a", header=False, index=False)

        
    for i in range(len(x)):
        q=[]
        if(countN>=1 and countNC>=1):
            #print("both")
            q.append("Both")
            break
        if(countN>=1):
            #print("thread comment")
            q.append("Thread Comment")
            break
        if(countNC>=1):
            #print("comment")
            q.append("Comment")
            break
        else:
            break
        
    #print("Count for authorid N",[final_list[i]],"is",countN)
    #print("Count for authorid NC",[final_list[i]],"is",countNC)
        
    data={'Author_id':[final_list[i]],'Behavior(N/NC)':[q]}
    df=pd.DataFrame(data)

    if writeheader6 is True:
        df.to_csv("BehaviorNNC4.csv", mode="a", header=True, index=False)
        writeheader6=False
    else:
        df.to_csv("BehaviorNNC4.csv", mode="a", header=False, index=False)



    for i in range(len(x)):
        c=[]
        if(countL>=1 and countB>=1):
            #print("both")
            c.append("Both")
            break
        if(countL>=1):
            #print("comment")
            c.append("Thread Starter")
            break
        if(countB>=1):
            #print("comment")
            c.append("Blank")
            break
        else:
            break
    
    data={'Author_id':[final_list[i]],'Behavior(Lxi/Blank)':[c]}
    df=pd.DataFrame(data)

    if writeheader7 is True:
        df.to_csv("BehaviorLXI4.csv", mode="a", header=True, index=False)
        writeheader7=False
    else:
        df.to_csv("BehaviorLXI4.csv", mode="a", header=False, index=False)
