#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:37:06 2024

@author: shivam
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = '/home/shivam/Downloads/shopping_trends_updated.csv'
shop = pd.read_csv(file_path)
print(shop.shape)

# Convert CSV to Excel
shop.to_excel("shopping_trends_updated.xlsx")
print(shop.head())

# Display data types of columns
print(shop.dtypes)

# Display column names
print(shop.columns)

# Display dataset information
print(shop.info())

# Check for missing values
print(shop.isnull().sum())

# Display unique values in certain columns
print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()
print(f"The unique values of the 'Color' column are: {shop['Color'].unique()}")
print()

# Display value counts and mean of 'Age' column
print(shop['Age'].value_counts())
print(shop['Age'].mean())

# Display unique values in the 'Gender' column
print(shop['Gender'].unique())


# Q1. What is the overall distribution of customer ages in the dataset?
# Create a histogram to visualize the distribution of ages
plt.figure(figsize=(10, 6))
sns.histplot(data=shop, x='Age', kde=True)
plt.title('Overall Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Q2. How does the average purchase amount vary across different product categories?
# Group by 'Category' and calculate the mean purchase amount
avg_purchase_amount_by_category = shop.groupby('Category')['Purchase Amount (USD)'].mean().reset_index()
# Create a bar plot to visualize the average purchase amount by category
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_purchase_amount_by_category, x='Category', y='Purchase Amount (USD)')
plt.title('Average Purchase Amount by Product Category')
plt.xlabel('Category')
plt.ylabel('Average Purchase Amount (USD)')
plt.show()

# Q3. Which gender has the highest number of purchases?
# Get the count of purchases by gender
purchases_by_gender = shop['Gender'].value_counts()
# Create a bar plot to visualize the number of purchases by gender
plt.figure(figsize=(10, 6))
sns.barplot(x=purchases_by_gender.index, y=purchases_by_gender.values)
plt.title('Number of Purchases by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Purchases')
plt.show()

# Q4. What are the most commonly purchased items in each category?
# Find the most common item purchased in each category
most_common_items = shop.groupby('Category')['Item Purchased'].agg(lambda x: x.value_counts().index[0]).reset_index()
# Create a bar plot to visualize the most commonly purchased items by category
plt.figure(figsize=(10, 6))
sns.barplot(data=most_common_items, x='Category', y='Item Purchased')
plt.title('Most Commonly Purchased Items by Category')
plt.xlabel('Category')
plt.ylabel('Most Common Item')
plt.show()

