def calc_compound_interest(p, r, t, n):
    # Converting annual interest rate from percentage to decimal
    r = r/100

    A = p * (1 + r/n) ** (n*t)
    return A


# Test the function
principal = 1000  # Principal amount
annual_rate = 5  # Annual interest rate in percentage
time_period = 10  # Time period in years
compounds_per_year = 4  # Number of times interest is compounded per year

amount = calc_compound_interest(principal, annual_rate, time_period, compounds_per_year)
compound_interest = amount - principal

print(f"The amount after {time_period} yrs is: {amount:.2f}")
print(f"The compound interest after {time_period} years is: {compound_interest:.2f}")