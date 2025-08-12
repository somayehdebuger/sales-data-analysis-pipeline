
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists('visual'):
    os.makedirs('visual')

#read csv file
    
df=pd.read_csv(r'C:\Users\Rayanegostar\Desktop\Test.csv')

print("\n our DataFrame is:\n",df)
print("*"*70)

# colmn setting
def Col_sett(df):
#delete space and write uper first of each world 
    df.columns = df.columns.str.strip().str.capitalize()
    return df
#check  missing data  and data information
def Data_Info(df):
#basic information of Dataframe is 
   print("\n data information is :\n")
   df.info()
   print("_"*70)
#sum null data in each column 
   print("\n DataFrame NUN values in each column is :\n",df.isnull().sum())
   print("*"*70)
   return df

#delete duplicate data
def Clean_dup_data(df):
#delete duplicate and result show data frame
    df=df.drop_duplicates()
    print("data frame after delete duplicate data ia :\n",df)
    print("*"*70)
    return df

#filling nan & incorrect data 
def Filling_nan(df):
    df['Name']=df['Name'].fillna('Unknown')   #fill null name by "Unknown"
    mean_age = round(df['Age'].mean())         #calculate mean of age column
    df['Age']=df['Age'].fillna(mean_age)     #fill null age by  mean of age
    mean_score=round(df['Score'].mean())     #mean of score 
    df['Score']=df['Score'].fillna(mean_score)   #fill null score by mean of score column 
    df=df[df['Quantity']>=0].copy()
    df.loc[:, 'Quantity'] = df['Quantity'].fillna(round(df['Quantity'].mean()))# fill negetive quantity by mean of quantity
    print("\n data frame after filiing uun is :\n",df)                #print new data frame after this changes
    print("*"*70)

    return df
#find product and category by them relatinoship
def Find (df):
  
    category_map = df.groupby('Product')['Category'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)             ## Map most frequent category for each product

    df['Product'] = df['Product'].fillna('Unknown')                ## Replace missing products with 'Unknown'


    df['Category'] = df.apply(
        lambda row: category_map[row['Product']] if pd.isnull(row['Category']) and pd.notnull(row['Product']) else row['Category'],axis=1)                 # Fill missing categories using product-based mapping
             
    df['Category'] = df['Category'].fillna('Uncategorized')                            ## Fill remaining missing categories with 'Uncategorized'
    print("\n data frame after find mising product is:\n",df)
    print("*"*70)
    return df
#checking emloyer ages and delete them
def Em_age(df):
    mean_age=round(df['Age'].mean())
    df.loc[df['Age'] < 18, 'Age']=mean_age    #persons that are under legal age
    df.loc[df['Age']>60,'Age']=mean_age   #persons that are in retierd age
    return df
#convert units
def Convert(df):
    df['Weight']=df['Weight']*0.453592              # convert weight to kg
    df['Height']=df['Height']*2.5                    #convert height to cm
    df.rename(columns={'Weight':'Weight_kg','Height':'Height_cm'},inplace=True)      # rename weight and height
    df['Weight_kg']=df['Weight_kg'].round()                #round numbers in weight_kg column
    df['Height_cm']=df['Height_cm'].round()                 #round numbers in height_cm column
    return df

#date cleaning
def Date_cl(df):
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')         #convert date in data_frame to date_time
    return df

#high price
def Save_expensive_data(df):
    expensive=df[df['Price']>=700].copy()                 #find price expencive
    expensive.to_csv('expensive_product_data.csv',index=True)     #save as expensive csv file
    plt.hist(expensive['Price'], bins=20, color='orange')
    plt.title('Distribution of Expensive Products Prices (>700)')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig('visual/expensive_products_price_distribution.png')
    plt.close()
    return df

