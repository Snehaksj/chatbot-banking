import pandas as pd
import os
def DataStore(name,mobile_number,feedback):
    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        df.append([[name,mobile_number,feedback]])
        df.to_excel("user_data.xlsx",index=False)
    else:
        df=pd.DataFrame([[name,mobile_number,feedback]],
                        columns=["name","mobile_number","feedback"])
        df.to_excel("user_data.xlsx",index=False)