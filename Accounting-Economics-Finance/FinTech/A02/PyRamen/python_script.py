# imports
import csv

# read the menu data
#   item, category, description, price, cost
menu_data, header = [], ''
with open('menu_data.csv') as menu_data_file:
    reader = csv.reader(menu_data_file)
    next(reader) # skip the header
    for row in reader:
        menu_data.append(row)

# read the sales data
#   Line_Item_ID, Date, Credit_Card_Number, Description, Quantity, Menu_Item
sales_data = []
with open('sales_data.csv') as sales_data_file:
    reader = csv.reader(sales_data_file)
    next(reader) # skip the header
    for row in reader:
        sales_data.append(row)
        
# process the data
report, count = {}, 0
for sales_record in sales_data:
    sales_item = sales_record[4]
    sales_item_quantity = int(sales_record[3])
    if sales_item not in report.keys():
        report[sales_item] = {
            '01-count': 0,
            '02-revenue': 0,
            '03-cost': 0,
            '04-profit': 0,
        }
    for menu_record in menu_data:
        menu_item = menu_record[0]
        menu_item_price = float(menu_record[3])
        menu_item_cost = float(menu_record[4])
        menu_item_profit = menu_item_price - menu_item_cost
        if sales_item == menu_item:
            report[sales_item]['01-count'] += sales_item_quantity
            report[sales_item]['02-revenue'] += menu_item_price * sales_item_quantity
            report[sales_item]['03-cost'] += menu_item_cost * sales_item_quantity
            report[sales_item]['04-profit'] += menu_item_profit * sales_item_quantity
    count += 1

# write the report
with open('python_report.txt', 'w') as python_report_file:
    for key, value in sorted(report.items()):
        python_report_file.write(f'{key} {value}\n')

# print the report
print(count)
for item_report in sorted(report.items()):
    print(item_report)