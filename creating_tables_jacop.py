# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 09:45:14 2015

@author: keriambermudez
"""

import pandas as pd
import csv
import re
from pandas import DataFrame
import os
import pandas as pd
import numpy as np

path = "F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Jacop_csvs_our_thr\\"
#%%
basal = pd.read_csv("F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Our_Thr_Basal_Log_files\\Our_Thr_Basal_jacop.csv")
bleomycin = pd.read_csv("F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Our_Thr_Bleomycin_Log_files\\Our_Thr_Bleomycin_jacop.csv")

#%%
icq = DataFrame([basal.ix[:,'43'],bleomycin.ix[:,'43']], index=['basal','bleomycin'])
icq = icq.transpose()
icq.to_csv(path+"ICQ.csv")

pearsons = DataFrame([basal.ix[:,'3'],bleomycin.ix[:,'3']], index=['basal','bleomycin'])
pearsons = pearsons.transpose()
pearsons.to_csv(path+"pearsons.csv")

overlap_coef = DataFrame([basal.ix[:,'5'],bleomycin.ix[:,'5']], index=['basal','bleomycin'])
overlap_coef = overlap_coef.transpose()
overlap_coef.to_csv(path+"overlap_coef.csv")

M1 = DataFrame([basal.ix[:,'16'],bleomycin.ix[:,'16']], index=['basal','bleomycin'])
M1 = M1.transpose()
M1.to_csv(path+"M1.csv")

M2 = DataFrame([basal.ix[:,'17'],bleomycin.ix[:,'17']], index=['basal','bleomycin'])
M2 = M2.transpose()
M2.to_csv(path+"M2.csv")



