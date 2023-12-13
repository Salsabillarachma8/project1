#Fixing missing values in 'product_category_name'
#First, we will perform a check on the existing values in 'product_category_name' before deciding whether to delete the 'product_category_name' column or fill in the null parts and determine the appropriate method for null filling.
products_df.product_category_name.value_counts()
#Since the values are scattered, null values will be filled with the values above them.
products_df['product_category_name'] = products_df['product_category_name'].fillna(method='pad')
#checking
products_df.isna().sum()

#Fixing missing values in 'product_name_lenght'
#checking the value
products_df.product_name_lenght.value_counts()
#Since the values are scattered, null values will be filled with the values above them.
products_df['product_name_lenght'] = products_df['product_name_lenght'].fillna(method='pad')
#checking
products_df.isna().sum()

#Fixing missing values in 'product_description_lenght'
#checking the value
products_df.product_description_lenght.value_counts()
#Since the values are scattered, null values will be filled with the values above them.
products_df['product_description_lenght']=products_df['product_description_lenght'].fillna(method='pad')
#checking
products_df.isna().sum()

#Fixing missing values in 'product_photos_qty'
#checking the value
products_df.product_photos_qty.value_counts()
#Because the ratio of the used values to the other values is quite large, null values will be filled with the most frequently used values.
products_df.product_photos_qty.fillna(value='1.0',inplace=True)
#checking
products_df.isna().sum()

#The considerations for filling null values above will be used for the following steps.
#Fixing missing values in 'product_weight_g'
products_df.product_weight_g.value_counts()
products_df.product_weight_g.fillna(value='200.0',inplace=True)
products_df.isna().sum()

#Fixing missing values in 'product_length_cm'
products_df.product_length_cm.value_counts()
products_df.product_length_cm.fillna(value='16.0',inplace=True)
products_df.isna().sum()

#fixing missing value in 'product_height_cm'
products_df.product_height_cm.value_counts()
products_df.product_height_cm.fillna(value='10.0',inplace=True)
products_df.isna().sum()

#fixing missing value in 'pproduct_width_cm'
products_df.product_width_cm.value_counts()
products_df.product_width_cm.fillna(value='11.0',inplace=True)
products_df.isna().sum()

