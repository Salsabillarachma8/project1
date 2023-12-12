#prepare libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Gathering Data
customers_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/customers_dataset.csv")
order_items_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/order_items_dataset.csv")
order_payments_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/order_payments_dataset.csv")
order_reviews_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/order_reviews_dataset.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/orders_dataset.csv")
product_category_name_translation_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/product_category_name_translation.csv")
products_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/products_dataset.csv")
sellers_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma/Dashboard1/main/sellers_dataset.csv")

