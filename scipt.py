import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data and expenes overview
financial_data = pd.read_csv('financial_data.csv')
expense_overview = pd.read_csv('expenses.csv')
employees = pd.read_csv('employees.csv')

# code goes here
print(financial_data.head())
print(expense_overview.head(7))
print(employees.head())

#Store each column in three separate variables called month, revenue, and expenses
month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

#plot revenue over the past six months with labels and formatting
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

#repeat with expenses using plt.clf()
plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

#Store the Expense column in a variable called expense_categories and the Proportion column in a variable called proportions
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout
plt.show()

#Update Expense Categories so that all categories make up less than 5% of the overall expenses (Equipment, Utilities, Supplies, and Food) are collapsed into an "Other" category
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = 'Salaries'

#Sort the employees dataframe in ascending order by the Productivity column
sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)

#Print the 100 least productive employees
employees_cut = sorted_productivity.head(100)
print(employees_cut)

transformation = 'standardization'

#Create a variable called commute_times that stores the Commute Time column
commute_times = employees['Commute Time']
commute_times_log = np.log(commute_times)
print(commute_times.describe())

plt.clf()
plt.hist(commute_times_log)
plt.title('Employee Commute Times')
plt.xlabel('Commute Time')
plt.ylabel('Frequency')
plt.show()
