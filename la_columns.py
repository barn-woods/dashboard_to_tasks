import pandas as pd
import string
"""
Add a column with dropdown options called LA_action, a free text column called LA_comments,
format the column widths to be the same as the max character sting in the column +4 unless this is greater than 35
in which case  a width of 39 characters is used, and freeze the first row.
"""


def la_columns_and_format_sheet(file_instance, file_name):
    file_instance['LA_action'] = None
    file_instance['LA_comment'] = None
    if 'statutory_provision' in file_instance.columns:
        stat_prov = file_instance.columns.get_loc('statutory_provision')
    if 'charge_geographic_description' in file_instance.columns:
        geo_desc = file_instance.columns.get_loc('charge_geographic_description')
    if 'supplementary_information' in file_instance.columns:
        sup_info = file_instance.columns.get_loc('supplementary_information')
    num_cols = len(file_instance.columns)
    num_rows = int(len(file_instance) + 1)
    last_column = string.ascii_uppercase[num_cols - 1]
    la_act = file_instance.columns.get_loc('LA_action')
    writer = pd.ExcelWriter(file_name + '.xlsx', engine='xlsxwriter')
    file_instance.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    cell_range = string.ascii_uppercase[la_act] + '2:' + string.ascii_uppercase[la_act] + str(len(file_instance) + 1)
    worksheet.data_validation(
        cell_range, {'validate': 'list', 'source': ['Corrected', 'Cancelled', 'No action required'],
                     'dropdown': True, 'error_title': 'Invalid input',
                     'error_message': 'Please select an action from the dropdown'})
    worksheet.set_row(0, None, None, {'align': 'left'})
    worksheet.freeze_panes(1, 0)
    string_range = f"A1:{last_column}{num_rows}"
    format_align = workbook.add_format({'text_wrap': True, 'align': 'left', 'valign': 'top'})

    worksheet.set_column(string_range, None, format_align)
    worksheet.autofilter(string_range)
    worksheet.autofit()
    worksheet.set_column(0, stat_prov, 20, format_align)
    worksheet.set_column(0, geo_desc, 31, format_align)
    worksheet.set_column(0, sup_info, 34, format_align)

    workbook.close()
