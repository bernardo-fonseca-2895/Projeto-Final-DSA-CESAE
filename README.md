# VIDEOGAME SALES OVER THE YEARS

**THIS IS THE FINAL PROJECT FOR THE DATA SCIENCE & ANALYTICS COURSE TAKEN IN CESAE DIGITAL**

**OBJECTIVE:** Demonstrate competences in the area of Data Analysis, such as Python/R programming, SQL/Database managing
and Excel/PowerBI Data Visualization

**Material:** 'vgsales.csv'

# PHASE 1 - BUSINESS
**DEFINE BUSINESS QUESTION AND OBJECTIVES**

**Business Question:** Which videogame genres and platforms generate more revenue per region and how has the market
evolved over time?

**Criteria for success:**
1. Being able to recognize which genres generated more global revenue per decade, to decide in which type of game to invest for the next generation;
2. Recognizing how the market quota for platforms evolved across the decades to identify cycles of dominance and/or hardware tendencies;
3. Knowing which videogame genres sell more per region (NA, EU, JP) to ajust stock and marketing campaigns per region.

# PHASE 2 - DATA
**EXTRACT AND TRANSFORM DATA**

**Source of the dataset:** Video Game Sales - Kaggle

**Link:** https://www.kaggle.com/datasets/gregorut/videogamesales

# PHASE 3 - CLEANING

**CLEAN FILTER AND TRANSFORM DATASET**
1. Import csv file to Power Query (Used Excel but can also use Power BI);
2. Filter out the N/A and unkown values from column Publisher and Date;
3. Filter out outlier (A single row that has the date 2020);
4. Substitute . for , on sales columns;
5. Alter types to correct typing on sales collumns;
6. Add new column from example (Use date column to create decade column);
7. Add new personalized column Global_Sales Revised by adding NA, EU, JP and Others Sales;
8. Alter type to decimal on new column;
9. Save and load to Excel as table ready to use.
