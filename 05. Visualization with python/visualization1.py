#highest product order price
plt.figure(figsize=(5, 5))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="price",
    x="product_category_name",
    data=order_product_mg_df.sort_values(by="price", ascending=False).head(3),
    palette=colors
)

plt.title("highest product order price", loc="center", fontsize=15)
plt.ylabel("price", fontsize=10)
plt.xlabel("product", fontsize=10)
plt.tick_params(axis='x', labelsize=10)
plt.show()
