#DataSet Info : This data set, which includes a company's website information, includes information such as the number of ads users saw and clicked, as well as 
#earnings information from here. There are two separate data sets as Control and Test group. These data sets
#ab_testing.xlsx are located on separate pages of excel. Maximum Bidding to the control group, Average to the test group Bidding implemented

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#Control Group Max Bidding
#Test Group Avg Bidding 


#Load and Analyze Data

df_conrol = pd.read_excel("W4/HW1/ab_testing.xlsx",sheet_name="Control Group")
#df_conrol.columns=["C_Impression","C_Click","C_Purchase","C_Earning"]
df_conrol["Group"]="C"
df_test = pd.read_excel("W4/HW1/ab_testing.xlsx",sheet_name="Test Group")
#df_test.columns=["T_Impression","T_Click","T_Purchase","T_Earning"]
df_test["Group"]="T"
#Adım2

df_conrol.head()
df_test.head()

df_conrol.describe()
df_test.describe()

#Adım3
frames = [df_conrol,df_test]
df=pd.concat(frames,axis=0)
df.head(50)

#Görev2
#Adım1
#H0 : M1=M2
#H1 : M1 != M2

#Adım2
df.groupby("Group").agg({"Purchase":"mean"})

#Normality test

#H0 : M1 = M2 
#H1 : M1!= M2

test_stat, pvalue = shapiro(df.loc[df["Group"] == "C", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["Group"] == "T", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Test Result is Normal.

#Variance homogeneity test

# H0: Variances are Homogeneous
# H1: Variances are not Homogeneous

test_stat, pvalue = levene(df.loc[df["Group"] == "C", "Purchase"],
                           df.loc[df["Group"] == "T", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Ho cannot be denied. Variance homogeneity is accepted.

#According to these results, an independent two-sample t-test is applied.

test_stat, pvalue = ttest_ind(df.loc[df["Group"] == "C", "Purchase"],
                           df.loc[df["Group"] == "T", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Based on the result, the hypothesis M1=M2 cannot be rejected. 
#There is no significant difference between the purchase averages of the Control and Test data. So the change didn't work.

#Results

# Independent two-sample t-test was used to ensure normality and homogeneity of variance. 
#Since the p value is not less than 0.05 as a result of this test, the original hypothesis cannot be rejected.
#Mathematically, the Avg Bidding Purchase average was 550 vs 580 with the MaxBidding Purchase average.
#Although there seems to be a significant difference here, it was observed that this difference was coincidental in the test results.

#New data for slightly longer observation structures can also be included in the research.

