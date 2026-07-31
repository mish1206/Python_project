import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('C:/Users/dell/Desktop/game-workshop/Py/diabetes_prediction_dataset.csv')
le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
df["smoking_history"] = le.fit_transform(df["smoking_history"])
x=df.iloc[:,0:8]
y=df.iloc[:,8:9]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
while True:
    print("Enter details of the pateint:")
    while True:
        try:
            gen = int(input("Enter Gender [Male-1/Female-0]: "))
            if gen in [0, 1]:
                break
            else:
                print("Enter only 0 or 1")
        except:
            print("Invalid input")
    while True:
        try:
            age=int(input("Enter Age: "))
            if 0 < age < 120:
                break
            else:
                print("Enter valid age")
        except:
            print("Invalid input")
    hype_ten=int(input("Do you have Hypertension? [Yes-1/No-0]: "))
    heart_dis=int(input("Do you have Heart Disease? [Yes-1/No-0]: "))
    while True:
        try:
            smoke=int(input("Do you have Smoking History?[No Info-0/current-1/ever-2/former-3/never-4/not current-5]: "))
            if smoke in [0,1,2,3,4,5]:
                break
            else:
                print("Enter value between 0–5")
        except:
            print("Invalid input")
    while True:
        try:
            bmi = float(input("Enter BMI: "))
            if 10 < bmi < 60:
                break
            else:
                print("Enter realistic BMI")
        except:
            print("Invalid input")
    while True:
        try:
            hbac1 = float(input("Enter HbA1c: "))
            if 3 < hbac1 < 15:
                break
            else:
                print("Enter valid HbA1c")
        except:
            print("Invalid input")
    while True:
        try:
            glu_lvl = int(input("Enter Glucose Level: "))
            if 50 <= glu_lvl <= 300:
                break
            else:
                print("Enter realistic glucose value (50–300)")
        except:
            print("Invalid input")
        
    new_data = [[gen, age, hype_ten, heart_dis, smoke, bmi, hbac1, glu_lvl]]

    dt_model = DecisionTreeClassifier()
    rf_model = RandomForestClassifier()

    dt_model.fit(x_train, y_train)
    rf_model.fit(x_train, y_train)

    dt_pred = dt_model.predict(new_data)
    rf_pred = rf_model.predict(new_data)

    dt_acc = accuracy_score(y_test, dt_model.predict(x_test))
    rf_acc = accuracy_score(y_test, rf_model.predict(x_test))

    print("\nDecision Tree Accuracy:", dt_acc)
    print("Random Forest Accuracy:", rf_acc)

    print("\nDecision Tree Prediction:", "Diabetic" if dt_pred[0] == 1 else "Not Diabetic")
    print("Random Forest Prediction:", "Diabetic" if rf_pred[0] == 1 else "Not Diabetic")

    ch = input("\nDo you want to continue? (y/n): ")
    if ch.lower() != 'y':
        break
