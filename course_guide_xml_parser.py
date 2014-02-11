#!/usr/bin/env python

"""
Author:         Garret Handel
Last Updated:   2014/02/10
Description:    A script to gather the 
                    courses and associated information
                    from and XML document of the course
                    list and form a CSV flie
"""

import re, sys, os, urllib, operator

# FILE HANDLING - Open XML and initialize CSV
for x in os.listdir(os.getcwd()):
    if x.endswith(".xml"):
        xml = x
if xml is None:
    print('No XML file found in current directory! Quitting.')
    sys.exit(1)
filehandle = open(xml, 'r')
file_out = open('uwmadison_2014_spring_courses.csv', 'w')

# Define search string to split off unneeded text on course title
split_str = 'Chem\s\d+|Math\s.+|Grad\ss?t?o?r?|Cons\s.*|Biochem\s.*|AAE\s.*|[FJS][ro]/?\s.*|BSE\s.*|\(|Physics\s\d.*|Open\s.*| \
Junior\s.*|College\slevel.*|Dy\sSci\s.*|An\s[^I].*|Intro\s.*|Entom\s.*|Food\sSci\s.*|Class\sCr.*|Stdt.*|Genetics\s\d.*| \
Honors\scandidacy.*|Honors\sprogram.*|Hon\sprog\s.*|Civ\sEngr.*|L\sSc\sCom\s.*|Land\sArc\s.*|At\sleast\s.*|Journ\s.*|Microbio\s.*| \
Variable\s.*|1st\s.*|None|Env\sTox\s.*|Not\sopen\s.*|Consent\s.*|Admission\s.*|Nutr\s.*|A?\s?\d\scr\s.*|Acct\s.*|(Graduate|Senior)\sstanding\s.*| \
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
Health\sprofessional\s.*|Med\sMicro\s.*|(\d|A)\ssem\s.*|Enrollment\sin\s.*|Statistics\s\d.*|Zool\s\d.*|Theatre\s\d.*| \
Stats/.*|Math/.*|Span\s\d.*|Spanish\slang.*|Soc\swork.*|Scand\sSt\s\d.*|Portuguese\s\d.*|ILS\s\d.*|One\scrse\s.*| \
Enroll\sin\s.*|Philos\s\d.*|Physcis\s\d.*|Am\sLit\s.*|Submission\s.*|ESL\sAss.*|Prerequisites\s.*|Grade\sof\s.*| \
Com\sA\..*|Adv\s.*|Quantitative\s.*'

# Define search strings for finding division, department, and course number and title
division_search = '<(TH|H4)\sid\=\"LinkTarget_\d{4}\">((College\sof|School\sof|Air,)[a-zA-Z&;, ]+)\([a-zA-Z& ]+\)\s?([A-Z&, ]+)(\(\d\d\d\s\))?'
department_search = '<(TH|H4)\sid\=\"LinkTarget_\d{4}">\s?([A-Z&;\(\) ]+)</[TH4]{2}>([a-zA-Z&;, ]+\(.*\).*)?'
course_search = '<[DHPT6]{1,2}>\s?(\d{3})\s([a-zA-Z0-9\.&;:,\-()/ ]+)</[DHPT6]{1,2}>'

# Initialize variables to avoid uninitialized variable errors
division = ''
department =''
course_title = ''
course_number = ''
courses = []

# Begin search. Read lines from input file and apply RegEx searches to find appropriate information
for line in filehandle:
    line = line.replace('&amp;', '&')
    # find the DIVISION
    division_temp = re.search(r'%s' % (division_search), line)
    if division_temp is not None:
        division = division_temp.group(2).replace(',', '/')
        # Check for DEPARTMENT included on same line as division (only a couple cases of this)
        if division_temp.group(4) is not None:
            department = division_temp.group(4).replace(',', '/')
    else:
        # find the DEPARTMENT
        department_temp = re.search(r'%s' % (department_search), line)
        if department_temp is not None:
            department = department_temp.group(2).replace(',', '/')
        else:
            # find COURSE TITLE and COURSE NUMBER
            course_temp = re.search(r'%s' % (course_search), line)
            if course_temp is not None:
                course_number = course_temp.group(1)
                course_title = re.split(split_str, course_temp.group(2).replace(',', '/'))[0]
                # Extract COURSE NUMBER and add COURSE INFO to the array
                if re.search(r'\d\d\d', course_title) is None:
                    courses.append('%s,%s,%s,%s' % (division.rstrip(), department.rstrip(), course_number, course_title))

# Initialize CSV with headers
file_out.write('Division, Department, Course Number, Course Title\n')

# Write entries from array to CSV
for course in courses:
    file_out.write('%s\n' % course)

# Close files and exit safely
filehandle.close()
file_out.close()
sys.exit(0)