#data analyze
def Data_analize(df):
    print("description of cleaned data frame is :\n",df.describe())               #describe cleaned data frame
    print("_"*70)
    print("female and male values count is :\n",df['Gender'].value_counts())  #count male and female
    print("_"*70)
    print("smoker and no smoker person is :\n",df['Smoker'].value_counts())    #count smoker and dont smoker
    print("_"*70)
    print("count weekdays is :\n",df['Day'].value_counts())      #count weekdays repet
    print("_"*70)
    print("categories value is :\n",df['Category'].value_counts())   #count category values
    print("_"*70)
    print("product values is :\n",df['Product'].value_counts())      #count product value is
    print("_"*70)
    smoker_gender=pd.crosstab(df['Gender'], df['Smoker']).reset_index()
    print("checking relaton between smoker and gender :\n",smoker_gender)                  #checking relation between smoker and gender
    print("_"*70)
    print("relation between gender and score is :\n",df.groupby('Gender')['Score'].mean())         #check relatin between gender and score 
    print("_"*70)              
    print(df.groupby('Gender')['Tip'].mean())             #mean of tip for each gender
    print("_"*70)
    print(df.groupby('Gender')['Quantity'].mean())       #mean of quantity sale for each gender
    print("_"*70)
    print(df.groupby('Gender')['Price'].mean())           #mean of price sale for each gender
    print("_"*70)
    print(df[df['Price']==df['Price'].max()])           #maximum price
    print("_"*70)
    print(df[df['Price']==df['Price'].min()])             #min price
    print("_"*70)
    print(df[df['Score']==df['Score'].max()])            #maximum score
    print("_"*70)
    print(df[df['Score']==df['Score'].min()])             #min score 
    print("_"*70)
    print(df[['Price', 'Tip']].corr())        #compute_pearson_correlation_between_price_and_tip
    print("_"*70)
    print(df.groupby('Smoker')['Tip'].mean())           #check relation between smoker and tip
    print("_"*70)
    print(df.groupby('Day')['Price'].sum())             #calculate_total_sales_grouped_by_day
    print("_"*70)
    print(df.groupby('Product')['Quantity'].sum().sort_values(ascending=False))     #calculate total quantity grouped by product      
    print("_"*70)
    print(df.groupby('Product')['Price'].sum().sort_values(ascending=False)) #calculate total price grouped by product 
    print("_"*70)
    sns.countplot(data=df, x='Gender', hue='Smoker')
    plt.title('Gender vs Smoker')
    plt.savefig('visual/Gender_vs_Smoker.png')
    plt.show()
    plt.close()
    return df

#sum of lunch bill and tip
def Total_cost(df):
    df['Total_cost']=df['Tip']+df['Total_bill']      #creat new column Total_cost
    #figure
    plt.figure(figsize=(20,10))
    plt.grid(True)
    sns.histplot(df['Total_cost'],bins=15,color='red')
    plt.title("total cost for per person")
    plt.xlabel("total cost")
    plt.ylabel("frequency")
    plt.savefig('visual/total_cost_for_per_person.png')
    plt.show()
    plt.close()                  #show figure of total cost
    return df

#result sels & cost 
def Resul_income(df):
    df['Total_sale']=df['Quantity']*df['Price']                 #New column as total_sale
    df['Income']=df['Total_sale']-df['Total_cost']
    plt.scatter(df['Total_sale'],df['Total_cost'],c=df['Income'], cmap='coolwarm', s=60)
    plt.colorbar(label='Income Level')
    plt.title("sales vs cost")
    plt.xlabel("Total_sale")
    plt.ylabel("Total_cost")
    plt.savefig('visual/sales_vs_cost.png')
    plt.show()              #show figure of total price
    plt.close()         
    return df
