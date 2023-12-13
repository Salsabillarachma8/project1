#The number and type of customer data will be checked.
orders_df.info()
#It was found that the 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', and 'order_estimated_delivery_date' have an incorrect type, which is 'object', when it should be 'datetime'

#Next, a check will be conducted for duplicate data.
print('jumlah duplicate :',orders_df.duplicated().sum())
#It has been found that there is no duplicate data.

#Next, a check will be conducted for null values.
orders_df.isna().sum()
#There are 160 null values in 'ordeer_approved_at', 1783 null values in 'order_delivered_carrier_date' and 2965 null values in 'order_delivered_customer_date'.

#Observing the data distribution by looking at the mean, median, etc.
customers_df.describe()
