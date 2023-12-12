#prepare libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Gathering Data
customers_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/customers_dataset.csv")
order_items_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/order_items_dataset.csv")
order_payments_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/order_payments_dataset.csv")
order_reviews_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/order_reviews_dataset.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/orders_dataset.csv")
product_category_name_translation_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/product_category_name_translation.csv")
products_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/products_dataset.csv")
sellers_df = pd.read_csv("https://raw.githubusercontent.com/Salsabillarachma8/project1/main/00.%20Data/sellers_dataset.csv")
