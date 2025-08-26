#!/usr/bin/env python3

# import parts 

import psutil
import plotille as plt
import re
from string import digits

# make the list

cpu_usage_list = []	
n = []	
cpu_percent_usage = []

# this is the loop for make the list 

for i in range (6):
	cpu_usage_var = psutil.cpu_percent(0.14)
	cpu_usage_var = int(cpu_usage_var)
	cpu_usage_list.append(cpu_usage_var)

	cpu_percent_usage.append(cpu_usage_var) 
	#print(cpu_usage_list)	
		
	n.append(i)
	#print(n)

#print(f"\r the list is complete {cpu_usage_list}")
#make the "moyenne" for print next to the graph
cpu_percent_usage = round(sum(cpu_percent_usage)/len(cpu_percent_usage))

result = plt.plot(n, cpu_usage_list, width=15, height=1, interp="linear", lc="red")

# make the list for remove the non used part s of the graph
# ( sorry if this code is dirty this is the first i publish)

replacement = str.maketrans({"-": None, "(": "", "|": "", ")": "", "^": "", "Y": "", "X": "", ">": "", ".": ""})
rmv_number = str.maketrans("", "", digits)

# remove the number and the non used parts

result = result.translate(replacement)
result = result.translate(rmv_number)

# convert into a list to remove non used space
result = list(result)

#del result[0:13] 
#del result [18:37]

if cpu_percent_usage > 99:
	del result[0:13]
	del result [22:37]
else:
	del result[0:13]
	del result[18:37]

# reconvert into str var and print it
final_graph = ''.join(map(str, result))


print(cpu_percent_usage, final_graph)
