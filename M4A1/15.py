'''Analyse various school outcomes in Tennessee using pandas. Suppose you are a
public school administrator. Some schools in your state of Tennessee are
performing below average academically. Your superintendent, under pressure
from frustrated parents and voters, approached you with the task of understanding
why these schools are under-performing. To improve school performance, you
need to learn more about these schools and their students, just as a business needs
to understand its own strengths and weaknesses and its customers. Though you is
eager to build an impressive explanatory model, you know the importance of
conducting preliminary research to prevent possible pitfalls or blind spots. Thus,
you engages in a thorough exploratory analysis, which includes: a lit review, data
collection, descriptive and inferential statistics, and data visualization.
Phase 1 - Data Collection
Here is a data of every public school in middle Tennessee. The data also includes
various demographic, school faculty, and income variables. You need to convert the
data into useful information.
• Read the data in pandas data frame
• Describe the data to find more details
'''

import pandas as pd
df1=pd.read_csv("./M4A1/middle_tn_schools.csv")
print(df1)
print(df1.describe())