# Q5. Are there any specific seasons where customer spending is significantly higher?
# Group by 'Season' and calculate the total purchase amount
seasonal_spending = shop.groupby('Season')['Purchase Amount (USD)'].sum().reset_index()
# Create a pie chart to visualize the seasonal spending distribution
plt.figure(figsize=(8, 8))
plt.pie(seasonal_spending['Purchase Amount (USD)'], labels=seasonal_spending['Season'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Seasonal Customer Spending Distribution')
plt.show()

# Q6. What is the average rating given by customers for each product category?
# Group by 'Category' and calculate the mean review rating
avg_rating_by_category = shop.groupby('Category')['Review Rating'].mean().reset_index()
# Create a bar plot to visualize the average rating by category
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_rating_by_category, x='Category', y='Review Rating')
plt.title('Average Rating by Product Category')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.show()

# Q7. Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?
# Group by 'Subscription Status' and calculate the mean purchase amount
purchase_behavior = shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean().reset_index()
# Create a bar plot to visualize the purchase behavior by subscription status
plt.figure(figsize=(10, 6))
sns.barplot(data=purchase_behavior, x='Subscription Status', y='Purchase Amount (USD)')
plt.title('Purchase Behavior by Subscription Status')
plt.xlabel('Subscription Status')
plt.ylabel('Average Purchase Amount (USD)')
plt.show()

# Q8. Which payment method is the most popular among customers?
# Get the count of each payment method
payment_method_popularity = shop['Payment Method'].value_counts()
# Create a bar plot to visualize the popularity of payment methods
plt.figure(figsize=(10, 6))
sns.barplot(x=payment_method_popularity.index, y=payment_method_popularity.values)
plt.title('Popularity of Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.show()

# Q9. Do customers who use promo codes tend to spend more than those who don't?
# Group by 'Promo Code Used' and calculate the mean purchase amount
promo_code_spending = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].mean().reset_index()
# Create a bar plot to visualize the spending by promo code usage
plt.figure(figsize=(10, 6))
sns.barplot(data=promo_code_spending, x='Promo Code Used', y='Purchase Amount (USD)')
plt.title('Spending by Promo Code Usage')
plt.xlabel('Promo Code Used')
plt.ylabel('Average Purchase Amount (USD)')
plt.show()

# Q10. How does the frequency of purchases vary across different age groups?
# Create an 'Age_category' column based on age ranges
shop['Age_category'] = pd.cut(shop['Age'], bins=[0, 15, 18, 30, 50, 70], labels=['child', 'teen', 'young adult', 'adult', 'senior'])
# Get the count of purchases by age category
purchase_frequency_by_age = shop['Age_category'].value_counts().sort_index()
# Create a bar plot to visualize the purchase frequency by age group
plt.figure(figsize=(10, 6))
sns.barplot(x=purchase_frequency_by_age.index, y=purchase_frequency_by_age.values)
plt.title('Purchase Frequency by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Purchases')
plt.show()

# Q11. Are there any correlations between the size of the product and the purchase amount?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=shop, x='Size', y='Purchase Amount (USD)')
plt.title('Correlation between Product Size and Purchase Amount')
plt.xlabel('Size')
plt.ylabel('Purchase Amount (USD)')
plt.show()

# Q12. Which shipping type is preferred by customers for different product categories?
shipping_preference = shop.groupby(['Category', 'Shipping Type']).size().unstack()
shipping_preference.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Shipping Preference by Product Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.legend(title='Shipping Type')
plt.show()

# Q13. How does the presence of a discount affect the purchase decision of customers?
discount_effect = shop.groupby('Discount Applied')['Purchase Amount (USD)'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=discount_effect, x='Discount Applied', y='Purchase Amount (USD)')
plt.title('Effect of Discount on Purchase Amount')
plt.xlabel('Discount Applied')
plt.ylabel('Average Purchase Amount (USD)')
plt.show()

# Q14. Are there any specific colors that are more popular among customers?
color_popularity = shop['Color'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=color_popularity.index, y=color_popularity.values)
plt.title('Popularity of Colors among Customers')
plt.xlabel('Color')
plt.ylabel('Count')
plt.show()

# Q15. What is the average number of previous purchases made by customers?
avg_previous_purchases = shop['Previous Purchases'].mean()
print(f"The average number of previous purchases made by customers is: {avg_previous_purchases}")

# Q16. How does the purchase amount differ based on the review ratings given by customers?
plt.figure(figsize=(10, 6))
sns.boxplot(data=shop, x='Review Rating', y='Purchase Amount (USD)')
plt.title('Purchase Amount by Review Rating')
plt.xlabel('Review Rating')
plt.ylabel('Purchase Amount (USD)')
plt.show()

# Q17. Are there any noticeable differences in purchase behavior between different locations?
purchase_behavior_by_location = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=purchase_behavior_by_location, x='Location', y='Purchase Amount (USD)')
plt.title('Purchase Behavior by Location')
plt.xlabel('Location')
plt.ylabel('Average Purchase Amount (USD)')
plt.xticks(rotation=90)
plt.show()

# Q18. Is there a relationship between customer age and the category of products they purchase?
age_category_crosstab = pd.crosstab(shop['Age'], shop['Category'])
plt.figure(figsize=(12, 8))
sns.heatmap(age_category_crosstab, cmap='Blues', annot=True, fmt='d')
plt.title('Relationship between Age and Product Category')
plt.xlabel('Product Category')
plt.ylabel('Age')
plt.show()

# Q19. How does the average purchase amount differ between male and female customers?
avg_purchase_by_gender = shop.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_purchase_by_gender, x='Gender', y='Purchase Amount (USD)')
plt.title('Average Purchase Amount by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Purchase Amount (USD)')
plt.show()


