import pandas as pd
from datetime import date


class Init_df:


    def __init__(self):
        self.df = pd.DataFrame(pd.read_csv('Birthdays_Database1.csv'))

    def Birthday_Today(self):
        today = date.today().strftime("%d/%m")
        self.df_today = self.df[self.df.Birthdate == today]
        self.names = list(self.df_today.Name.values)
        self.nicknames = list(self.df_today.NickName.values)
        self.messages = list(self.df_today.Message.values)
        return self.names, self.nicknames, self.messages
