from numpy.random import pareto, randint
import pandas as pd
import numpy as np
import sys
import random
import time
def fitness(population,duration,movies):
    limit=0
    value=0
    for i in range(len(population)):
        if population[i]==1:
            limit+=movies[i][1]
            value+=movies[i][-1]
        if limit>duration:
            return 0
    return value 
def selection(population,duration,movies):
    v={}
    b=[]
    for j in range(len(population)):
        v[j]=fitness(population[j],duration,movies)
        b.append(v[j])
    b.sort()
    max1=b[-1]
    max2=b[-2]
    x=sys.maxsize
    y=sys.maxsize
    for j in v.keys():
        if v[j]==max1:
            x=j
        if v[j]==max2:
            y=j 
    return population[x],population[y]
def crossover(genome1,genome2,population):
    x=randint(1,len(genome1))
    if len(genome1)<2:
        return genome1,genome2
    return list(genome1[:x])+list(genome2[x:]),list(genome2[:x])+list(genome1[x:])
def mutation(genome):
    probability=0.5
    for j in range(len(genome)):
        index=random.randrange(0,len(genome))
        if random.random()>probability:
            pass
        else:
            if genome[index]==1:
                genome[index]=0
            else:
                genome[index]=1
    return genome
def run(limit,movies,generation_limit,duration,population):
    for j in range(generation_limit):
        population=sorted(population,key=lambda x:fitness(x,duration,movies),reverse=True)
        if fitness(population[0],duration,movies)>=limit:
            break
        next_gen=population[:2]
        for k in range(len(population)//2-1):
            parents=selection(population,duration,movies)
            a,b=crossover(parents[0],parents[1],population)
            a=mutation(a)
            b=mutation(b)
            next_gen+=[a,b]
        population=next_gen
    population=sorted(population,key=lambda x:fitness(x,duration,movies),reverse=True)        
    return population,j        
#start
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
X=int(input("Enter the size of genome: "))
t=int(input('Enter the fitness limit: '))
movies=m[:X]
population=[]
gen=int(input('Enter Generations: ')) 
population_size=int(input('Enter Population size: '))
a=time.time()
for i in range(population_size):
    x=np.random.choice([0, 1], size=len(movies))
    population.append(x)
best_ans,generations=run(t,movies,gen,duration,population)
movies_list=[]
for j in range(len(best_ans[0])):
    if best_ans[0][j]==1:
        movies_list.append(movies[j])
b=time.time()       
print(f'The number of generations is {generations}')
print("your list : "+f'{movies_list}')        
print("time taken : "+f'{b-a}')



        
