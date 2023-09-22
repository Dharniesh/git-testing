def calculate_outstanding_balance(loan_current_outstanding_balance, series_currency):
    return loan_current_outstanding_balance * series_currency
def calculate_loan_disbursement_amount(loan_total_disbursed_amount, series_currency):
    return loan_total_disbursed_amount * series_currency
def check_loan_eligibility(loan_delinquency_status, loan_current_outstanding_balance):
    if loan_delinquency_status > 6 or loan_current_outstanding_balance == 0:
        return "Ineligible"
    else:
        return "Eligible
def calculate_loan_result(loan_delinquency_status):
    return loan_delinquency_status * 30 if loan_delinquency_status > 0 else 0
def check_loan_status(loan_current_outstanding_balance, loan_delinquency_status):
    if loan_current_outstanding_balance == 0:
        return "Settled"
    elif loan_delinquency_status > 6:
        return "Defaulted"
    else:
        return "Live"
def calculate_loan_status(Snapshot_Date, Days_Past_Due):
    if "Status of Loan" == "Defaulted":
        return Snapshot_Date - Days_Past_Due + 180
    else:
        return ""
def calculate_payment(loan_current_outstanding_balance, series_currency):
    return loan_current_outstanding_balance * series_currency
def check_loan_delinquency_status(loan_delinquency_status):
    if loan_delinquency_status < 0:
        return loan_delinquency_status
    else:
        return 0
def calculate_remaining_loan_term(original_loan_term, loan_months_on_book, Payments_Ahead):
    return original_loan_term - loan_months_on_book + Payments_Ahead
