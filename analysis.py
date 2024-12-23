# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file with all sheets
file_path = "C:\\Users\\polan\\Downloads\\Uppliance_ai\\Combined_Workbook.csv"
user_details = pd.read_excel(file_path, sheet_name="UserDetails.csv")
cooking_sessions = pd.read_excel(file_path, sheet_name="CookingSessions.csv")
order_details = pd.read_excel(file_path, sheet_name="OrderDetails.csv")

# Merge datasets
merged_data = (
    order_details
    .merge(user_details, on="User ID", how="left")
    .merge(cooking_sessions, on=["User ID", "Dish Name", "Meal Type"], how="left")
)

# Analyze popular dishes
popular_dishes = merged_data['Dish Name'].value_counts().head(5)
print("Top 5 Popular Dishes:")
print(popular_dishes)

# Visualize the top dishes
plt.figure(figsize=(8, 5))
popular_dishes.plot(kind="bar", title="Top 5 Popular Dishes", color="skyblue")
plt.xlabel("Dish Name")
plt.ylabel("Order Count")
plt.show()

# Analyze orders by location
orders_by_location = merged_data['Location'].value_counts().head(5)
plt.figure(figsize=(8, 5))
orders_by_location.plot(kind="bar", title="Top 5 Locations by Order Count", color="orange")
plt.xlabel("Location")
plt.ylabel("Order Count")
plt.show()

# Analyze orders by age group
orders_by_age = merged_data['Age'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
orders_by_age.plot(kind="line", title="Orders by Age Group", marker='o', color="green")
plt.xlabel("Age")
plt.ylabel("Order Count")
plt.grid()
plt.show()

# Recommendations
print("Recommendations:")
print("1. Promote top dishes to increase sales.")
print("2. Focus on high-order locations for targeted campaigns.")
print("3. Customize marketing strategies for specific age groups.")
