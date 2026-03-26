import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('C:/Users/dell/Desktop/game-workshop/Py/User_Data.csv')
x=df.iloc[:,3:4]
y=df.iloc[:,4:5]
#print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)#Recommended 0.2/0.25
lr=LogisticRegression()
lr.fit(x_train,y_train)
#sal=int(input("Enter Salary:"))
y_pred=lr.predict(x_test)
print("======LR======")
print(f"Prediction is",y_pred)
acc=accuracy_score(y_pred,y_test)
print(f"Accuracy is",acc)
#Take sem 3 marks from users and predict sem 4 marks
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
#sal2=int(input("Enter Salary:"))
y_pred1=knn.predict([[150000]])
print("======KNN======")
print(f"Prediction is",y_pred1)
#sal3=int(input("Enter Salary:"))
print("======DT=======")
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_pred2=dt.predict([[150000]])
print(f"Prediction is",y_pred2)
