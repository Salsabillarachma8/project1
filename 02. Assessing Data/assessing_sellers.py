#The number and type of customer data will be checked.
sellers_df.info()
#It has been found that the quantity and type of data are correct.

#Next, a check will be conducted for duplicate data.
print('jumlah duplicate :',sellers_df.duplicated().sum())
#It has been found that there is no duplicate data.

#Next, a check will be conducted for null values.
sellers_df.isna().sum()
#It has been found that there are no null values.

#Observing the data distribution by looking at the mean, median, etc.
sellers_df.describe()
