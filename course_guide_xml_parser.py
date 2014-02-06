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

for line in filehandle:
    temp = re.search(r'<H6>(\s?\d\d\d\s[a-zA-Z. ]+)[Cons]?[Math]?[Open]?[a-zA-Z0-9. ]+</H6>', line)
    if temp is not None:
        div = temp.group(1).replace('&amp;', 'AND').replace(',', '/').strip()
        #udds[div] = {}
        udds.append(div)
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
