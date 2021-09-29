##########################################
# This code is created by Hesam Marshal  #
# Website : HesamMarshal.ir              #
# instagram: @HesamMarshal               #
##########################################
worked_years = int(input("Enter worked years: "))
salary = int(input("Enter Salary: "))

worked_days = worked_years * 365

reward = salary * 30 / 365 * worked_days
print(f"reward = {reward}")
