import numpy_financial as npf

def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
  """
  Author: Russel
  Calculates the monthly payment for a mortgage loan.

  Args:
    loan_amount: The principal amount of the loan.
    annual_interest_rate: The annual interest rate as a decimal (e.g., 0.065 for 6.5%).
    loan_term_years: The loan term in years.

  Returns:
    The monthly payment amount.
  """

  monthly_interest_rate = annual_interest_rate / 12
  total_number_of_payments = loan_term_years * 12

  monthly_payment = npf.pmt(monthly_interest_rate, total_number_of_payments, -loan_amount)

  return monthly_payment

# Example usage with the values from the image:
loan_amount = 402400
annual_interest_rate = 0.05499  # 5.499%
loan_term_years = 30

monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
print(f"{loan_amount} at {annual_interest_rate*100:.2f}% Monthly Payment: ${monthly_payment:.2f}")

# Additional examples with different interest rates:
loan_amount = 402400
annual_interest_rate = 0.065  # 6.5%
loan_term_years = 30

monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
print(f"{loan_amount} at {annual_interest_rate*100:.2f}% Monthly Payment: ${monthly_payment:.2f}")

loan_amount = 402400
annual_interest_rate = 0.0325  # 6.95%
loan_term_years = 30

monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
print(f"{loan_amount} at {annual_interest_rate*100:.2f}% Monthly Payment: ${monthly_payment:.2f}")

# Example with a different loan amount and term:
loan_amount = 420000
annual_interest_rate = 0.0695  # 4%
loan_term_years = 30

monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
print(f"{loan_amount} at {annual_interest_rate*100:.2f}% Monthly Payment: ${monthly_payment:.2f}")
