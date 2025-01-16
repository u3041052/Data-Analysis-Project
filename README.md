# Data-Analysis-Project
This is a very brief project on Data Analysis using Python.

## Project Description
The project focuses on analysizing a sales dataset and answering some basic questions regarding it.The project leverages Python libraries like pandas, numpy, seaborn, matplotlib, and plotly for various tasks.

## File Structure
- shopping_trends_updated.csv: The original dataset in CSV format.
- shopping_trends_updated.xlsx: The converted dataset in Excel format and I have uploaded this dataset so that you can also do your own analysis.
- README.md: Project documentation and Information.

## Requirements
- Python
- Pandas
- Matplotlib
- Seaborn

## Setup
1. Install the relevant dependencies
    ```
    pip install pandas numpy seaborn matplotlib plotly openpyxl
    ```
2. Run the python script
   ```
   python salesdataset_analysis.py
   ```
> **Note**: Ensure all dependencies are installed before running the project.
> ## Notes
- If the file path is different, update the `file_path` variable in the script to point to the correct location of `shopping_trends_updated.csv`.

## License
This project is licensed under the MIT License.


## Data Description
The dataset used in this project includes the following columns:

| Column Name            | Description                                      |
| ---------------------- | ------------------------------------------------ |
| **Customer ID**        | Unique identifier for each customer              |
| **Age**                | Age of the customer                              |
| **Gender**             | Gender of the customer                           |
| **Item Purchased**     | Name of the item purchased                       |
| **Category**           | Product category                                 |
| **Purchase Amount (USD)** | Amount spent on the purchase                  |
| **Location**           | Location of the customer                         |
| **Size**               | Size of the product                              |
| **Color**              | Color of the product                             |
| **Season**             | Season during which the purchase was made        |
| **Review Rating**      | Customer's review rating for the product         |
| **Subscription Status** | Whether the customer is subscribed or not       |
| **Shipping Type**      | Type of shipping chosen                          |
| **Discount Applied**   | Whether a discount was applied                   |
| **Promo Code Used**    | Whether a promo code was used                    |
| **Previous Purchases** | Number of previous purchases made by the customer|
| **Payment Method**     | Payment method used                              |
| **Frequency of Purchases** | Frequency of the purchases made             |

## Analysis
    The script performs the following analyses:
    
    - > Filtering Data
    
    - > Demography related questions
    
    - > Visualizing data using Matplotlib and Seaborn

## Visualizations

### Age Distribution

Here is a visualization of the age distribution of customers:

![Age Distribution Histogram](https://github.com/user-attachments/assets/505a6e58-c03b-4e9b-89f7-3156d29d3357)


### Purchase Trends

Below is a chart showing the average purchase amount by product category:

![Average Purchase Amount by Category](https://github.com/user-attachments/assets/24f2403e-742b-441e-a91a-7a4f05183dfb)



