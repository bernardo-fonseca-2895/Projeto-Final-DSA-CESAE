# VIDEOGAME SALES OVER THE YEARS

**THIS IS THE FINAL PROJECT FOR THE DATA SCIENCE & ANALYTICS COURSE TAKEN IN CESAE DIGITAL**

**OBJECTIVE:** Demonstrate competences in the area of Data Analysis, such as Python/R programming, SQL/Database managing
and Excel/PowerBI Data Visualization

**OUR PIPELINE:** data -> Excel PowerQuery (cleaning) -> Python (cleaning + analysis) -> Excel Dashboard

**TEAM AND RESPONSIBILITIES:**
1. Bernardo Pina Fonseca - Data Cleaning (Python), Analysis, Coordination
2. Miguel Fonseca Pina - Data Cleaning (Excel PowerQuery), Dashboard (Excel)


# PHASE 1 - BUSINESS
**DEFINE BUSINESS QUESTION AND OBJECTIVES**

**Business Question:** Which videogame genres and platforms generate more revenue per region and how has the market
evolved over time?

**Criteria for success:**
1. Being able to recognize which genres generated more global revenue per decade, to decide in which type of game to invest for the next generation;
2. Recognizing how the market quota for platforms evolved across the decades to identify cycles of dominance and/or hardware tendencies;
3. Knowing which videogame genres sell more per region (NA, EU, JP) to ajust stock and marketing campaigns per region.

# PHASE 2 - DATA
**EXTRACT AND EXPLORE DATA**

**Material:** 'vgsales.csv'

**Source of the dataset:** Video Game Sales - Kaggle

**Link:** https://www.kaggle.com/datasets/gregorut/videogamesales

**SIZE:** ~16.5K lines, 11 columns: Rank, Name, Platform, Year, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

# PHASE 3 - PREPARATION
**CLEAN, FILTER AND TRANSFORM DATASET**
1. Download data and place `vgsales.csv` in `data/raw/` 
2. Upload `vgsales.csv` file to Excel PowerQuery;
3. Filter out the N/A and Unknown values from columns "Publisher" and "Year";
4. Filter out the outlier (A single row in the column "Year" = 2020);
5. Substitute . for , on all Sales columns;
6. Alter data type to Decimal Number on all Sales columns;
7. Add new column from example (Use Year column to create "Decade" column by typing the respective starting year of the decade on the first two lines followed by an "-s" so Excel can fill the rest of the lines);
8. Add new personalized column "Global_Sales_Verified" by adding the columns "NA_Sales", "EU_Sales", "JP_Sales" and "Others_Sales";
9. Alter data type to Decimal Number on new column;
10. Save and load to Excel as table on existing spreadsheet;
11. Rename existing spreadsheet to "vgsales";
12. Save as `vgsales_fase1.xlsx` and place the file in `data/1stCleaningPhase/`
13. Open VSCode, click File -> Open Folder -> Projeto-Final-DSA-CESAE
14. Install dependencies: `pip install -r requirements.txt`
15. Run the python cleaning script: `python src/limpeza.py`
16. Run the analysis script: `python src/analise.py`
17. Dashboard: Open `data/processed/vgsales_processed.csv` in Excel (see `reports/relatorio.md`)

# PHASE 4 - ANALYSIS
**ANSWERING THE BUSINESS QUESTION AND USER STORIES**

*(REAL RESULTS OBTAINED FROM THE DATASET)*

**TOTAL GLOBAL SALES:** ~8973.63 M units sold in 4 decades, between 11246 videogame entries, distributed by ~575 publishers and 31 different platforms

**MOST POPULAR GENRES IN THE LAST DECADE:** Action (671 M), Shooter (462 M), Sports (325 M), Role-Playing (302 M)

**MOST POPULAR HARDWARE MANUFACTURERS:** Sony (40.4%), Nintendo (37.6%), Microsoft (13.9%)

**MOST POPULAR GENRES PER REGION:** **NA:** Action (861 M); **EU:** Action (516 M); **JP:** Role-Playing (349 M); **OTHERS**: Action (185 M)

# PHASE 5 - EVALUATION
**VALIDATING RESULTS & LIMITATIONS**

- ~300 lines with null/unknown values in columns "Year" and "Publisher": opted to remove due to low impact on final results;
- Sales columns measured in units sold, not revenue generated: good for measuring popularity, not so much to measure profit;
- Some lines in column "Publisher" have typos in their names: not impactful in the end results, look to correct in the future;
