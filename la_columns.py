import pandas as pd
import string
import pandas.io.formats.excel

"""
Add a column with dropdown options called LA_action, a free text column called LA_comments,
format the column widths to be the same as the max character sting in the column +4 unless this is greater than 35
in which case  a width of 39 characters is used, and freeze the first row.
"""


def la_columns_and_format_sheet(file_instance, file_name):
    # create empty LA_action and LA_comment columns
    file_instance['LA_action'] = None
    file_instance['LA_comment'] = None
    # get the position the columns: statutory_provision, charge_geographic_description and supplementary_information
    stat_prov = 0
    geo_desc = 0
    sup_info = 0
    if 'statutory_provision' in file_instance.columns:
        stat_prov += file_instance.columns.get_loc('statutory_provision')
    if 'charge_geographic_description' in file_instance.columns:
        geo_desc += file_instance.columns.get_loc('charge_geographic_description')
    if 'supplementary_information' in file_instance.columns:
        sup_info += file_instance.columns.get_loc('supplementary_information')
    # get the position of the last row and last column
    num_cols = len(file_instance.columns)  # numerical last column position
    num_rows = int(len(file_instance) + 1)  # numerical row position
    last_column = string.ascii_uppercase[num_cols - 1]  # letter based column last column position
    # get the position of the LA_action column
    la_act = file_instance.columns.get_loc('LA_action')
    # use xlsxwriter to make formatting changes
    writer = pd.ExcelWriter(file_name + '.xlsx', engine='xlsxwriter')
    pandas.io.formats.excel.ExcelFormatter.header_style = None  # remove xlsxwriters default formats
    file_instance.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    # add a dropdown list under LA_action
    cell_range = string.ascii_uppercase[la_act] + '2:' + string.ascii_uppercase[la_act] + str(len(file_instance) + 1)
    worksheet.data_validation(
        cell_range, {'validate': 'list', 'source': ['Corrected', 'Cancelled', 'No action required'],
                     'dropdown': True, 'error_title': 'Invalid input',
                     'error_message': 'Please select an action from the dropdown'})
    # align column text left
    worksheet.set_row(0, None, None, {'align': 'left'})
    # freeze the first row so that in remains in veiw when the user scrolls down
    worksheet.freeze_panes(1, 0)
    # get the dataset range
    string_range = f"A1:{last_column}{num_rows}"
    # apply a format to all columns to wrap text
    format_align = workbook.add_format({'text_wrap': True, 'align': 'left', 'valign': 'top'})
    worksheet.set_column(string_range, None, format_align)
    worksheet.autofilter(string_range)  # add a filter
    worksheet.autofit()  # autofit row lengths for the worksheet
    # set custom widths for statutory_provision, charge_geographic_description and supplementary_information columns
    worksheet.set_column(0, stat_prov, 20, format_align)
    worksheet.set_column(0, geo_desc, 31, format_align)
    worksheet.set_column(0, sup_info, 34, format_align)
    workbook.close()
