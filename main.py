from produce_indiv_excel_files import produce_files
from geo_info_from_json import json_geo_info

# enter file path of the dashboard in the parenthesis
dashboard_file_path = r''

"""
Optional uncomment line 16 and 17 if extract_with_modified_columns.csv doesn't already exist and desire spatial
analysis fields and enter the file path of the relevant extract file in the speach marks on line 16. Once the
json_geo_info command runs a file called extract_with_modified_columns.csv will be produced this file should
contain all the spatial analysis for the given extract. If this file exists it will be used for spatial analysis
so if the file already exists line 16 and 17 can be commented. If tasks are required for both spatial and textual
it is advisable to first run main.py with lines 16 and 17 uncommented and then uncomment the lines to run the spatial.
"""

# json_file_path = r''
# json_geo_info(input_file=json_file_path)

"""
Optional uncomment line 22 if adding an LA name to each file is desired, add the name in the speach marks and replace
None with the name on line.
"""

# la_name = ''

produce_files(input_file=dashboard_file_path, la_name=None)
