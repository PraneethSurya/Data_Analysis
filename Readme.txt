Data Analysis Task

Overview

This project revolves around the processes of the datasets analyzing users’ tendencies and attitudes toward cooking and ordering food. The analysis is centered on popular dishes and recommendations that can be implemented based on the analysis done.

Datasets

The analysis employs three dataset:

UserDetails.csv : Contains user demographic data.

CookingSessions.csv : Contains user’s cooking session data.

OrderDetails.csv : Contains data regarding user orders.

Key Steps

Load Data
This is a task whereby the kind of data that was prepared for analysis and identified in the introduction as user details, cooking sessions and orders was imported from an excel file. All the three datasets are found on different sheets in the said excel file.

file_path = "C:\Users\polan\Downloads\Uppliance_ai\Assigment.xlsx"

user_details = pd.read_excel(file_path, sheet_name = 'UserDetails.csv')

cooking_sessions = pd.read_excel(file_path,sheet_name = 'CookingSessions.csv')

order_details = pd.read_excel(file_path,sheet_name = 'OrderDetails.csv')

Merge Datasets
The merging of the data sets takes place based on common shared attributes (User ID and particular order made) to yield combined data set for thorough analysis.
merged_data = (

    order_details

    .merge(user_details, on="User ID", how="left")

    .merge(cooking_sessions, on=["User ID", "Dish Name", "Meal Type"], how="left")

)

3. Analyze Popular Dishes

The code identifies the top 5 most popular four-hands cooking dishes based on the number of orders.

popular_dishes = merged_data['Dish Name'].value_counts().nlargest(5)

print(“Top 5 Popular Dishes:”)

print(popular_dishes)

4. Visualize Results

To visualize the most popular dishes, A vertical bar graph is prepared.

popular_dishes.plot(kind=”bar”, title=”Top 5 Popular Dishes”, color=”skyblue”)

plt.xlabel(“Dish Name”)

plt.ylabel(“Order Count”)

plt.show()

5. Recommendations

From the results of the analysis, actionable recommendations are suggested:

* Focus on the most selling dishes by promoting them.

* Observe trends to help market them better.

print(“Recommendations:”)

print(“1. Focus on the most selling dishes by promoting them.”)

print(“2. Observe trends to help market them better.”)

1. Download the file named Assigment.xlsx from the designated folder. 

2. Modify the file_path variable within the script in the event the file is stored elsewhere. 

3. Execute the python code (Ensure required libraries are present). 

Prerequisites 

* Python 3.x 

* Libraries: 
o pandas
o matplotlib

Install required libraries using pip: 
pip install pandas matplotlib 

Output 
* Console Output: The first five most popular dishes with their recommendations. 

* Visualization: A bar graph showing five most frequently ordered dishes.

