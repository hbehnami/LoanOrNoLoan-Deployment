function onClickedLoanOrNoLoan() {
  console.log("Loan Or No Loan button clicked");
  var applInc = document.getElementById("app_income");
  var coapplInc = document.getElementById("coapp_income");
  var loanval = document.getElementById("loan_amount");
  var loanvalterm = document.getElementById("loan_amount_term");
  var credithis = document.getElementById("credit_hist");
  var gender = document.getElementById("uiGenders");
  var married = document.getElementById("uiMarrieds");
  var dependents = document.getElementById("uiDependents");
  var education = document.getElementById("uiEducations");
  var employment = document.getElementById("uiEmployments");
  var property = document.getElementById("uiProperties");
  var loanornot = document.getElementById("uiLoanOrNoLoan");
  var url = "http://127.0.0.1:5000/predict_loan_or_non_loan";

  $.post(
    url,
    {
      applicant_income: applInc.value,
      coapplicant_income: coapplInc.value,
      loan_amount: loanval.value,
      loan_amount_term: loanvalterm.value,
      credit_history: credithis.value,
      gender: gender.value,
      married: married.value,
      dependents: dependents.value,
      education: education.value,
      employment: employment.value,
      property: property.value,
    },
    function (data, status) {
      console.log(data.loan_or_no_loan);
      loanornot.innerHTML =
      "<h2>" + data.loan_or_no_loan.toString() + " Lakh</h2>";
      console.log(status);
    }
  );
}
