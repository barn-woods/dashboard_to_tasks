from Produce_indiv_excel_files import produce_files

# enter file path of the dashboard in the parenthesis
dashboard_file_path = r''
# optional uncomment line 6 if desire spatial info and enter the file path the relevant extract file in parentheses'
# json_file_path = r''
# optional uncomment line 8 if adding an LA name to each file is desired then add the name in the parentheses'
# la_name = ''

# optional uncomment line 11 if uncommented line 4
# json_geo_info(input_file = json_file_path)

# replace None with la_name if a la_name was used in line 8
produce_files(input_file=dashboard_file_path, la_name=None)
