
# This script reads in OCR text data subject headings in the lowercase format
# and splits it into meaningful files. 1915-1953.

# the first part cleans up the data by removing linebreaks over the report
# number lines, in order to identify and extract report numbers. 
# It is probably easier to extract report numbers while not all line breaks
# have been removed, but just the line-breaks that break a report number into 
# two lines.
# It was found to be difficult to extract report numbers without brackets, 
# hence full paragraphs were subsequently needed to be cleaded up.
#
# More scripts need to be run on these files to convert them into usable variables



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



# define the input files; these are OCR with header/intro and footer stripped
toc_49 = "./indexes/1915-1949_toc_lc.txt"
toc_51 = "./indexes/1949-1951_toc_lc.txt"

toc1=toc_49
toc2=toc_51


# the file being handled; change from toc1-toc8 manually 
# (yea I know; cumbersome) such is data cleaning
fname = toc1

iii=0;

# strip linebreaks from file where it spans across report numbers so that
# report numbers can be identified.
# filename
fname_1 = fname.rstrip('.txt')+'_repNoLines2.txt'
with open(fname) as fr:
    with open(fname_1, 'w') as f1:
        lines = fr.readlines()
        for i, line in enumerate(lines):
            if (line.find('NACA\n') != -1) or (line.find('NACA \n') != -1)\
            or (line.find("Rept.\n") != -1) or (line.find("Rept. \n") != -1)\
            or (line.find('TN\n') != -1) or (line.find('TN \n') != -1)\
            or (line.find('TM\n') != -1) or (line.find('TM \n') != -1)\
            or (line.find('WR\n') != -1) or (line.find('WR \n') != -1)\
            or (line.find('AC\n') != -1) or (line.find('AC \n') != -1)\
            or (line.find('RM\n') != -1) or (line.find('RM \n') != -1)\
            or (line.find('ACR\n') != -1) or (line.find('ACR \n') != -1)\
            or (line.find('ARR\n') != -1) or (line.find('ARR \n') != -1)\
            or (line.find('CB\n') != -1) or (line.find('CB \n') != -1)\
            or (line.find('RB\n') != -1) or (line.find('RB \n') != -1)\
            or (line.find('MR\n') != -1) or (line.find('MR \n') != -1)\
            or ((line.find('and\n') != -1) and (lines[i+1] == '\n'))\
            or ((line.find('and \n') != -1) and (lines[i+1] == '\n'))\
            or ((line.find(':\n') != -1) and (lines[i+1] == '\n')):
                templine = line.strip('\n')
                print('linebreak removed at'+templine)
                f1.write(templine)
            else:
                f1.write(line)
                
# close the files; will be needed            
fr.close()
f1.close()       
    
# extract brackets only
fname_2 = fname.rstrip('.txt')+'_repNoLines3.txt'
#regexp = re.compile(r"^([^()]|\([^()]+\))+$")


#parNos = [];

# do the files with lowercase names; 
# these have a slightly different formatting than the rest
if fname[-6:-4] =='lc':
    with open(fname_1) as fr:
        with open(fname_2, 'w') as f2:
            lines = fr.readlines()
            for i, line in enumerate(lines[:-1]):
                if (lines[i+1] == '\n') and (line != '\n') and (len(line)>2): 
                    if (line[-3] != '.') and (line.find("(") == -1)\
                    and (line.find(")") == -1) and (len(line) > 5)\
                    and (line.find(',') != -1):
#                if ((line.find("(") != -1) and (line.find(")") != -1)):
#                    templine=line[line.find("(")+1:line.find(")")]
#                    print(templine)
#                    f2.write(templine+'\n')
                        templine = line.strip('\n')
                        print('linebreak removed at'+templine)
                        f2.write(templine)
                    elif (line.find("(") != -1) and (line.find(")") != -1) :
                        f2.write(line+'\n')
                    else: f2.write(line)
                else:
                    f2.write(line)
                    iii=iii+1;

#.  ,
#TM
#TN
#ACR
#MR 
#RM
#ARR
#Rept.
#Rept
#CB
#WR
#RB







print(fname)
print(iii)
#fadd = open(fnamew, "r")
#for x in fadd:
#  print(x)
  
