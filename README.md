# dashboard_to_tasks_project #

This Python project is designed to automate part of the process of producing
LA task spreadsheets. The structure is designed so that it should work with
small changes in the dashboard, however if there are large changes, to column
structure it may need updating.

__It is not a substitute for looking through the Dashboard as critical
information will likely be missed if this is done.__

The project uses the dashboard to produce spreadsheets, with each spreadsheet
corresponding to a different task. Every spreadsheet relevant info from the
dashboard and two additional columns LA_action a column with dropdown options
and a free text column LA_comment.

To run simply change the dashboard_file_path in the script main.py
to the file path of the relevant dashboard and run main.py. There is also the
option to return geometry data using a json extract file and an option to
add the LA name. Simply follow the comment instructions in the main.py script.
