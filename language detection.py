import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# loading the dataset 
df=pd.read_csv("dataset.csv")
x=df['Text']
y=df['language']

#converting to numbers for computer to read

cvt=CountVectorizer()
X=cvt.fit_transform(x)

#splitting data for the evaluation of our model

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#model training
model=MultinomialNB()
model.fit(x_train, y_train)
score=model.score(x_test,y_test)
print(score)

#prediction
user_input=input("enter the text to predict: ")
x_user=cvt.transform([user_input]).toarray()
prediction=model.predict(x_user)
print(prediction)
