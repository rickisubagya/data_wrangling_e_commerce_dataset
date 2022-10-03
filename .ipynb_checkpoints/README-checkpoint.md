# This is a simple repository for practice in the data wrangling

## The Data Source

### Sales Datasets

You can download the dataset from this [link](https://docs.google.com/document/d/1v33dd7tNS6pYoUXp32GO1YyW1LpxuvDMuFJmKOYJdsY/edit), the Sales datasets consist of:

- Customers Dataset
- Orders Dataset
- Order Review Dataset
- Order Items Dataset
- Product Dataset
- Sellers Dataset

Here is the relation between Sales datasets

![Untitled](Easy%20Report%2052852b68a86a447aaa2a39f27d35c205/Untitled.png)

The data wrangling process for Sales datasets:

- Convert into DateTime format
- Sort value
- Input missing value
- Merge datasets
- Drop some rows
- Convert value into title case

You can check the documentation in the helper folder, feature_engineering_sales_performance.py

### Marketing Datasets

You can download the dataset from this [link](https://docs.google.com/document/d/1OCgfp8fGf9QSAEVtb8qNWspVGORqNWhx-uEy3KoD4Yc/edit), the data wrangling process for marketing datasets:

- Convert into DateTime format
- Rename column name
- Input missing value
- RFM segmentation

You can check the documentation in the helper folder, feature_engineering_marketing.py

### A/B Testing Datasets

You can download the dataset from this [link](https://docs.google.com/document/d/1V7O6xiJ0wH5h3ddBK4Ji0vcD_6DNuXuKWb-yxRw28Ww/edit), the data wrangling process for a/b testing datasets:

- Convert into DateTime format
- Make sure if the control group visit the old page and the treatment group visits the new page
- Drop duplicate user-id
- Group data by date and separate the control and treatment
- Calculate the conversion rate for group control and treatment
- Calculate the power
- Calculate the p-value

You can check the documentation in the helper folder, feature_engineering_ab.py

- If you want to read the full story of this project please visit my [medium](https://medium.com/@rickisubagya/e-commerce-dashboard-37202f02e940) story
- If you want to see the E-Commerce Dashboard that I have created please visit my [Tableau](https://public.tableau.com/app/profile/ricki.subagya/viz/IhKamesdashboard/C-Level) Dashboard
- Let’s connect with my [LinkedIn](https://www.linkedin.com/in/rickisubagya/) account