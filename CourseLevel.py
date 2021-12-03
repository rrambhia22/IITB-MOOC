import pandas as pd
import numpy as np
import csv

writeheader=True
writeheader1=True
writeheader2=True
writeheader3=True
writeheader4=True
writeheader5=True



File1=pd.read_csv("Week1CSV.csv", encoding="ISO-8859-1")
a=File1.iloc[:,0].values #week1authorid
b=File1.iloc[:,1].values #week1count

File2=pd.read_csv("Week2CSV.csv", encoding="ISO-8859-1")
c=File2.iloc[:,0].values #week2authorid
d=File2.iloc[:,1].values #week2count

File3=pd.read_csv("Week3CSV.csv", encoding="ISO-8859-1")
e=File3.iloc[:,0].values #week3authorid
f=File3.iloc[:,1].values #week3count

File4=pd.read_csv("Week4CSV.csv", encoding="ISO-8859-1")
g=File4.iloc[:,0].values #week4authorid
h=File4.iloc[:,1].values #week4count

File5=pd.read_csv("Week5CSV.csv", encoding="ISO-8859-1")
i=File5.iloc[:,0].values #week5authorid
j=File5.iloc[:,1].values #week5count

File6=pd.read_csv("Week6CSV.csv", encoding="ISO-8859-1")
k=File6.iloc[:,0].values #week6authorid
l=File6.iloc[:,1].values #week6count


for z in range (len(a)):    #WEEEK1

    R=c1=c2=c3=c5=c7=c9=0
    c2=b[z]
    
    for y in range (len(c)):
        
        if a[z]==c[y]:
            c1=d[y]
    
    for x in range (len(e)):
        
        if a[z]==e[x]:
            c3=f[x]
    
    for w in range (len(g)):
        
        if a[z]==g[w]:
            c5=h[w]
    
    for v in range (len(i)):
        
        if a[z]==i[v]:
            c7=j[v]
    
    for u in range (len(k)):
        
        if a[z]==k[u]:
            c9=l[u]
    
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",a[z],"Count is",R)
    data={'Checked AuthorID':[a[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader is True:
        df.to_csv("Week1CourseCount.csv", mode="a", header=True, index=False)
        writeheader=False
    else:
        df.to_csv("Week1CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK1








for z in range (len(c)):     #WEEK2

    R=c1=c2=c3=c5=c7=c9=0
    c2=d[z]
   
     
    for y in range (len(a)):
        
        if c[z]==a[y]:
            c1=b[y]
            
                     
    for x in range (len(e)):
        if c[z]==e[x]:
            c3=f[x]
            
                     
    for w in range (len(g)):                     
        if c[z]==g[w]:
            c5=h[w]

    for v in range (len(i)):
        
        if c[z]==i[v]:
            c7=j[v]
            
                     
    for u in range (len(k)):
        
        if c[z]==k[u]:
            c9=l[u]
            
                     
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",c[z],"Count is",R)
    
    data={'Checked AuthorID':[c[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader1 is True:
        df.to_csv("Week2CourseCount.csv", mode="a", header=True, index=False)
        writeheader1=False
    else:
        df.to_csv("Week2CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK2







for z in range (len(e)):     #WEEK3

    R=c1=c2=c3=c5=c7=c9=0
    c2=f[z]
    
     
    for y in range (len(a)):
        
        if e[z]==a[y]:
            c1=b[y]
            
                     
    for x in range (len(c)):
        if e[z]==c[x]:
            c3=d[x]
            
                     
    for w in range (len(g)):                     
        if e[z]==g[w]:
            c5=h[w]

    for v in range (len(i)):
        
        if e[z]==i[v]:
            c7=j[v]
         
                     
    for u in range (len(k)):
        
        if e[z]==k[u]:
            c9=l[u]
            
                     
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",c[z],"Count is",R)
    
    data={'Checked AuthorID':[e[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader2 is True:
        df.to_csv("Week3CourseCount.csv", mode="a", header=True, index=False)
        writeheader2=False
    else:
        df.to_csv("Week3CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK3









for z in range (len(g)):     #WEEK4

    R=c1=c2=c3=c5=c7=c9=0
    c2=h[z]
    
     
    for y in range (len(a)):
        
        if g[z]==a[y]:
            c1=b[y]
            
                     
    for x in range (len(c)):
        if g[z]==c[x]:
            c3=d[x]
            
                     
    for w in range (len(e)):                     
        if g[z]==e[w]:
            c5=f[w]

    for v in range (len(i)):
        
        if g[z]==i[v]:
            c7=j[v]
         
                     
    for u in range (len(k)):
        
        if g[z]==k[u]:
            c9=l[u]
            
                     
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",c[z],"Count is",R)
    
    data={'Checked AuthorID':[g[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader3 is True:
        df.to_csv("Week4CourseCount.csv", mode="a", header=True, index=False)
        writeheader3=False
    else:
        df.to_csv("Week4CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK4










for z in range (len(i)):     #WEEK5

    R=c1=c2=c3=c5=c7=c9=0
    c2=j[z]
    
     
    for y in range (len(a)):
        
        if i[z]==a[y]:
            c1=b[y]
            
                     
    for x in range (len(c)):
        if i[z]==c[x]:
            c3=d[x]
            
                     
    for w in range (len(e)):                     
        if i[z]==e[w]:
            c5=f[w]

    for v in range (len(g)):
        
        if i[z]==g[v]:
            c7=h[v]
         
                     
    for u in range (len(k)):
        
        if i[z]==k[u]:
            c9=l[u]
            
                     
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",c[z],"Count is",R)
    
    data={'Checked AuthorID':[i[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader4 is True:
        df.to_csv("Week5CourseCount.csv", mode="a", header=True, index=False)
        writeheader4=False
    else:
        df.to_csv("Week5CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK5








for z in range (len(k)):     #WEEK6

    R=c1=c2=c3=c5=c7=c9=0
    c2=l[z]
    
     
    for y in range (len(a)):
        
        if k[z]==a[y]:
            c1=b[y]
            
                     
    for x in range (len(c)):
        if k[z]==c[x]:
            c3=d[x]
            
                     
    for w in range (len(e)):                     
        if k[z]==e[w]:
            c5=f[w]

    for v in range (len(g)):
        
        if k[z]==g[v]:
            c7=h[v]
         
                     
    for u in range (len(i)):
        
        if k[z]==i[u]:
            c9=j[u]
            
                     
    R=c1+c2+c3+c5+c7+c9
    
    #print("Authorid is",c[z],"Count is",R)
    
    data={'Checked AuthorID':[k[z]],'Total Count':[R]}
    df=pd.DataFrame(data)

    if writeheader5 is True:
        df.to_csv("Week6CourseCount.csv", mode="a", header=True, index=False)
        writeheader5=False
    else:
        df.to_csv("Week6CourseCount.csv", mode="a", header=False, index=False)   #END OF WEEK6

