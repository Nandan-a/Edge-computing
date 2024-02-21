import pandas as pd
import numpy as np
student_details = (
    {
        'S.No' : ["1","2","3","4"],
        'Name' : ["Nandan","Shreyash","Ritesh","Kaka"]
    }
)
df = pd.DataFrame(student_details)
df_str = df.to_string(index=False)
print(df_str)