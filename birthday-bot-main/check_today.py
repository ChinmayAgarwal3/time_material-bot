import pandas as pd
from datetime import date
from csv import writer

class Check:

    def __init__(self):
        self.df = pd.DataFrame(pd.read_csv('check_today.csv'))

    def Check_Today(self):
        today = date.today().strftime("%d/%m")
        self.df_today = self.df[self.df.Date == today]
        
        # check if dataframe empty, if empty then store date and count as 1, else 
        # check for count in the dataframe.list and if it says one then send false, else true
        if self.df_today.empty:
            update=[today,1]
            with open('check_today.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(update)
                f_object.close()
            return True
        else:
            if 1 in self.df_today.values:
                return False
            else:
                update = [today, 1]
                with open('check_today.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(update)
                    f_object.close()
                return True

        # self.names = list(self.df_today.Name.values)
        # self.nicknames = list(self.df_today.NickName.values)
        # return self.names, self.nicknames


