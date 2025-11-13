import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 📊 Step 1: Create the dataset
# -------------------------------
data = {
    "Invoice_ID": ["INV1", "INV2", "INV3", "INV4", "INV5", "INV6", "INV7", "INV8", "INV9", "INV10"],
    "Branch": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
    "Customer_Type": ["Member", "Normal", "Member", "Normal", "Member", "Normal", "Member", "Normal", "Member", "Normal"],
    "Product_Category": ["Food", "Clothing", "Electronics", "Food", "Electronics", "Clothing", "Food", "Electronics", "Clothing", "Food"],
    "Quantity": [5, 3, 2, 4, 3, 2, 6, 5, 3, 7],
    "Unit_Price": [100, 200, 400, 120, 500, 220, 90, 450, 210, 80]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

print(df.head())

# -------------------------------
# 📈 Step 2: Total Sales per Branch
# -------------------------------
sns.barplot(x="Branch", y="Total_Sales", data=df, hue="Branch", legend=False, palette="viridis")
plt.title("Total Sales per Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.savefig("total_sales_branch.png")
plt.close()

# -------------------------------
# 🍱 Step 3: Average Sales by Product Category
# -------------------------------
sns.barplot(x="Product_Category", y="Total_Sales", data=df, hue="Product_Category", legend=False, palette="coolwarm")
plt.title("Average Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Total Sales")
plt.savefig("sales_by_category.png")
plt.close()

# -------------------------------
# 🧍 Step 4: Sales by Customer Type
# -------------------------------
sns.boxplot(x="Customer_Type", y="Total_Sales", data=df, hue="Customer_Type", palette="Set2", legend=False)
plt.title("Sales Distribution by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.savefig("sales_by_customer_type.png")
plt.close()

# -------------------------------
# 🔥 Step 5: Correlation Heatmap
# -------------------------------
sns.heatmap(df[["Quantity", "Unit_Price", "Total_Sales"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")
plt.show()