#sales group
def Sales_summery(df):
    summary=df.groupby(['Category','Product']).agg({'Total_sale':'sum','Quantity':'sum'})           #Aggregate_Sales_And_Quantity_By_Category_And_Product
    print("\n GroupBy Category Product Summary:\n",summary)
    print("_"*70)
    plt.figure(figsize=(12,6))
    sns.barplot(data=summary, x='Category', y='Total_sale', errorbar=None,color="pink")
    plt.title("sum of sale by category")
    plt.xlabel("category")
    plt.ylabel("total sales")
    plt.savefig('visual/sum_of_sale_by_category.png')
    plt.show()
    plt.close()                    #figure
    plt.figure(figsize=(12,6))
    sns.barplot(data=summary, x='Product', y='Total_sale', errorbar=None,color="red")
    plt.title("sum of sale by product")
    plt.xlabel("product")
    plt.ylabel("total sales")
    plt.savefig('visual/sum_of_sale_by_product.png')
    plt.show()
    plt.close()                #figure
    category_sales =summary.groupby('Category')['Total_sale'].sum().reset_index()
    plt.figure(figsize=(8,8))
    plt.pie(category_sales['Total_sale'], labels=category_sales['Category'], autopct='%1.1f%%', startangle=140)
    plt.title('sels by each category ')
    plt.savefig('visual/sels_by_each_category.png')
    plt.show()
    plt.close()             #figure

    return df
#data statistical analysis
def Statistical_anly(df):
    print("\n data frame shape is :\n",df.shape)             # data frame shape 
    print("_"*70)
    print("\n null values in data is :\n:",df.isnull().sum())    #null values
    print("_"*70)
    print("\n data information is :\n")
    df.info()                  #data informaton
    print("_"*70)
    print(df.describe())        #data description
    print("_"*70)
    print(df.head())             #data 5 first rows 
    print("_"*70)
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        plt.figure(figsize=(15,5))
        sns.countplot(data=df, x=col, order=df[col].value_counts().index,palette='Set2')
        plt.title(f'values in each columns {col}')
        plt.xticks(rotation=45)
        plt.savefig(f'visual/values_in_each_columns{col}.png')
        plt.show()
        plt.close()           #figure
    return df
#make catgory by age
def Age_category(df):
    bins = [0, 12, 18, 30, 60, 90]
    labels = ['Child,cantwork', 'Teen,under elegal age', 'Young', 'Adult','old,cant work ']
    df['Age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)      #create age group column
    
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x='Age_group', hue='Age_group',legend=False)
    plt.title("Distribution by Age Group")
    plt.savefig('visual/Distribution_by_Age_Group.png')
    plt.show()
    plt.close()     #figure
    return df
#mean of height employers
def Mean_height(df):
    mean_height=df.groupby('Gender')['Height_cm'].mean()       #calculate mean gender grouped by height
    print("\n mean of height by gender is :\v",mean_height)
    print("_"*70)
    plt.figure(figsize=(8,5))
    sns.barplot(x=mean_height.index, y=mean_height.values)
    plt.title("height and gender relation" )
    plt.ylabel("Mean Height (cm)")
    plt.xlabel("Gender")
    plt.savefig('visual/height_and_gender_relation.png')
    plt.show()
    plt.close()        #figure
    return df
 #sales by each seller
def Seller_sales(df):
    seller_sale=df.groupby('Name')['Total_sale'].sum().sort_values(ascending=False).reset_index()     #calculate total sales grouped by seller
    print("\n sumation of sales for each seller is :\n",seller_sale)
    print("_"*70)
    plt.figure(figsize=(12,6))
    sns.barplot(data=seller_sale, x='Name', y='Total_sale', order=seller_sale['Name'])
    plt.title("seller sales relation" )
    plt.ylabel("Total price")
    plt.xlabel("seller names")
    plt.savefig('visual/seller_sales_relation.png')
    plt.show()
    plt.close()       #figure
    return df
