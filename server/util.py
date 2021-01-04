import pickle
import json
import numpy as np
import os

__genders = None
__married = None
__dependents = None
__education = None
__employment = None
__property = None

__data_columns = None
__model = None

def get_loan_or_no_loan(applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,
                        gender,married,dependents,education, employment,property):
    try:
        gender_index = __data_columns.index(gender.lower())
    except:
        gender_index = -1

    try:
        married_index = __data_columns.index(married.lower())
    except:
        married_index = -1

    try:
        dependents_index = __data_columns.index(dependents.lower())
    except:
        dependents_index = -1

    try:
        education_index = __data_columns.index(education.lower())
    except:
        education_index = -1

    try:
        employment_index = __data_columns.index(employment.lower())
    except:
        employment_index = -1

    try:
        property_index = __data_columns.index(property.lower())
    except:
        property_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = applicant_income
    x[1] = coapplicant_income
    x[2] = loan_amount
    x[3] = loan_amount_term
    x[4] = credit_history

    if gender_index>=0:
        x[gender_index] = 1

    if married_index>=0:
        x[married_index] = 1

    if dependents_index>=0:
        x[dependents_index] = 1

    if education_index>=0:
        x[education_index] = 1

    if employment_index>=0:
        x[employment_index] = 1

    if property_index>=0:
        x[property_index] = 1
    return float(__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __genders
    global __married
    global __dependents
    global __education
    global __employment
    global __property

    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts"),

    with open(artifacts[0]+"/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __genders = __data_columns[5:8]  # first 5 columns are "applicantincome", "coapplicantincome", "loanamount", "loan_amount_term", "credit_history"
        __married = __data_columns[8:11]
        __dependents = __data_columns[11:15]
        __education = __data_columns[15:17]
        __employment = __data_columns[17:20]
        __property = __data_columns[20:23]

    global __model
    if __model is None:
        with open(artifacts[0]+"/model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns

load_saved_artifacts()
