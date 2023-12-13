#The number and type of customer data will be checked.
products_df.info()
#It has been found that the quantity and type of data are correct.

#Next, a check will be conducted for duplicate data.
print('jumlah duplicate :',products_df.duplicated().sum())
#It has been found that there is no duplicate data.

#Next, a check will be conducted for null values.
products_df.isna().sum()
#There are 610 null values in 'product_category_name', 610 null values in 'product_name_lenght', 610 null values in 'product_description_lenght', 610 null values in 'product_photos_qty ', 2 null values in 'product_weight_g', 2 null values in 'product_length_cm', 2 null values in 'product_height_cm' and 2 null values in 'product_width_cm'.

#Observing the data distribution by looking at the mean, median, etc.
products_df.describe()
