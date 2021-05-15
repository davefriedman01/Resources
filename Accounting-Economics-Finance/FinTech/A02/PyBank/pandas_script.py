# imports
import pandas as pd

# read data
df = pd.read_csv('budget_data.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)

# compute the number of months
num_months = df.shape[0]
#df.index.size
#num_months = df['Date'].count()
#num_months = len(df)

# compute the net total profit
net_profit = df['Profit/Losses'].sum()

# compute the average change in profit
avg_change = df['Profit/Losses'].diff().mean()

# compute the change in profit of the month which saw the greatest increase in profit
max_gain = df['Profit/Losses'].diff().max()

# compute the change in profit of the month which saw the greatest decrease in profit
max_loss = df['Profit/Losses'].diff().min()

analysis = pd.DataFrame(
    {'Num Months': num_months, 'Net Profit': net_profit, 'Avg Change': avg_change, 'Max Gain': max_gain, 'Max Loss': max_loss},
    index=[0]
).iloc[0].round(2)
# analysis = pd.Series(
#    data = [num_months, net_profit, avg_change, max_gain, max_loss],
#    index = ['Num Months', 'Net Profit', 'Avg Change', 'Max Gain', 'Max Loss']
#)

# format the analysis
lines = [
    'Financial Analysis',
    '-' * 25,
    analysis.to_string()
]

# write the analysis
with open('pandas_analysis.txt', 'w') as pandas_analysis_file:
    pandas_analysis_file.write('\n'.join(lines))
    
# print the analysis
print('\n'.join(lines))
