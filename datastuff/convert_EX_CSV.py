import pandas as pd, os


# converting .xlsx to .csv
curr_path = os.getcwd()
data_curr_path = os.path.join(curr_path,'Data')
csv_curr_path = os.path.join(curr_path,'CSVData')

readFile = pd.read_excel(os.path.join(data_curr_path,'Book_Loans.xlsx'))

readFile.to_csv(os.path.join(csv_curr_path,'Book_Loans.csv'),index=False)



