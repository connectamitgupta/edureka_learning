'''Domain – Education
focus – Data analysis
Business challenge/requirement
You are a data analyst with University of Cal USA (Not a machine learning expert yet
as you still have not completed ML with Python Course :-)).The University has data of
Math, Physics and Data Structure score of sophomore students. This data is stored in
different files. The University has hired a data science company to do analysis of
scores and find if there is any correlation of score with age, ethnicity etc. Before the
data is given to the company you have to do data wrangling.
Key issues
Ensure students identify is not revealed to the agency and only relevant data is
shared
Considerations
NONE
Data volume
- In thousands, but only around 1800 records are shared in files MathScoreTerm1.csv
DSScoreTerm1.csv, PhysicsScoreTerm1.csv
Additional information
- NA
Business benefits
University can get more students enrollment by improving its international ranking
through personalized course/curriculum for students
Approach to Solve
You have to use fundamentals of Numpy and Pandas covered in module 4.
1. Read the three csv files which contains the score of same students in term1 for
each Subject
2. Remove the name and ethnicity column (to ensure confidentiality)
3. Fill missing score data with zero
4. Merge the three files
5. Change Sex(M/F) Column to 1/2 for further analysis
6. Store the data in new file – ScoreFinal.csv
Enhancements for code
You can try these enhancements in code
1. Convert ethnicity to numerical value
2. Fill the missing score for a student to the average of the class
'''
import numpy as np
import pandas as pd

## Reading data from CSV files
math_df1=pd.read_csv("./M4A2/MathScoreTerm1.csv")
ds_df1=pd.read_csv("./M4A2/DSScoreTerm1.csv")
physics_df1=pd.read_csv("./M4A2/PhysicsScoreTerm1.csv")


## Replace data with average values in score columns
math_df1['Score'].replace([np.nan], math_df1['Score'].mean(), inplace=True)
ds_df1['Score'].replace([np.nan], ds_df1['Score'].mean(), inplace=True)
physics_df1['Score'].replace([np.nan], physics_df1['Score'].mean(), inplace=True)


# print(math_df1.columns)
# print(ds_df1.columns)
# print(physics_df1.columns)

## Rename score column name so that whle merging these dataframe can be easily identified 
math_df1['Maths_Score']=math_df1['Score']
ds_df1['DS_Score']=ds_df1['Score']
physics_df1['Physics_Score']=physics_df1['Score']

# print(math_df1.columns)
# print(ds_df1.columns)
# print(physics_df1.columns)

## Merging these 3 dataframes on the basis of multiple columns
sf1=math_df1.merge(ds_df1,on=['Name','Age','Sex','Ethinicity']).merge(physics_df1,on=['Name','Age','Sex','Ethinicity'])
# print(sf1.columns)
sf1=sf1[['Name','Age','Sex','Ethinicity','Maths_Score','DS_Score','Physics_Score']]
# sf1.drop(sf1.columns.difference(['Age','Maths_Score','DS_Score','Physics_Score']), 1, inplace=True)

# print(sf1.columns)

# sf1.to_csv("ScoreFinal1.csv")

## Replace male and female with binary
sf1['Sex'] = sf1['Sex'].map({'M': 1, 'F': 0})
# eth=sf1['Ethinicity'].unique()
# print(eth)
sf1['Ethinicity'] = sf1['Ethinicity'].map({'White American':0, 'European American':1, 'Hispanic':2, 'African American':3})
sf1=sf1.drop(['Name'],axis=1)
## Exporting merged dataframes to CSV output
sf1.to_csv("./M4A2/ScoreFinal.csv")
