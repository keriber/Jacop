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

#%%

path = "C:\\Users\\keriambermudez\\Dropbox\\David_Fenyos_Lab\\Image_Analysis\\Testing_Jacop\\Basal_bleomycin_masked_cvs\\"


#%%

basal = pd.read_csv("C:\\Users\\keriambermudez\\Dropbox\\David_Fenyos_Lab\\Image_Analysis\\Testing_Jacop\\Basal\\Masked_log_files\\Basal_masked_jacop.csv")
bleomycin = pd.read_csv("C:\\Users\\keriambermudez\\Dropbox\\David_Fenyos_Lab\\Image_Analysis\\Testing_Jacop\\Bleomycyn\\Masked_log_files\\Bleomycin_masked_jacop.csv")

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



