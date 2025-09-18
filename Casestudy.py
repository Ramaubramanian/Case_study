#Extracting the players from the dataset
#Filtering the players from Mumbai Indians and the Royal Challengers Bengaluru
#Filtering V Kohli from RCB team and JJ Bumrah from MI team
#Analyzing Bumrah vs other Batters
#Analyzing Kohli vs other Bowlers
#Scatter Plot to describe a conclusion

# Step 1
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', None)
#pd.set_option('max_colwidth', -1)
# Reading the dataset
df = pd.read_csv('deliveries.csv')
df.head()
