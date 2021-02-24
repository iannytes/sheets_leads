""" This helps if gspread won't initialize when switching between python versions.
import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])
"""
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1QamvRozhyz7PkUhVLgARZUW-vn1QPIlHtphhzaI0rVU')
#Test of Changes
# define sheets as leads, meets, and callbacks.
leads = sh.sheet1
meets = sh.get_worksheet(1)
callbacks = sh.get_worksheet(2)

        #function to take col to be checked and sheet to wrtie results to.
def col_check(col, pull_sheet, write_sheet):
                #creates value table for true/false in col to be checked
                check_values_list = pull_sheet.col_values(col)
                loop = 0
                #loops through for total number of rows in leads sheet
                for rows in check_values_list:
                        loop = loop + 1
                #establishes variable of the col result As true or false.
                        val = pull_sheet.cell(loop, col).value
                #checks if col cell contains "TRUE", if it does; adds row to sheet to be written on.
                        if val.upper() == ("TRUE"):
                #deletes any row that might have been left over from previous runs of the program.
                                write_sheet.delete_rows(loop)
                #writes row to passed in worksheet with info on cols that return TRUE
                                values_list = pull_sheet.row_values(loop)
                                write_sheet.insert_row(values_list, loop)
                                print (values_list)
                        else:
                                print("no")


col_check(5, leads, meets)
col_check(7, leads, callbacks)

