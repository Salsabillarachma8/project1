#By Recency (days)
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]
 
sns.barplot(
    y="recency",
    x="customer_id",
    data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors,
)
ax.set_title("By Recency (days)", loc="center", fontsize=18)
ax.set_ylabel("recency", fontsize=15)
ax.set_xlabel("customer_id", fontsize=15)
ax.tick_params(axis='x', labelsize=5)
ax.tick_params(axis='y', labelsize=10)
plt.show()

#frequency
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]
 
sns.barplot(
    y="frequency",
    x="customer_id",
    data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors
)
ax.set_title("By Frequency", loc="center", fontsize=18)
ax.set_ylabel("frequency", fontsize=15)
ax.set_xlabel("customer_id", fontsize=15)
ax.tick_params(axis='x', labelsize=5)
ax.tick_params(axis='y', labelsize=10)
plt.show()

#monetary
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]
 
sns.barplot(
    y="monetary",
    x="customer_id",
    data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors
)
ax.set_title("By Monetary", loc="center", fontsize=18)
ax.set_ylabel("monetary", fontsize=15)
ax.set_xlabel("customer_id", fontsize=15)
ax.tick_params(axis='x', labelsize=5)
ax.tick_params(axis='y', labelsize=10)
plt.show()
