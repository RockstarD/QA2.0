import pandas as pd
import numpy as np
#IMPORTING THE DATA SET AND REMOVING ANY NULL VALUES
df=pd.read_csv("math_dataset.csv",encoding='latin1')
df.dropna(how='any',inplace=True)
df.head()
df.shape
df.columns
# SETTING THE TARGET FUNCTION INTO X
x=df.iloc[:,1]
x
# ASSIGNING THE VALUES FROM 1 TO 7 TO EACH TOPIC
df.type.replace({'Counting & Probability':1,'Algebra':2,'Prealgebra':3,
                 'Geometry':4,'Precalculus':5,'Number Theory':6,'Intermediate Algebra':7})
# SPLITTING THE DATA INTO TRAINING AND TESTING
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.problem,df.type,test_size=0.25)
# CONVERTING THE STRING QUESTIOS INTO NUMBER MATRIX 
from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
x_train_count=v.fit_transform(x_train.values)
x_test_count=v.transform(x_test)
x_test_count.toarray()[:]

# PREPARING MODEL AND TRAINING IT
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train_count,y_train)

# GENERATING INPUT
a=['find the area of a square with side 8 cm.',
  'find the probaility of head in fliping a coin',
  'solve 3x^2 + 2x',
  'find the probability of drawing a card which is club',
  'What value of x^2 will give the minimum value for x^2- 14x + 3 ?',
  'Find the minimum value of the function f(x) = sqrt{-x^2 + 4x + 21} - sqrt{-x^2 + 3x + 10}.] ',
  'What is the sum of the three digit cubes that are the cubes of either squares or cubes?',
  'In how many ways can the letters of the word ''COPYRIGHT'' be arranged?',
  'Evaluate d/dx cos 99 ']
   
# PREDICTING THE INPUT
k=v.transform(a)
r=model.predict(k).tolist()
s=r
s

# ASSIGINING THE CHAPTER VALUES TO THE CHAPTERS
j=0;
for i in r:
    if i=='Counting & Probability':
        s[j]=1
    elif i=='Algebra':
        s[j]=2
    elif i=='Prealgebra':
        s[j]=3
    elif i=='Geometry':
        s[j]=4
    elif i=='Precalculus':
        s[j]=5
    elif i=='Number Theory':
        s[j]=6
    elif i=='Intermediate Algebra':
        s[j]=7
    j=j+1;  
   

s

# COUNTING FOR NUMBER OF QUESTIONS FROM EACH CHAPTER
chap=[1,2,3,4,5,6,7]
j=0
for i in chap:
    chap[j]=s.count(i)
    j=j+1
chap

model.score(x_test_count,y_test)

# CALCULATING CHAPTER WISE WEIGHTAGE OF THE PREDICTED RESULT
sum=0
for i in chap :
    sum+=i
    
p=0
for i in chap :
    
    chap[p]=(i/sum)*100
    p=p+1

topic={1:'Counting & Probability',2:'Algebra',3:'Prealgebra',4:'Geometry',5:'Precalculus',6:'Number Theory',7:'Intermediate Algebra'}
print('CHAPTER   WEIGHTAGE(%)  ')
for i in range(1,8):
    print(topic[i],'\t',chap[i-1])

# function to take input array from user and predict the chapter and weightage
def predictAnswer(question):


    k = v.transform(question)
    r = model.predict(k).tolist()
    s = r
    j = 0;
    for i in r:
        if i == 'Counting & Probability':
            s[j] = 1
        elif i == 'Algebra':
            s[j] = 2
        elif i == 'Prealgebra':
            s[j] = 3
        elif i == 'Geometry':
            s[j] = 4
        elif i == 'Precalculus':
            s[j] = 5
        elif i == 'Number Theory':
            s[j] = 6
        elif i == 'Intermediate Algebra':
            s[j] = 7
        j = j + 1;
    
    chap = [1, 2, 3, 4, 5, 6, 7]
    j = 0
    for i in chap:
        chap[j] = s.count(i)
        j = j + 1

    sum = 0
    for i in chap:
        sum += i    

    p = 0
    for i in chap:
        chap[p] = (i / sum) * 100
        p = p + 1

    topic = {1: 'Counting & Probability', 2: 'Algebra', 3: 'Prealgebra', 4: 'Geometry', 5: 'Precalculus', 6: 'Number Theory',
                7: 'Intermediate Algebra'}
    d = {}
    for i in range(1, 8):
        d[topic[i]] = chap[i - 1]
    return d


# print(predictAnswer(['find the area of a square with side 8 cm.',
#     'find the probaility of head in fliping a coin',
#     'solve 3x^2 + 2x',
# ]))
