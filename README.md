# sales-data-analysis-pipeline
A Python project for cleaning, analyzing, and visualizing company sales and employee data.
Data Cleaning, Analysis, and Visualization Project
📌 Overview
This project is a Python-based data cleaning, analysis, and visualization pipeline developed as part of the Python section of my Data Science Bootcamp.
The script reads a CSV file containing company sales data and employee personal information, cleans and preprocesses it, performs various analyses, and generates multiple visualizations.
It also creates filtered datasets (e.g., expensive products) and saves them for further use.

🎯 Features
The script includes:

Data cleaning: Removing duplicates, handling missing values, fixing incorrect data.

Data transformation: Unit conversion, age categorization, date formatting.

Data analysis:

Descriptive statistics

Grouped summaries

Correlation analysis

Data visualization: Histograms, bar plots, pie charts, scatter plots.

Exporting results:

Cleaned data saved as output.csv

Expensive products saved as expensive_product_data.csv

Charts saved in the visual/ folder.

🛠 Technologies Used
Python 3

pandas – Data manipulation and analysis

matplotlib – Data visualization

seaborn – Advanced visualization

📂 Project Structure
bash
Copy
Edit
project/
│
├── main.py                         # Main Python script
├── Test.csv                        # Input dataset (not included in repo if private)
├── output.csv                      # Final cleaned dataset (generated)
├── expensive_product_data.csv      # Filtered expensive products data (generated)
├── visual/                         # Folder containing all generated charts
│   ├── expensive_products_price_distribution.png
│   ├── Gender_vs_Smoker.png
│   ├── total_cost_for_per_person.png
│   ├── sales_vs_cost.png
│   ├── sum_of_sale_by_category.png
│   ├── sum_of_sale_by_product.png
│   ├── sels_by_each_category.png
│   ├── values_in_each_columns[ColumnName].png
│   ├── Distribution_by_Age_Group.png
│   ├── height_and_gender_relation.png
│   ├── seller_sales_relation.png
│   ├── product_sale_by_year.png
│   ├── product_sale_by_mounth.png
│   ├── product_sale_by_season.png
│   ├── Category_sale_by_year.png
│   ├── Category_sale_by_mounth.png
│   ├── Category_sale_by_season.png
│   ├── presents_of_smoker_and_no_smoker_in_data.png
│   ├── gouropby_seller_score.png
│   └── ... (more generated plots)
└── README.md
🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies
It is recommended to create a virtual environment before installing dependencies:

bash
Copy
Edit
pip install pandas matplotlib seaborn
Prepare your dataset

Place your CSV file in the project directory.

Update the file path in pd.read_csv() inside the script:

python
Copy
Edit
df = pd.read_csv("Test.csv")
Run the script

bash
Copy
Edit
python main.py
Check the outputs

Cleaned dataset: output.csv

Expensive products: expensive_product_data.csv

Visualizations: inside visual/ folder

📊 Example Outputs
Sample Analyses Performed:

Gender distribution by smoking habits

Total sales vs. costs

Sales breakdown by category and product

Age group distribution

Price distribution of expensive products

Example Plot:


📌 Functions in the Script
The script is modular and contains specific functions for each processing step:

Col_sett(df) – Standardizes column names

Data_Info(df) – Displays dataset info and missing values

Clean_dup_data(df) – Removes duplicate rows

Filling_nan(df) – Handles missing values

Find(df) – Fills missing product/category values

Em_age(df) – Adjusts unrealistic ages

Convert(df) – Converts units (weight, height)

Date_cl(df) – Formats date columns

Save_expensive_data(df) – Filters and saves expensive products

Data_analize(df) – Generates descriptive statistics and plots

Total_cost(df) – Calculates total cost per person

Resul_income(df) – Compares sales and cost

Sales_summery(df) – Summarizes sales by category and product

Statistical_anly(df) – Performs statistical analysis

Age_category(df) – Categorizes age groups

Mean_height(df) – Analyzes mean height by gender

Seller_sales(df) – Summarizes sales by seller

Product_sale(df) – Sales trends by product (year, month, season)

Category_sale(df) – Sales trends by category

Smoker(df) – Smoking status distribution

Seller_score(df) – Scores by seller


