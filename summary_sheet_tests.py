import re
import datetime

"""
If the input equals any words form the exclude_list, contains the word Council, is in the date format of double
forward slash indicating a date, is a date format, has a format of triple dot indicating a version, has the equation
format of an equals sign at the start of the string or contains the word Analysis return True else return False.
"""


def not_exclude_value(test):
    exclude_tuple = ('Version', 'Issue', 'Refreshed:', 'Total', 'Link', 'Small Area Warnings', 'Check Required',
                     'Charge Geographic Description Lengths', 'Data Set', 'Refreshed',
                     'Charge distribution by year (graph)', 'Other Warnings', 'Check Advised', 'Check Required',
                     'Value in charge-geographic-description', 'Unique Values', 'Register parts',
                     'Charge Types and Charge Categories', 'Charges registered between 2010 and Present',
                     'Charges registered between 1990 and 2009', 'Charges registered between 1970 and 1989',
                     'Charges registered between 1925 and 1969', 'Value in charge - address',
                     'originating-authority variations', 'further-information-location variations')
    if test in exclude_tuple or re.search('.*Council.*', str(test)) or re.search('.*/.*/.*', str(test)) or \
            re.search('.*\..*\..*\..*', str(test)) or re.search('^=.*', str(test)) or \
            re.search('.*Analysis.*', str(test)) or isinstance(test, datetime.date):
        return False
    else:
        return True


"""
Check if the text contains a number and the string 'm' to identify small area checks or if it contains a number and the
string 'km' to identify large area checks name everything else other_checks.
"""


def type_of_check(test):
    if re.search('.*\dm.*', test):
        return 'small_area_checks'
    if re.search('.*\dkm.*', test):
        return ['large_area_checks', 'large_area_checks_sheet']
    elif re.search('Length.*', test):
        return ['short_geo_desc_checks', 'short_geo_desc_checks_sheet']
    else:
        return ['other_checks', 'other_checks_sheet']
