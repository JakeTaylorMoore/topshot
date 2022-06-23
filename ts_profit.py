# Author:      Jacob Moore
# Date:        5/26/22
# Description: Calculate profit based on downloadable csv file from NBA Topshot
#              Followed tutorial for csv library from:
#              https://www.geeksforgeeks.org/working-csv-files-python/

# importing csv module
import csv

# csv file name
filename = "topshot.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields += next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

#  find amounts
dapper_purchases = 0
purchase_fees = 0
sales = 0
withdrawal = 0
withdrawal_fees = 0
adjustments = 0
purchases = 0
print('\nSaving important data\n')
for i in range(len(rows) - 1):
    if rows[i][0] == "Dapper purchase":
        dapper_purchases += float(rows[i][2])
        purchase_fees += float(rows[i][3])
    elif rows[i][0] == "NBA Top Shot sale":
        sales += float(rows[i][2])
    elif rows[i][0] == "Dapper withdrawal":
        withdrawal += float(rows[i][2])
        withdrawal_fees += float(rows[i][3])
    elif rows[i][0] == "Dapper adjustment":
        adjustments += float(rows[i][2])
    elif rows[i][0] == "NBA Top Shot purchase":
        purchases += float(rows[i][2])
print('\n')
print('purchases: ' + str(dapper_purchases))
print('purchase_fees: ' + str(purchase_fees))
print('sales: ' + str(sales))
print('withdrawal: ' + str(withdrawal))
print('withdrawal_fees: ' + str(withdrawal_fees))
print('adjustments: ' + str(adjustments))
print('purchases: ' + str(purchases))

print('\n')
spent = (dapper_purchases + purchase_fees + withdrawal_fees) - (withdrawal + adjustments)
print('spent: ' + str(spent))
