from flask import Flask, request, jsonify, render_template
import server.util as util  #replace this by import util for running locally

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/get_gender_type', methods=['GET'])
def get_gender_type():
    response = jsonify({
        'genders': util.get_gender_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_married_type', methods=['GET'])
def get_married_type():
    response = jsonify({
        'married': util.get_married_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_dependents_type', methods=['GET'])
def get_dependents_type():
    response = jsonify({
        'ependents': util.get_dependents_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_education_type', methods=['GET'])
def get_education_type():
    response = jsonify({
        'education': util.get_education_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_employment_type', methods=['GET'])
def get_employment_type():
    response = jsonify({
        'employment': util.get_employment_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_property_type', methods=['GET'])
def get_property_type():
    response = jsonify({
        'property': util.get_property_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_loan_or_non_loan', methods=['POST'])
def predict_loan_or_non_loan():
    applicant_income = int(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = float(request.form['credit_history'])
    gender = request.form['gender']
    married = request.form['married']
    dependents = request.form['dependents']
    education = request.form['education']
    employment = request.form['employment']
    property = request.form['property']

    response = jsonify({
        'loan_or_no_loan': util.get_loan_or_no_loan(applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,gender,married,dependents,education,employment,property)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Loan or NonLoan Prediction...")
    app.run()
