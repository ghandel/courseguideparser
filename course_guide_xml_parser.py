#!/usr/bin/env python

""" A script to gather the 
divisions and departments of 
the UW from the UDDS page
and form a CSV flie"""

import re, sys, os.path, urllib, operator

filehandle = open('PDF_Schedule_of_Classes_1144.xml', 'r')

#file_in = open('div_dep.in', 'w')
file_out = open('uwmadison_2014_spring_courses.csv', 'w')

#udds = {}
udds = []

'''for line in filehandle:
    temp = re.split('<br>', line)
    for piece in temp:
        file_in.write('%s\n' % piece)

file_in.close()
file_in = open('div_dep.in', 'r')'''

split_str = 'Chem\s\d+|Math\s.+|Grad\ss?t?o?r?|Cons\s.*|Biochem\s.*|AAE\s.*|[FJS][ro]/?\s.*|BSE\s.*|\(|Physics\s\d.*|Open\s.*| \
Junior\s.*|College\slevel.*|Dy\sSci\s.*|An\s[^I].*|Intro\s.*|Entom\s.*|Food\sSci\s.*|Class\sCr.*|Stdt.*|Genetics\s\d.*| \
Honors\scandidacy.*|Honors\sprogram.*|Hon\sprog\s.*|Civ\sEngr.*|L\sSc\sCom\s.*|Land\sArc\s.*|At\sleast\s.*|Journ\s.*|Microbio\s.*| \
Variable\s.*|1st\s.*|None|Env\sTox\s.*|Not\sopen\s.*|Consent\s.*|Admission\s.*|Nutr\s.*|A?\s?\d\scr\s.*|Acct\s.*|Graduate\sstanding\s.*| \
PhD\scand\s.*|Sophomore/?\ssta.*|Prerequisite\s.*|Stat\s.*|Comp\sSci/?\s?.*|Info\sSys\s.*|Spanish\s\d.*|Econ\s.*|Gen\sBus\s.*| \
Admitted\s.*|Finance\s\d.*|O[TI]M\s.*|One\ssemester\s.*|RMI\s.*|Art\s\d.*|Art\sEd/\sCurric\s.*|Couns?\sPsy\s.*| \
Successful\s.*|Adv\sreg\s.*|Curric\s\d.*|Tchg\s.*|Com\sDis\s.*|Dance\s\d.*|Intermediate/Advanced.*| \
Previous\s.*|Audition\s.*|Dance\smajor.*|ELPA\s.*|Coun\sPsy.*|Ed\sPsych\s\d.*|El\sEd\s.*|Post-master\s.*|Psych\s.*|Kines\s.*| \
RPSE\s.*|EMA\s.*|BME\s.*|Biocore\s.*|Senior\sor\s.*|Advanced\smath.*|ECE\s.*|EPD/?E?\s.*|Crse\s.*|Geoscience\s\d.*| \
Ind\sEngr\s.*|Pre-admission\s.*|NEEP.*|Approval\s.*|Astron\s.*|Prior\s.*|Geog\s.*|Suitable\s.*|Must\s.*|Completion\s.*| \
Graded\son\s.*|Undergrad\scom\s.*|Varies\s.*|Communication\sArts\s250\sand.*|Com\sArts\s.*|Au\.D\..*|Any\s.*| \
Students\sma?u?y?s?\s?.*|Honors\scand.*|BMI\s.*|E\sAsian\s.*|E\sA\sStds.*|Declared\s.*|Limited\s.*|A\slower\s.*| \
Vet\sMed\s.*|Good\sacademic\s.*|DPH-2\s.*|PH-3\s.*|Phm\sSci\s.*|NUR\s.*|Nursing\smajor\s.*|Nurs\s\d.*|Nursing\s\d.*| \
DPM-1\s.*|4?t?h?3?r?d?\syr\s.*|Pop\sHlth\s.*|MPH\sst\s.*|prof\sst\s.*|PA\scla.*|DPT\sst.*|Physiol\s\d.*|Neurosci\s\d.*| \
Health\sprofessional\s.*|Med\sMicro\s.*|\d\ssem\s.*|Enrollment\sin\s.*|Statistics\s\d.*|Zool\s\d.*|Theatre\s\d.*| \
Stats/.*|Math/.*|Span\s\d.*|Spanish\slang.*|Soc\swork.*|Scand\sSt\s\d.*|Portuguese\s\d.*|ILS\s\d.*|One\scrse\s.*| \
Enroll\sin\s.*|Philos\s\d.*|Physcis\s\d.*|Am\sLit\s.*|Submission\s.*|ESL\sAss.*|Prerequisites\s.*|Grade\sof\s.*| \
Com\sA\..*|Adv\s.*'

for line in filehandle:
    #temp = re.search(r'<[HPT6]{1,2}>\s?(\d\d\d\s[a-zA-Z.,\- ]+)[a-zA-Z0-9. ]+</[HPT6]{1,2}>', line)
    temp = re.search(r'<H4\sid\=\"LinkTarget_\d{4}">\s?([a-zA-Z()&; ]+)\s?</H4>', line)
    if temp is not None:
        department = temp.group(1).replace('&amp;', 'AND').replace(',', '/')
    else:
        temp = re.search(r'<[DHPT6]{1,2}>\s?(\d{3})\s([a-zA-Z0-9\.&;:,\-()/ ]+)</[DHPT6]{1,2}>', line)
        if temp is not None:
            class_number = temp.group(1)
            class_title = re.split(split_str, temp.group(2).replace('&amp;', 'AND').replace(',', '/'))[0]
            if re.search(r'\d\d\d', class_title) is None:
                udds.append('%s,%s,%s' % (department, class_number, class_title))
    '''else:
        temp = re.search(r'A\d{2}\s+\d{2}\s+([a-zA-Z ]+)\s+', line)
        if temp is not None:
            dept = temp.group(1).replace('&amp;', 'AND').replace(',', '/').strip()
            if dept not in udds[div]:
                udds[div][dept] = []
        else: 
            temp = re.search(r'A\d{2}\s+\d{4}\s+([a-zA-Z ]+)\s+', line)
            if temp is not None:
                unit = temp.group(1).replace('&amp;', 'AND').replace(',', '/').strip()
                if unit not in udds[div][dept]:
                    udds[div][dept].append(unit)'''

file_out.write('Division, Departent, Unit\n')

"""for division in udds:
    for department in udds[division]:
        for i in xrange(len(department) - 1):
            file_out.write('%s, %s, %s\n' % \
            (division, department, udds[division][department][i]))"""

for divi in udds:
    file_out.write('%s\n' % divi)
    '''for dep in udds[divi]:
        for i in xrange(len(udds[divi][dep])):
            file_out.write('%s, %s, %s\n' % \
            (divi, dep, udds[divi][dep][i]))'''

filehandle.close()
#file_in.close()
file_out.close()
#os.remove('div_dep.in')
sys.exit(0)
