


# This script reads in OCR text data subject headings in the uppercase format
# and splits it into meaningful files. 1949-1958 and beyond
# the first part cleans up the data by removing linebreaks over the report
# number lines, in order to identify and extract report numbers. 
# It is probably easier to extract report numbers while not all line breaks
# have been removed, but just the line-breaks that break a report number into 
# two lines.
# Then the report numbers and headings are extracted, categorizing all report
# numbers (or at least those that are OCR recognizable) into the subject heading
# file _repNos.txt
#
# More scripts need to be run on the output files to convert them into usable variables

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
#toc_49 = "./indexes/1915-1949_toc_lc.txt"
#toc_51 = "./indexes/1949-1951_toc_lc.txt"
toc_53 = "./indexes/1949-1953_toc_uc.txt"
toc_54 = "./indexes/1953-1954_toc_uc.txt"
toc_55 = "./indexes/1954-1955_toc_uc.txt"
toc_56 = "./indexes/1955-1956_toc_uc.txt"
toc_57 = "./indexes/1956-1957_toc_uc.txt"
toc_58 = "./indexes/1957-1958_toc_uc.txt"
#toc1=toc_49
#toc2=toc_51
toc3=toc_53
toc4=toc_54
toc5=toc_55
toc6=toc_56
toc7=toc_57
toc8=toc_58

# the file being handled; change from toc1-toc8 manually 
# (yea I know; cumbersome) such is data cleaning

# this script does only the uppercase files toc3-8
fname = toc8

iii=0;

# strip linebreaks from file where it spans across report numbers so that
# report numbers can be identified.
# filename
fname_1 = fname.rstrip('.txt')+'_repNoLines.txt'
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
            or (line.find('MR\n') != -1) or (line.find('MR \n') != -1):
                templine = line.strip('\n')
                print('linebreak removed at'+templine)
                f1.write(templine)
            else:
                f1.write(line)
                
# close the files; will be needed            
fr.close()
f1.close()       
    
# extract brackets only
fname_2 = fname.rstrip('.txt')+'_repNos.txt'
#regexp = re.compile(r"^([^()]|\([^()]+\))+$")



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




# init and triggers
allsections = [];
allSec2 = { 'sec': [], 'line': []}
#thissection = []
buffer = []
newSecTrigger = False
subjLineTrigger = False





# do the uppercase files
if fname[-6:-4] =='uc':
    with open(fname_1) as fr:
        with open(fname_2, 'w') as f2:
            lines = fr.readlines()
            for i, line in enumerate(lines[:-1]):
        
                subjLineTrigger = False 
#                exctract relevant lines that also contain report numbers
#                clean up report numbers. They are in parentheses
    #            line.replace('ARR','-ARR-')
                # extract the subject heading numbers 
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
                            f2.write('\n')
                            f2.write('\n')
                            f2.write('----------'+templine+'\n\n')
                            
                elif ((line.find("(") != -1) and (line.find(")") != -1))\
                or (line.find("Rept.") != -1) or (line.find("TN ") != -1)\
                or (line.find("TM ") != -1) or (line.find("TM ") != -1)\
                or (line.find("WR ") != -1) or (line.find(" AC ") != -1)\
                or (line.find(" RM ") != -1) or (line.find("ACR") != -1)\
                or (line.find("NACARM ") != -1)\
                or (line.find(" ARR ") != -1) or (line.find("CB") != -1)\
                or (line.find("RB ") != -1) or (line.find("MR") != -1):
                    templine = line.replace('Rept.','-TR-')
                    templine=templine.replace('TN','-TN-')
                    templine=templine.replace('TM','-TM-')
                    templine=templine.replace('WR','-WR-')
                    templine=templine.replace(' RM ','RM-')
                    templine=templine.replace('NACARM','NACA-RM-')
    #                templine = brackets.replace(' ','')
                    templine = templine.replace(' ','')
                    if (templine[:3]== '-TN-'): 
                        templine = 'NACA'+templine
                    if (templine[:2]== 'RM-'): 
                        templine = 'NACA-'+templine
                    templine = templine.replace('Supersedes','')
                    templine = templine.replace('Formerly','')
                    templine = templine.replace('Nowissuedas','')
                    templine = templine.replace('{','(')
                    templine = templine.replace('.RM-',' NACA-RM-')
                    templine = templine.replace(';RM-',' NACA-RM-')
                    templine = templine.replace('.-TN-',' NACA-TN-')
                    templine = templine.replace(';-TN-',' NACA-TN-')
                    templine = templine.replace(',-TR-',' NACA-TR-')
                    templine = templine.replace('--','-')
                    if (templine[:4]== '-TN-'): 
                        templine = 'NACA'+templine
                    templine=templine[templine.find("(")+1:templine.find(")")]
                    templine = templine.replace(',','.')
                    templine = templine.replace('l.','1.')
                    templine = templine.replace('.l','.1')
                    print(templine)
                    if (templine.find("Cont.") != -1)\
                    or (templine.find("Declassified") !=-1)\
                    or (templine.find("ii") !=-1)\
                    or (templine.find("inpocket") !=-1)\
                    or (templine.find("M=1.53") !=-1)\
                    or (templine.find("Revised") !=-1):
                        print('line removed:'+templine)
                    else:
                        templine = templine.replace(' NACA','\n\nNACA')
                        templine = templine.replace('.NACA','\n\nNACA')
                        templine = templine.replace('sedes','NACA')
                        templine = templine.replace('andportionsof','\n\nNACA')
                        templine = templine.replace('merly','\n\nNACA')
                        templine = templine.rstrip('.')
                        templine = templine.rstrip(';')
                        if (templine.find('.')!=-1):
                            templine = templine[:templine.find('.')]
#                        templine=templine.replace('\nRM','\nNACA-RM')
                        f2.write(templine+'\n\n')
                        iii=iii+1;
                        
#                
#            else:
#                fw.write(line)
#            fw.write(lines[i + 1])
#            fw.write(lines[i + 2])

print(fname)
print(iii)
#fadd = open(fnamew, "r")
#for x in fadd:
#  print(x)
  
