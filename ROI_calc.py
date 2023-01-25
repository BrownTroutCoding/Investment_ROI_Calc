# Rental income property calculator written using Object Oriented Programming

class Calculator():

    def __init__(self, income, expenses, cashFlow, ROI):
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.ROI = ROI

    # 1: Income
    # total monthly income = income, laundry, storage, misc

    def calc_income(self):
        print("\nLets calculate your monthly income")
        prop_income = int(input("\nTo get started, enter your monthly property income: "))
        laundry = int(input("What did you make on laundry machines? "))
        storage = int(input("What did you make on storage? "))
        misc_income = int(input("Do you have any Misc profit (i.e. vending machines)? "))

        # Total monthly property income
        monthly_income = prop_income + laundry + storage + misc_income

        print(f"\nTotal monthly income = ${monthly_income}")
        self.income = monthly_income
    
    # 2: Expenses
    # Tax, Insurance, Utilities (electric, water, sewer, garbage, gas), HOA, lawn/snow care, vacancy, repairs
    # capital expenditures(CapEx putting money asside for a new roof), property management, mortgage.

    def calc_expenses(self):
        print("\nLets calculate your monthly expenses.")

        # Calculating utilities
        utilities = str(input("\nAre you responsible for some or all utilities? (yes, no) "))
        monthly_utilities = 0
        while utilities != 'yes' and utilities != 'no':
            utilities = input("Please enter 'yes' or 'no': ")

        if utilities == 'yes':
            electricity = int(input("How much do you pay monthly for electricity? "))
            water = int(input("How much do you pay monthly for water? "))
            sewage = int(input("How much do you pay monthly for sewage? "))
            garbage = int(input("How much do you pay monthly for garbage/recycling? "))
            gas = int(input("How much do you pay monthly for gas? "))
            monthly_utilities = electricity + water + sewage + garbage + gas
        elif utilities == 'no':
            print("\nGreat!Lets continue.")

        print(f"\n Total monthly utility costs = ${monthly_utilities}")

        tax = int(input("\nHow much do you pay monthly in property taxes? "))
        insurance = int(input("How much do you pay monthly in home insurance? "))
        HOA = int(input("How much do you pay monthly in HOA fees? "))
        prop_care = int(input("How much do you pay monthly for lawn care and or snow removal? "))
        vacancy = int(input("How much $ do you put aside each month, planning for future vacanies? "))
        repairs = int(input("How much do you pay monthly in property repairs? "))
        CapEx = int(input("How much $ do you put aside each month, planning for unforseen repairs? "))
        prop_mgmt = int(input("How much do you pay monthly for property management? "))
        mortgage = int(input("How much do you pay monthly for your mortgage? "))

        # Total monthly expenses
        monthly_expenses = tax + insurance + HOA + prop_care + vacancy + repairs + CapEx + prop_mgmt + mortgage + monthly_utilities
        self.expenses = monthly_expenses
        print(f"\nYour total monthly expenses = ${monthly_expenses}")
    
    # 3: Total Monthly Cash Flow = Monthly Income - Monthly Expenses
    # calculate annual cash flow as well
    def calc_cashFlow(self):
        self.cashFlow = self.income - self.expenses
        total_monthly_cashFlow = self.cashFlow
        annual_cashFlow = total_monthly_cashFlow * 12
        print(f"\nYour total monthly cash flow = ${total_monthly_cashFlow}")
        print(f"\nYour annual cash flow = ${annual_cashFlow}")
    

    # 4: Cash on Cash ROI (what percentage are you earning based on what you payed for property)
    # down payment, closing costs, repair/rehab budget, misc/other = total investment
    # Annual cash flow / totasl investment = Cash on cash ROI
    # Example: 9.36%
    def calc_ROI(self):
        print("\nLets calculate your cash on cash return on investment (ROI). This is the percentage of what you are earning based on what you invested into the property to purchase.")
        price = int(input("\nWhat is the price of the property? "))
        down_payment = int(input("How much do plan to pay for your down payment? "))
        repair_budget = int(input("How much do you have for a repair/renovation budget? "))
        misc_ROI = int(input("Do you have any MISC costs when purchasing?(i.e. attorney fees) "))
        calc_CC = str(input("Do you plan on splitting the closing costs with the seller? (yes, no) "))
        while calc_CC != 'yes' and calc_CC != 'no':
            calc_CC = input("Please enter 'yes' or 'no': ")
        if calc_CC == 'yes':
            print("In Montana, the average closing cost fees are 1.5 percent of the purchase price.")
            closing_amount = price * (1.5/100) / 2
            print(f"Therefore, your estimated closing costs = ~${closing_amount}")
        elif calc_CC == 'no':
            print("\nGreat! Lets continue.")
            
        closing_costs = closing_amount
        total_investment = down_payment + repair_budget + misc_ROI + closing_costs
        annual_cashFlow = self.cashFlow * 12
        ROI = 100 * (annual_cashFlow/total_investment)

        print("\nCash on cash return on investment (ROI) is a metric used to calculate the profitability of a rental property by taking the cash flow generated by the property and dividing it by the total cash invested in the property. It's expressed as a percentage and represents the return on the cash invested in the property, not including any appreciation or tax benefits.")

        print(f"\nYour monthly cash on cash return on investment = {round(ROI, 3)}%")

        print("\nDifferent investors will have different thresholds for what they consider to be a good cash on cash ROI. Generally, investors are looking for a return of at least 8-12 percent in order to make a property worth investing in. However, this threshold can vary depending on factors such as the overall economic conditions, the investor's own financial situation, and the specific characteristics of the property. It is also worth considering your other investments, and if this ROI is higher than others, it may be worth your time investing.")

# Creating an instance of the 'Calculator' class and assigning it to the variable 'Calc'.
# 'Calculator' takes 4 parameters, 'income', 'expenses', 'cashFlow', 'ROI'
Calc = Calculator(income=[], expenses=[], cashFlow=[], ROI=[])

# Run function
def run_calc():
    while True:
        print("\nWelcome to the Investment Rental (ROI) calculator created by Brown Trout Coding.")
        start = input("\nPlease enter 'start', to begin calculating your ROI. You may enter 'no' to exit the program: ")

        if start == 'start':
            Calc.calc_income()
            Calc.calc_expenses()
            Calc.calc_cashFlow()
            Calc.calc_ROI()
        elif start == 'no':
            print("\nThank you for using our investment calculator!")
            break

run_calc()