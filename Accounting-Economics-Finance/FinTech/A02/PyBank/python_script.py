# imports
import csv
from math import inf

# name initialization
num_months = 0                        # initialize the count: the number of months (the number of rows in the dataset)
months = []                           # intialize a list of the months (column 1 in the dataset)...
mo_changes = []                       # ...and a list of the monthly changes in profit (column 2 in the dataset)
max_gain = ['', -inf]                 # track the name and change in profit of the month which saw the greatest increase in profit
max_loss = ['', inf]                  # track the name and change in profit of the month which saw the greatest decrease in profit
net_profit = 0                        # track the net total profit

# read and process data
with open('budget_data.csv') as data_file:
    reader = csv.reader(data_file)
    next(reader)                      # get the header
    
    # setup iterative processing
    row1 = next(reader)               # get the first row of data
    num_months += 1                   # update the count
    curr_mo = int(row1[1])            # get the current month's profit
    net_profit += curr_mo             # update the net profit
    prev_mo = curr_mo                 # assign the current month's profit to the previous month's profit for the next iteration
    
    # iterative processing
    for row in reader:                # get the next row of data
        num_months += 1               # update the count
        curr_mo = int(row[1])         # get the current month's profit
        net_profit += curr_mo         # update the net profit
        mo_change = curr_mo - prev_mo # get the current month's change in profit
        mo_changes += [mo_change]     # append the current month's change in profit to the list of monthly changes in profit
        months += [row[0]]            # append the name of the current month to the list of the names of the months
        if mo_change > max_gain[1]:   # update the name and change in profit of the month which saw the greatest increase in profit
            max_gain[0], max_gain[1] = row[0], mo_change
        if mo_change < max_loss[1]:   # update the name and change in profit of the month which saw the greatest decrease in profit
            max_loss[0], max_loss[1] = row[0], mo_change
        prev_mo = curr_mo             # assign the current month's profit to the previous month's profit for the next iteration

# compute the average change in profit
avg_change = round(sum(mo_changes) / len(mo_changes), 2)

# format the analysis
lines = [
    'Financial Analysis',
    '-' * 30,
    '{:15}{:>15}'.format('Num Months', num_months),
    '{:15}{:>15}'.format('Net Profit', '{}${:.2f}'.format('-' if net_profit < 0 else ' ', abs(net_profit))),
    '{:15}{:>15}'.format('Avg Change', '{}${:.2f}'.format('-' if avg_change < 0 else ' ', abs(avg_change))),
    '{:15}{:>15}'.format('Max Gain', '{}${:.2f}'.format('-' if max_gain[1] < 0 else ' ', abs(max_gain[1]))),
    '{:15}{:>15}'.format('Max Loss', '{}${:.2f}'.format('-' if max_loss[1] < 0 else ' ', abs(max_loss[1]))),
]

# write the analysis
with open('python_analysis.txt', 'w') as python_analysis_file:
    python_analysis_file.write('\n'.join(lines))

# print the analysis
print('\n'.join(lines))
