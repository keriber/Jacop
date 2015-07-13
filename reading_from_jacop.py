# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:50:27 2015

@author: keriambermudez
"""

import pandas as pd
import os

path = 'F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Our_Thr_Basal_Log_files\\'

#%%
tables = []
for i in os.listdir(path):
    print(i)
    table = pd.read_table(path+i,sep='\n',header=None,names=[i[:-8]],skiprows= 1 )
    print(table)
    table = table.transpose()
    tables.append(table)

all_table = pd.concat(tables) 


#%%
#string 2 to 8 
#Pearson's Coefficient:, Overlap Coefficient, Overlap Coefficient:threshold
string_2_8 = [3,5,11]
#string_3_8 = [10,11,20,21,24,25,28,29]
# k1,k2,
string_3_8 = [7,8,13,14,16,17,19,20]

for i in string_2_8:
    test = all_table.ix[:,i].str[2:8]
    test = test.str.replace('(',' ')
    test = test.astype(float)
    all_table.ix[:,i]= test
    all_table.ix[:,i]
    
for i in string_3_8:
    test = all_table.ix[:,i].str[3:8]
    test = test.str.replace('(',' ')
    test = test.astype(float)
    all_table.ix[:,i]= test
    all_table.ix[:,i]

icq = all_table.ix[:,43].str[5:]
all_table.ix[:,43]= icq
all_table.columns = all_table.columns.astype(int)

#%%
all_table.to_csv('F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Our_Thr_Bleomycin_Log_files\\Our_Thr_Basal_jacop.csv')

#%%
   
excel_file ='F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Basal_Testing_Jacob_with_thresholded.xls'

xls_file = pd.ExcelFile (excel_file)
bleomycyn = xls_file.parse('Bleomycyn')
bleomycyn = bleomycyn.dropna()
bleomycyn = bleomycyn.transpose()
bleomycyn_orig = bleomycyn.transpose()


#string 2 to 8 
string_2_8 = [4,7,17]
#string_3_8 = [10,11,20,21,24,25,28,29]
string_3_8 = [10,11,20,21,24,25,28,29]

for i in string_2_8:
    test = bleomycyn.ix[:,i].str[2:8]
    test = test.replace('0.0 (','0.0')
    test = test.astype(float)
    bleomycyn.ix[:,i]= test
    bleomycyn.ix[:,i]
    
for i in string_3_8:
    test = bleomycyn.ix[:,i].str[3:8]
    test = test.replace('0.0 (','0.0')
    test = test.astype(float)
    bleomycyn.ix[:,i]= test
    bleomycyn.ix[:,i]

bleomycyn.columns = bleomycyn.columns.astype(str)
columns_names = {'4': 'Pearsons Coefficient:', '6': 'Overlap Coefficient:','10':'K1','11':'K2','17':'Thres Overlap Coe', '20':'Thre K1', '21':'Thre K2','24':'M1', '25':'M2','28':'Thre M1', '29': 'Thre M2'}
bleomycyn = bleomycyn.rename(columns=columns_names)


   
bleomycyn.to_csv('F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Bleomycyn_Testing_Jacob_thresholded.csv')

bleomycyn_orig.to_csv('F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Bleomycyn_Testing_Jacob_not_cleaned_thresholded.csv')

#BssalData

basal = xls_file.parse('Basal')
basal = basal.dropna()
basal = basal.transpose()
basal_orig = basal.transpose()
#string 2 to 8 
string_2_8 = [4,7,17]
#string_3_8 = [10,11,20,21,24,25,28,29]
string_3_8 = [10,11,20,21,24,25,28,29]

for i in string_2_8:
    test = basal.ix[:,i].str[2:8]
    test = test.replace('0.0 (','0.0')
    test = test.astype(float)
    basal.ix[:,i]= test
    
    
for i in string_3_8:
    test = basal.ix[:,i].str[3:8]
    test = test.replace('0.0 (','0.0')       
    test = test.astype(float)
    basal.ix[:,i]= test
    

basal.columns = basal.columns.astype(str)
columns_names = {'4': 'Pearsons Coefficient:', '6': 'Overlap Coefficient:','10':'K1','11':'K2','17':'Thres Overlap Coe', '20':'Thre K1', '21':'Thre K2','24':'M1', '25':'M2','28':'Thre M1', '29': 'Thre M2'}
basal = basal.rename(columns=columns_names)



basal.to_csv('F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\basal_Testing_Jacob_thresholded.csv')

basal_orig.to_csv('F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\basal_Testing_Jacob_not_cleaned_thresholded.csv')

#del basal['0']
#
#all_vals = []
#for i in basal.columns:
#    basal_series = basal[i]
#    bleomycyn_series = bleomycyn[i]
#    all_vals.append(basal_series)
#    all_vals.append(bleomycyn_series)
#    
#pd.concat(all_vals,axis=1)