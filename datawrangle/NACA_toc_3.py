
# This script reads in OCR text data that went through a first cleaning process
# to remove line breaks and some irregularies to now give a structured output 
# to the text by removing all linebreaks across paragraphs and group into
# meaningful sections. Some repition of code is here in the part that 
# extracts the heading lines (same as NACA_toc_1.py). Ideally this should be 
# done in a separate function...

# the outputs are data structured in csv files.



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
import sys


# define the input files; these are OCR with header/intro and footer stripped
toc_49 = "./indexes/1915-1949_toc_lc_repNoLines3.txt"
toc_51 = "./indexes/1949-1951_toc_lc_repNoLines3.txt"
toc_53 = "./indexes/1949-1953_toc_uc_repNoLines.txt"
toc_54 = "./indexes/1953-1954_toc_uc_repNoLines.txt"
toc_55 = "./indexes/1954-1955_toc_uc_repNoLines.txt"
toc_56 = "./indexes/1955-1956_toc_uc_repNoLines.txt"
toc_57 = "./indexes/1956-1957_toc_uc_repNoLines.txt"
toc_58 = "./indexes/1957-1958_toc_uc_repNoLines.txt"
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

fname = toc1    # <<======== CHANGE THIS fname


# init and triggers
iii=0;
allsections = [];
allSec2 = { 'sec': [], 'line': []}
#thissection = []
buffer = []
newSecTrigger = False
subjLineTrigger = False


# strip linebreaks from file where it spans across report numbers so that
# report numbers can be identified.


# filename
fname_1 = fname.replace('repNoLines','paragraphs')

with open(fname) as fr:
    with open(fname_1, 'w') as f1:
        lines = fr.readlines()
        
        for i, line in enumerate(lines):
            subjLineTrigger = False            
            # extract the subject heading numbers and paragraphs
            if ((line.find("(") != -1) and (line.find(")") != -1))\
            and (line.find(". \n") == -1) and (line.find("NACA") == -1)\
            and (line.find("(ii)") == -1) and (line.find("(i)") == -1)\
            and (line.find("(WR") == -1) and (line.find("Rept.") == -1)\
            and (line.find("(Revised)") == -1) and (line.find("Rept.") == -1)\
            and (line.find("(10-PERCENT") == -1) and (line.find("Rept.") == -1)\
            and (line.replace(' ','').find("(M=1.53)") == -1) :
                
                #found a line with subject heading number
                if (line.find('1.') != -1) or (line.find('2.') != -1) or\
                (line.find('3.') != -1) or (line.find('4.') != -1) or\
                (line.find('5.') != -1) or (line.find('6.') != -1) or\
                (line.find('7.') != -1) or (line.find('8.') != -1) or\
                (line.find('9.') != -1) or (line.find('0.') != -1) or\
                (line.find('(1') != -1) or (line.find('(2)') != -1) or\
                (line.find('(3)') != -1) or (line.find('(4)') != -1) or\
                (line.find('(5)') != -1) or (line.find('(6)') != -1) or\
                (line.find('(7)') != -1) or (line.find('(8)') != -1) or\
                (line.find('(9)') != -1) or (line.find('(4)') != -1):
                    subjLineTrigger = True
                    templine = line[line.find("(")+1:line.find(")")]
                    templine = templine.replace(',','.')
                    templine = templine.replace(' ','')
                    templine = templine.replace('l.','1.')
                    templine = templine.replace('.l','.1')
                    templine = templine.replace('.I','.1')
                    templine = templine.replace('I.','1.')
                    templine = templine.rstrip('.')
#                    print(templine)
                    if templine not in allsections:
                        newSecTrigger = True
                        thissection = templine.rstrip('\n');
                        allsections.append(thissection)
                        allSec2['sec'].append(thissection)
                        allSec2['line'].append(i)
                        f1.write('\n')
                        f1.write('\n')
                        f1.write('----------'+templine+'\n')
#                        iii=iii+1;
                        
#------------extract the paragraph
            if not subjLineTrigger:
                if (line.rstrip(' ') == '\n'):
                    f1.write(line+'\n')
                elif (line.find("Cont.") != -1) or (line.find("Cont .") != -1):
                    f1.write('\n')
                else:
                    templine = line.rstrip(' ')
                    templine = templine.rstrip('\n')                        
                    f1.write(templine)                         
#print(allSec2)
#print(len(allSec2['sec']))
#print(len(allSec2['line']))

# close the files; will be needed            
#fr.close()
#f1.close()       
#    
#
                    
      

# now extract the contents              
fname_2 = fname_1.replace('paragraphs','content')
fname_2 = fname_2.replace('ent3','ent')

#regexp = re.compile(r"^([^()]|\([^()]+\))+$")


if fname_2.find('1915-1949_toc_lc') != -1:
    filtlen = 30
else:
    filtlen = 40

# now extract the structure

firstFind = False
with open(fname_1) as fr:
    with open(fname_2, 'w') as f2:
        
        f2.write('|ocrSubjNumT|,|ocrTitle|\n')
        lines = fr.readlines()
        for i, line in enumerate(lines):
            
            subjBool=False
            if (line.find("----------") != -1):
                subjNum = line.strip('----------')
                subjNum = subjNum.strip('\n')
                subjBool=True
                firstFind=True
            elif (len(line)<filtlen) and (line != '\n'):
                print('remove ' + line)
            elif not firstFind:
                print('remove ' + line)                
            elif (len(line) > 10):
                templine=line.rstrip('\n')
#  use the | character as csv string mark instead of " because data is full of "
                f2.write('|'+subjNum+'|,|'+templine+'|\n')
fr.close()
f2.close()






# also extract the subject headings. This is only done for uppercase files              
fname_read = fname.replace('repNoLines','repNos')
fname_write = fname_read.replace('repNos','subjRepNos')

#regexp = re.compile(r"^([^()]|\([^()]+\))+$")


if fname.find('_toc_lc') != -1:
#    filtlen = 30
    sys.exit('cant get report numbers that werent originally in brackets')
else:
    filtlen = 2

# now extract the structure
newSecTrigger = False
subjLineTrigger = False
firstFind = False
with open(fname_read) as fr:
    with open(fname_write, 'w') as f3:
        
        f3.write('"ocrSubjNumR","ocrRepNo"\n')
        lines = fr.readlines()
        for i, line in enumerate(lines):
            
            subjBool=False
            if (line.find("----------") != -1):
                subjNum = line.strip('----------')
                subjNum = subjNum.strip('\n')
                subjBool=True
                firstFind=True
            elif (len(line)<filtlen) and (line != '\n'):
                print('remove ' + line)
            elif not firstFind:
                print('remove ' + line)                
            elif (len(line) > 10):
                templine=line.rstrip('\n')
                f3.write('"'+subjNum+'","'+templine+'"\n')
fr.close()
f3.close()















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






print(fname_1)
print(iii)

  
