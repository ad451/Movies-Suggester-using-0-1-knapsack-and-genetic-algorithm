import pandas as pd
import time
def knapsack(duration,wt,val,n,movies):
    dp=[[0 for i in range(duration+1)] for j in range(n+1)]
    for j in range(n+1):
        for w in range(duration+1):
            if j==0 or w==0:
                continue
            if wt[j-1]<=w:
                dp[j][w]=max(val[j-1]+dp[j-1][w-wt[j-1]],dp[j-1][w])
            else:
                dp[j][w]=dp[j-1][w]   
    l=[]
    i = n
    j = duration

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            l.append(movies[i-1])
            j = j - wt[i-1]
            i = i - 1
        else:
            i = i - 1
    return l
    
l=pd.read_csv('IMDb movies.csv',usecols = ['title','genre','avg_vote','duration'])
genre=input('please enter the genre : ')
duration=int(input('please enter the duration : '))
m=[]
count=0
for i in range(len(l['genre'])):
    if genre in l['genre'][i] and int(l['duration'][i])<=duration:
        count+=1
        m.append([l['title'][i],l['duration'][i],l['avg_vote'][i]])
m=sorted(m,key=lambda x: x[-1])
m.reverse()            
m=m[:10]
wt=[]
val=[]
a=time.time()
for j in m:
    wt.append(j[1])
    val.append(j[-1]) 
ans=knapsack(duration, wt, val, len(m),m)
b=time.time()
print("your list : "+f'{ans}')        
print("time taken : "+f'{b-a}')



