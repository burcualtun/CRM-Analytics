
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

#Kontrol grubuna Max Bidding
#Test Grubuna Avg Bidding uygulandı

#Görev1
#Adım1
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

#Görev3
#Normallik testi yapılır
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df.loc[df["Group"] == "C", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["Group"] == "T", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Sonuç Normaldir.

#Varyans homojenliği testi yapılır.
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df.loc[df["Group"] == "C", "Purchase"],
                           df.loc[df["Group"] == "T", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Ho reddedilemez. Varyans homojenliği kabul edilir.

#Bu sonuçlara göre bağımsız iki örneklem t testi yapılır.

test_stat, pvalue = ttest_ind(df.loc[df["Group"] == "C", "Purchase"],
                           df.loc[df["Group"] == "T", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Sonuca istinaden M1=M2 hipotezi reddedilemez. Control ve Test verilerinin purchase ortalamaları arasında anlamlı
#Fark yoktur. Yani değişim işe yaramamıştır.

#Görev4

# Normallik ve varyans homojenliği sağlandığı için  bağımsız iki örneklem t testi kullanılımıştır.
#Bu testin sonucunda da p değeri 0.05'ten küçük olmadığı için en başta kurulan hipotez reddedilemez.
#Matematiksel olarak MaxBidding Purchase ortalaması ile Avg Bidding Purchase ortalaması 550 vs 580 idi.
#Burada anlamlı bir fark var gibi görülmesine rağmen yapılan test sonuçlarında bu farkın tesadüfi olduğu gözlemlendi.

#Biraz daha uzun süre gözlem yapılara yeni veriler de araştırmaya dahil edilebilir.

