#Correcting the type of review_creation_date' and 'review_answer_timestamp' to 'datetime'.
datetime_columns = ['review_creation_date','review_answer_timestamp']
for column in datetime_columns:
  order_reviews_df[column]=pd.to_datetime(order_reviews_df[column])
#checking
order_reviews_df.info()

#Fixing missing values in 'review_comment_title'.
#First, we will perform a check on the existing values in 'order_reviews' before deciding whether to delete the 'order_reviews' column or fill in the null parts and determine the appropriate method for null filling
order_reviews_df.review_comment_title.value_counts()
#Since there are two top values, 'Recomendo' and 'recomendo', which have the same meaning, the null values will be filled with the most frequently occurring value.
order_reviews_df.review_comment_title.fillna(value="Recomendo",inplace=True)

#Fixing missing values in 'review_comment_massage'
#First, we will perform a check on the existing values in 'review_comment_message' before deciding whether to delete the 'review_comment_message' column or fill in the null parts and determine the appropriate method for null filling
order_reviews_df.review_comment_message.value_counts()
#Because the values in the 'review_comment_message' column regarding comments and messages from customers are very diverse, and there are too many null values, this column will be removed.
del order_reviews_df['review_comment_message']

#checking
order_reviews_df.isna().sum()
