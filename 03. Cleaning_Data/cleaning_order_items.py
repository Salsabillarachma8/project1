#Correcting the type of 'shipping_limit_date' to 'datetime'.
datetime_columns = ["shipping_limit_date"]
for column in datetime_columns:
  order_items_df[column] = pd.to_datetime(order_items_df[column])
#Checking
order_items_df.info()
#The data has been changed to the correct type.
