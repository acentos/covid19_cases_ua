import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
"Июль", "Август", "Сентябрь","Октябрь", "Ноябрь", "Декабрь"]
PTITLE = {"ciu": "COVID19 в Украине\n", "cy": "2021"}
PLEGEND = {"nc": "Новых случаев", "gc": "Госпитализировано", "vc": "Выздоровели", "dc": "Умерло"}

matplotlib.use( 'tkagg')

if sys.argv[1:]:
    stat_file = sys.argv[1]
else:
    sys.exit("[-] Syntax\n\t$python covid19_stat.py files/Dec2020.csv")

stat_lines = []

with open(stat_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    stat_lines = [cr for cr in csv_reader]

labels = stat_lines[0]
del stat_lines[0]

if len(stat_lines) == 0:
    sys.exit("[-] No data.")

for i, v in enumerate(stat_lines):
    if len(v) == 0:
        del stat_lines[i]

month = MONTHS[int(stat_lines[0][0].split('.')[1]) - 1]

try:
	days = [sl[0].split('.')[0] for sl in stat_lines]
	new_cases = [int(sl[1]) for sl in stat_lines]
	recovered =  [int(sl[2]) for sl in stat_lines]
	hospitalized = [int(sl[3]) for sl in stat_lines]
	deaths = [int(sl[4]) for sl in stat_lines]
except IndexError as index_err:
	print(f"[!!] {index_err}")
except Exception as error:
    print(f"[!!] exception: {error}")

plt.plot(days, new_cases, marker='o', color='red')
plt.plot(days, hospitalized, marker='o', color='yellow')
plt.plot(days, recovered, marker='o', color='green')
plt.plot(days, deaths, marker='o', color='grey')

plt.suptitle(PTITLE["ciu"], fontsize=14, fontweight='bold')
plt.title(f"За {month} {PTITLE['cy']}.",fontsize=10) 
plt.legend(
	[
	    f"{PLEGEND['nc']} ({sum(new_cases)} за мес.)",
	    f"{PLEGEND['gc']} ({sum(hospitalized)} за мес.)",
	    f"{PLEGEND['vc']} ({sum(recovered)} за мес.)",
	    f"{PLEGEND['dc']} ({sum(deaths)} за мес.)"
	], loc=0)

plt.show()
