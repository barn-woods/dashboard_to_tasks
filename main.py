from Produce_indiv_excel_files import produce_files

dashboard_file_path = r'C:\Users\LRT0373\OneDrive - HM Land Registry\Stroud_LLC_EX2_v2 Dashboard Spatial.xlsx'
json_file_path = r'C:\Gitprojects\LLC\common-dev-env\apps\data-migration\Other\EX2_Stroud_dashboard_LLC' \
                 r'\int_150223_105936_LA_9591.json'
la_name = 'Stroud_District_Council'

produce_files(input_file=dashboard_file_path, json_file=json_file_path, la_name=la_name)
