
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

fname = toc8   # <<======== CHANGE THIS fname


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
fname_2 = fname_2.replace('content3','content')

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



#  extract the subject headings for lowercase files. 
# This is simpler with the text in a single line (as compared to the
#uppercase files which had report numbers in brackets)






# now extract the report numbers:

#workaround to get the right name
fname_1 = fname.replace('repNoLines','paragraphs')              
fname_2 = fname.replace('repNoLines3.txt','repNos.txt')
fname_3 = fname.replace('repNoLines3.txt','repNos_TBD.txt')

#regexp = re.compile(r"^([^()]|\([^()]+\))+$")
#print(fname_2)
# init and triggers
allsections = [];
allSec2 = { 'sec': [], 'line': []}
#thissection = []
buffer = []
newSecTrigger = False
subjLineTrigger = False
subjLineTrigger = False 
filtlen = 2

# do the lower case files
if (fname.find('_lc_') != -1):
    with open(fname_1) as fr:
        with open(fname_2, 'w') as f2:
            with open(fname_3, 'w') as f3:
                lines = fr.readlines()
                for i, line in enumerate(lines[:-1]):
            
                    # extract the subject heading numbers 
    
                    if (line.find("----------") != -1):
                        subjBool=True
                        firstFind=True
                        f2.write(line+'\n')
                        f3.write(line+'\n')
                    elif (len(line)<filtlen) and (line != '\n'):
                        print('remove ' + line)
    #                elif not firstFind:
    #                    print('remove ' + line)                
    #                elif (len(line) > 10):
    #                    templine=line.rstrip('\n')
    ##                    f3.write('"'+subjNum+'","'+templine+'"\n')
    #                    f2.write('line')
                        
           
                    elif (line.find("Rept.") != -1) or (line.find("TN ") != -1)\
                    or (line.find("TM ") != -1) or (line.find("Rept ") != -1)\
                    or (line.find("WR ") != -1) or (line.find(" AC ") != -1)\
                    or (line.find(" RM ") != -1) or (line.find("ACR") != -1)\
                    or (line.find("NACARM ") != -1)\
                    or (line.find(" ARR ") != -1) or (line.find("CB ") != -1)\
                    or (line.find("RB ") != -1) or (line.find("MR ") != -1):
                        templine = line.replace('Rept. ','NACA-TR-')
                        templine=templine.replace('TN ','NACA-TN-')
                        templine=templine.replace('TM ','NACA-TM-')
                        templine=templine.replace('AC ','NACA-AC-')
                        templine=templine.replace('RM ','NACA-RM-')
                        
                        templine=templine.replace('ACR (','(')
                        templine=templine.replace('ACR ','NACA-ACR-')
                        templine=templine.replace('ARR (','(')
                        templine=templine.replace('ARR ','NACA-ARR-')
                        templine=templine.replace('CB (','(')
                        templine=templine.replace('CB ','NACA-CB-')
                        templine=templine.replace('RB ','NACA-RB-')
                        
                        templine=templine.replace('MR (','(')
                        templine=templine.replace('MR ','NACA-MR-')
                        templine=templine.replace('SR ','NACA-SR-')
                        templine=templine.replace('WRL','WR L')
                        templine=templine.replace('WRW','WR W')
                        templine=templine.replace('(WRE','(WR E')
                        templine=templine.replace('WR ','NACA-WR-') #this must be last
                        
                        templine=templine.replace('NACA-Langley','NACA Langley') #this must be last
    #
                        repnoStart=templine.find('NACA-')
                        if (repnoStart != -1):
    #                        print('Rep no. ',type(len(templine)))
                            repnoEnd = templine.find(',',repnoStart)
                            templine = templine[repnoStart:len(templine)]
                            templine=templine[:templine.rfind(',')]
                            
    #                    templine = templine.replace('(','\n\n')
    #                    templine = templine.replace(')','')
    #                    templine=templine[templine.find("(")+1:templine.find(")")]
                        print(templine)
                        if (templine.find("Cont.") != -1)\
                        or (templine.find("Declassified") !=-1)\
                        or (templine.find("ii") !=-1)\
                        or (templine.find("inpocket") !=-1)\
                        or (templine.find("M=1.53") !=-1)\
                        or (templine.find("Revised") !=-1):
                            print('line removed:'+templine)
                        elif (templine.find('ACR,') != -1):
                            f3.write(templine+'\n')
                        else:
                            templine=templine.replace('(','\n\n')
                            templine=templine.replace(')','')
                            templine=templine.replace(' ','')
                            templine=templine.replace(',','')
                            f2.write(templine+'\n\n')
                            iii=iii+1;





fr.close()
f2.close()


























# also extract the subject headings. This is only done for uppercase files              
fname_read = fname.replace('repNoLines','repNos')
fname_read = fname_read.replace('repNos3','repNos')
fname_write = fname_read.replace('repNos','subjRepNos')

#regexp = re.compile(r"^([^()]|\([^()]+\))+$")


if fname.find('_toc_lc') != -1:
    filtlen = 2
#    print('still nee/d to do subjRepNos')
    
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






















print(fname_1)
print(iii)

  
