#The number and type of customer data will be checked.
order_reviews_df.info()
#It was found that the 'review_creation_date' and 'review_answer_timestamp' have an incorrect type, which is 'object', when it should be 'datetime'.

#Next, a check will be conducted for duplicate data.
print('jumlah duplicate :', order_reviews_df.duplicated().sum())
#It has been found that there is no duplicate data.

#Next, a check will be conducted for null values.
order_reviews_df.isna().sum()
#There are 87656 null values in 'review_comment_title' and 58247 null values in 'review_comment_message'.

#Observing the data distribution by looking at the mean, median, etc.
order_reviews_df.describe()
