# Import packages
import pandas as pd
from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')
from pyadomd import Pyadomd
from datetime import datetime as dt

# Build connection string 
##Catalog is the database
conn_str = 'Provider=PRODIVERINFO; Data Source=YourDatabaseURL;Catalog=OPTIONAL_DATABASENAME;'

# Enter DAX or MDX query
dax_query = """SELECT
 Field1*{Field2.&Value1,Field2.&Value2}*{Field3.&Value1,Field3.&Value2
	 } ON 0,
  
  {Field4} ON 1
 
FROM
   Database_cube
WHERE ({Field4.&Value1,Field4.&Value2},Field5.&Value1,Field6.&Value1)"""

# Output results as pandas dataframe
with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(dax_query) as cur:
        df = pd.DataFrame(cur.fetchone(),
        columns=[i.name for i in cur.description])

# Rename Columns
#df.rename(columns={'OriginalColumnName1':'NewColumnName1',
#                   'OriginalColumnName2':'NewColumnName2',
#                   'OriginalColumnName3':'NewColumnName3'},
#          inplace = True)
df['date_column']=pd.to_datetime(df['date_column'])
#print(df.dtypes)

df['year']=df['date_column'].dt.year
df['quarter']=df['date_column'].dt.quarter
df['month']=df['date_column'].dt.month
df['index']=df.index
df.to_csv('file_name.csv')
