
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd     # package for data analysis
import numpy as np      # package for numerical computations
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# to ignore warnings
import warnings
warnings.filterwarnings('ignore')

# In read_csv() function, we have passed the location to where the file is located at dphi official github page
loan_data  = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_train.csv" )

loan_data1 = loan_data.dropna(subset=['LoanAmount', 'Loan_Amount_Term', 'Credit_History'])

loan_data1['Gender'].fillna('Not Specified', inplace = True)

loan_data1['Married'].fillna('Not Specified', inplace = True)

loan_data1['Dependents'].fillna(loan_data1['Dependents'].mode()[0], inplace = True)

loan_data1['Self_Employed'].fillna('Not Specified', inplace = True)

# Drop irrelevant columns - Ticket and Name (may be passenger ID too - if not set it as index)
del loan_data1['Unnamed: 0']
del loan_data1['Loan_ID']

loan_data1 = pd.get_dummies(loan_data1, columns=['Gender'])
loan_data1 = pd.get_dummies(loan_data1, columns=['Married'])
loan_data1 = pd.get_dummies(loan_data1, columns=['Dependents'])
loan_data1 = pd.get_dummies(loan_data1, columns=['Education'])
loan_data1 = pd.get_dummies(loan_data1, columns=['Self_Employed'])
loan_data1 = pd.get_dummies(loan_data1, columns=['Property_Area'])

X = loan_data1.drop('Loan_Status', axis = 1)              # Input Variables/features
y = loan_data1.Loan_Status                                # output variables/features

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

rf = RandomForestClassifier(random_state=1, n_estimators=1000, max_depth=5)
 
rf.fit(X_train, y_train)

pickle.dump(rf, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))

print(model.predict([[4000, 2000.0, 120.0, 360.0, 1.0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0]]))
