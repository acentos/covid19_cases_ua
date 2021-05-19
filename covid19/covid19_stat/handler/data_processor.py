import os
import csv
import matplotlib.pyplot as plt
from covid19_stat import app


MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
"Июль", "Август", "Сентябрь","Октябрь", "Ноябрь", "Декабрь"]

def read_csv_data(stat_file_csv):
    
    if stat_file_csv:
        stat_lines = []

        with open(stat_file_csv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            stat_lines = [cr for cr in csv_reader]
    else:
        stat_file_csv = None
    
    return stat_lines

def data_generator(stat_lines, result_png_file):

    generate_info = {}
        
    labels = stat_lines[0]
    del stat_lines[0]

    if len(stat_lines) == 0:
        print("empty")

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

    generate_info = {
        "title": "COVID19 в Украине",
        "subtitle": f"{month} 2021.",
        "total_new_cases": sum(new_cases),
        "total_hospitalized": sum(hospitalized),
        "total_recovered": sum(recovered),
        "total_deaths": sum(deaths)
        }

    plt.savefig(f"{result_png_file}")
    plt.cla()
    
    return generate_info

def data_processor(stat_file):
    stat_file_csv = os.path.join(app.config['UPLOAD_FOLDER'], stat_file)
    result_png_file = os.path.join(
        app.config['DOWNLOAD_FOLDER'],
        os.path.splitext(os.path.basename(stat_file_csv))[0] + ".png")
    stat_lines = read_csv_data(stat_file_csv)
    return stat_lines, data_generator(stat_lines, result_png_file), result_png_file
