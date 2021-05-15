# imports
import pandas as pd

# read the menu data
menu_df = pd.read_csv('menu_data.csv', index_col='item').drop(columns=['category', 'description']).astype(float)
menu_df['profit'] = menu_df.price - menu_df.cost

# read the sales data
sales_df = pd.read_csv('sales_data.csv', index_col='Line_Item_ID').drop(columns=['Date', 'Credit_Card_Number'])

# process the data
quantity = sales_df.groupby('Menu_Item').sum().iloc[:, 0]
relevant_menu_df = menu_df[menu_df.index.isin(sales_df.Menu_Item.unique())].sort_index()
product_df = pd.DataFrame({
    'quantity': quantity,
    'revenue':  quantity * relevant_menu_df.price,
    'cost':     quantity * relevant_menu_df.cost,
    'profit':   quantity * relevant_menu_df.profit,
},
    index=sales_df.Menu_Item.sort_values().unique()
    # index=sales_df.Menu_Item.sort_values().drop_duplicates().values
)
#product_df = pd.DataFrame(
#    index=sales_df.Menu_Item.sort_values().unique()
#    # index=sales_df.Menu_Item.sort_values().drop_duplicates().values
#)
#product_df['quantity'] = quantity
#product_df['revenue'] =  quantity * relevant_menu_df.price
#product_df['cost'] =     quantity * relevant_menu_df.cost
#product_df['profit'] =   quantity * relevant_menu_df.profit

# write the report
with open('pandas_report.txt', 'w') as pandas_report_file:
    pandas_report_file.write(product_df.to_string())
    
# print the report
print(product_df)