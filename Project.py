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
df=pd.read_csv('C:/Users/dell/Desktop/game-workshop/Py/diabetes_prediction_dataset.csv')
x=df.iloc[:,0:8]
y=df.iloc[:,8:9]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