#calculate sales by each product
def Product_sale(df):
    df['Year']=df['Date'].dt.year           # convert date to year
    df['Mounth']=df['Date'].dt.month_name()        #convert date to mounth names
    df['Season']=df['Date'].dt.quarter           #convert date to season 
    product_sale_year=df.groupby(['Product','Year'])['Total_sale'].sum().reset_index()     #GroupBy Product And Year TotalSales
    product_sale_mounth=df.groupby(['Product','Mounth'])['Total_sale'].sum().reset_index()           #GroupBy Product And mounth TotalSales
    product_sale_season=df.groupby(['Product','Season'])['Total_sale'].sum().reset_index()            #GroupBy Product And season TotalSales
    print("\nProduct Sales By Year:\n",product_sale_year)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=product_sale_year,x='Year',y='Total_sale',hue='Product')
    plt.title("product sale by year")
    plt.savefig('visual/product_sale_by_year.png')
    plt.show()
    plt.close()                #figure
    print("\nProduct_Sales_By_mounth:\n",product_sale_mounth)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=product_sale_mounth,x='Mounth',y='Total_sale',hue='Product')
    plt.title("product sale by mounth")
    plt.savefig('visual/product_sale_by_mounth.png')
    plt.show()
    plt.close()            #figure
    print("\nProduct Sales By season:\n",product_sale_season)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=product_sale_season,x='Season',y='Total_sale',hue='Product')
    plt.title("product sale by season")
    plt.savefig('visual/product_sale_by_season.png')
    plt.show()
    plt.close()           #figure
    return df
#calculate sales by each category
def Category_sale(df):
    Category_sale_year=df.groupby(['Category','Year'])['Total_sale'].sum().reset_index()                   #GroupBy  category And Year TotalSales
    Category_sale_mounth=df.groupby(['Category','Mounth'])['Total_sale'].sum().reset_index()                   #GroupBy  category And mounth TotalSales
    Category_sale_season=df.groupby(['Category','Season'])['Total_sale'].sum().reset_index()                       #GroupBy  category And Season TotalSales
    print("\n category sale by year:\n",Category_sale_year)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=Category_sale_year,x='Year',y='Total_sale',hue='Category')
    plt.title("Category sale by year")
    plt.savefig('visual/Category_sale_by_year.png')
    plt.show()
    plt.close()         #figure
    print("\n category sale by mounth:\n",Category_sale_mounth)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=Category_sale_mounth,x='Mounth',y='Total_sale',hue='Category')
    plt.title("Category sale by mounth")
    plt.savefig('visual/Category sale_by_mounth.png')
    plt.show()
    plt.close()            #figure
    print("\n category sale by season :\n",Category_sale_season)
    print("_"*70)
    plt.figure(figsize=(9,5))
    sns.barplot(data=Category_sale_season,x='Season',y='Total_sale',hue='Category')
    plt.title("Category sale by season")
    plt.savefig('visual/Category_sale_by_season.png')
    plt.show()
    plt.close()    #figure
    return df
#persent of smoker 
def Smoker(df):
    smoker=df['Smoker'].value_counts(normalize=True) * 100    #count persent of smokers
    plt.figure(figsize=(5,5))   
    plt.pie(smoker.values, labels=smoker.index, autopct='%1.1f%%', startangle=140)
    plt.title("presents of smoker and no smoker in data ")
    plt.savefig('visual/presents_of_smoker_and_no_smoker_in_data .png')
    plt.show()
    plt.close()   #figure 
    return df
#total score for each seller
def Seller_score(df):
    seller_score=df.groupby('Name')['Score'].sum().reset_index()      #total score by each seller 
    print("\n sumation of score for each seller is :\n",seller_score)
    print("_"*80)
    plt.figure(figsize=(5,5))   
    sns.barplot(data=seller_score,x='Name',y='Score',order=seller_score['Name'],color='purple',hue='Name')
    plt.title("gouropby seller score ")
    plt.savefig('visual/gouropby_seller_score.png')
    plt.show()
    plt.close()   #figure
    return df



df=Col_sett(df)
df=Data_Info(df)
df=Clean_dup_data(df)
df=Filling_nan(df)
df=Find(df)
df=Em_age(df)
df=Convert(df)
df=Date_cl(df)
df=Save_expensive_data(df)
df=Data_analize(df)
df=Total_cost(df)
df=Resul_income(df)
df=Sales_summery(df)
df=Statistical_anly(df)
df=Age_category(df)
df=Mean_height(df)
df=Seller_sales(df)
df=Product_sale(df)
df=Category_sale(df)
df=Smoker(df)
df=Seller_score(df)
df.to_csv('output.csv',index=True)
