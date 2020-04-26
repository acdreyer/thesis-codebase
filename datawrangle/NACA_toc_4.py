from datetime import datetime
import re
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import json
import pprint
pp = pprint.PrettyPrinter(indent=0)
import matplotlib.pyplot as plt
import csv
from fuzzywuzzy import process


# define the input files; these are OCR with header/intro and footer stripped
toc_49 = "./indexes/1915-1949_toc_lc_content.txt"
toc_51 = "./indexes/1949-1951_toc_lc_content.txt"
toc_53 = "./indexes/1949-1953_toc_uc_content.txt"
toc_54 = "./indexes/1953-1954_toc_uc_content.txt"
toc_55 = "./indexes/1954-1955_toc_uc_content.txt"
toc_56 = "./indexes/1955-1956_toc_uc_content.txt"
toc_57 = "./indexes/1956-1957_toc_uc_content.txt"
toc_58 = "./indexes/1957-1958_toc_uc_content.txt"
toc1=toc_49
toc2=toc_51
toc3=toc_53
toc4=toc_54
toc5=toc_55
toc6=toc_56
toc7=toc_57
toc8=toc_58

# the file being handled; change from toc1-toc8 manually 
# (yea I know; cumbersome) such is data cleaning
fname = toc3


# init and triggers
headings = {}
nacaWebHeads = 'NACA_subjectHeadings.csv'
untjsonData = 'naca_data.json'
untplotData = 'testplot.csv'
ocrTitleHeads = fname
# note; the replace might be misleading to think one is used to generate the other
# which is not the case, its just to not have to write the names twice...
subjRepNos = fname.replace('content','subjRepNos')



df_shd = pd.read_csv(nacaWebHeads, sep=',',header=None)
#print(dfheads.values[:,0])
df_ocr = pd.read_csv(fname, sep=',',quotechar='|',header=None)
#print(df_toc.values[:,1])
df_unt = pd.read_csv(untplotData, sep=',',header=None)
#print(df_unt.head)



#if fname.find('_toc_lc') != -1:
##    filtlen = 30
#    print('cant get report numbers that werent originally in brackets')
#else:
df_ocrRepno = pd.read_csv(subjRepNos, sep=',',header=None)
#    print(df_ocrRepno.head)
print(df_ocrRepno.values[:,0])

for rowOcr in df_ocrRepno:
    print(rowOcr)
#        for rowDB in df_unt:
#            print(rowDB)
#            for repClean in rowDB['id_repno2']:
                










#print(data)

#for row in df_toc.values:
#    print(row[1])




#str2Match = "apple inc"
#strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]
#Ratios = process.extract(str2Match,strOptions)
#print(Ratios)
## You can also select the string with the highest matching percentage
#highest = process.extractOne(str2Match,strOptions)
#print(highest)















