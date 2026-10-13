import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

x= [[10000],[20000],[30000],[50000],[70000],[90000]]
y= [0,0,0,1,1,1]

modelo=DecisionTreeClassifier(random_state=42) 
modelo.fit(x,y)

prediction = modelo.predict([[80000]])

if prediction[0] == 1:
    print("El cliente puede comprar")
else:
    print("El cliente no podria comprar")
    
