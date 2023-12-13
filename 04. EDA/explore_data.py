#Top 5 cities from consumers
customers_df.groupby(by='customer_city').customer_id.nunique().sort_values(ascending=False)
states.head()

#Top 5 states from consumers
states=customers_df.groupby(by='customer_state').customer_id.nunique().sort_values(ascending=False)
states.head()

#Combining the 'order_items' and 'orders' tables to obtain new information.
order_mg_df = pd.merge(
    left=order_items_df,
    right=orders_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
order_mg_df.head()

#5 highest prices
price=order_items_df.groupby(by='price').order_id.nunique().sort_values(ascending=False)
price.head()

#Combining the 'order_mg' and 'products' tables to obtain new information.
order_product_mg_df = pd.merge(
    left=order_mg_df,
    right=products_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
order_product_mg_df.head()
