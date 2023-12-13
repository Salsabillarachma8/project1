#most purchased products
byproduct_df = order_product_mg_df.groupby(by="product_category_name").product_id.nunique().reset_index()
byproduct_df.rename(columns={
    "product_id": "product_name_count"
}, inplace=True)

plt.figure(figsize=(15, 5))

sns.barplot(
    y="product_name_count",
    x="product_category_name",
    data=byproduct_df.sort_values(by="product_name_count", ascending=False).head(5),
    palette=colors
)
plt.title("5 most purchased products", loc="center", fontsize=15)
plt.ylabel("quantity", fontsize=10)
plt.xlabel("product", fontsize=10)
plt.tick_params(axis='x', labelsize=10)
plt.show()
