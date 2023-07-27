import csv

input_file = input("Entrez le nom du fichier CSV : ")
input_file = input_file + '.csv'
params_input = input("Entrez les numéros des paramètres à sélectionner (séparés par des espaces).\n"    
                     "les options sont:\n"
                     "- station             : 0\n"
                     "- valid               : 1\n"
                     "- tmpf                : 2\n"
                     "- dwpf                : 3\n"
                     "- relh                : 4\n"
                     "- drct                : 5\n"
                     "- sknt                : 6\n"
                     "- p01i                : 7\n"
                     "- alti                : 8\n"
                     "- mslp                : 9\n"
                     "- vsby                : 10\n"
                     "- gust                : 11\n"
                     "- skyc1               : 12\n"
                     "- skyc2               : 13\n"
                     "- skyc3               : 14\n"
                     "- skyc4               : 15\n"
                     "- skyl1               : 16\n"
                     "- skyl2               : 17\n"
                     "- skyl3               : 18\n"
                     "- skyl4               : 19\n"
                     "- wxcodes             : 20\n"
                     "- ice_accretion_1hr   : 21\n"
                     "- ice_accretion_3hr   : 22\n"
                     "- ice_accretion_6hr   : 23\n"
                     "- peak_wind_gust      : 24\n"
                     "- peak_wind_drct      : 25\n"
                     "- peak_wind_time      : 26\n"
                     "- feel                : 27\n"
                     "- metar               : 28\n"
                     "- snowdepth           : 29\n")
selected_params = list(map(int, params_input.split()))
selected_params.sort()
output_file = "sorted-" + input_file
with open(input_file, 'r') as csv_file_in, open(output_file, 'w', newline='') as csv_file_out:
    reader = csv.reader(csv_file_in)
    writer = csv.writer(csv_file_out)
    headers = next(reader)
    selected_headers = [headers[i] for i in selected_params]
    writer.writerow(selected_headers)
    for row in reader:
        selected_row = [row[i] for i in selected_params]
        writer.writerow(selected_row)

print("Les colonnes sélectionnées ont été écrites dans le fichier", output_file)
