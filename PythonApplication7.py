# Import packages
import pandas as pd
from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')
from pyadomd import Pyadomd
from datetime import datetime as dt

# Build connection string 
##Catalog is the database
conn_str = 'Provider=MSOLAP; Data Source=asazure://aspaaseastus2.asazure.windows.net/marcaas;Catalog=Ferias;'

# Enter DAX or MDX query
dax_query = """SELECT
 [Scenarios].[Scenario].&[Total Actuals]*{[Line Of Business].[Line Of Business].&[Total Postpaid],[Line Of Business].[Line Of Business].&[AT&T Wireless Broadband]}*{[Subscription Devices].[Subscription Device].&[Mobile Wireless],[Subscription Devices].[Subscription Device].&[Voice Device],[Subscription Devices].[Subscription Device]}*{ [Measures].[Gross Adds],
       [Measures].[Net Disconnects],[Measures].[Net Adds],[Measures].[Net Invol Disc]
	 } ON 0,
  
  {[Calendar].[Date].[Date]} ON 1
 
FROM
   [Model]
WHERE ({[Calendar].[Year].&[2022],[Calendar].[Year].&[2023]},[Liability].[Liability].&[Corporate Responsibility User],[Business Units].[Business Unit].&[Small Business/Mid Market BU Group])"""

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
df['[Calendar].[Date].[Date].[MEMBER_CAPTION]']=pd.to_datetime(df['[Calendar].[Date].[Date].[MEMBER_CAPTION]'])
#print(df.dtypes)

df['year']=df['[Calendar].[Date].[Date].[MEMBER_CAPTION]'].dt.year
df['quarter']=df['[Calendar].[Date].[Date].[MEMBER_CAPTION]'].dt.quarter
df['month']=df['[Calendar].[Date].[Date].[MEMBER_CAPTION]'].dt.month
df['index']=df.index
df.to_csv('Ferias_wireless.csv')
#df_total_disco = df.groupby(['year','quarter','[Scenarios].[Scenario].&[Total Actuals].[Line Of Business].[Line Of Business].&[Total Postpaid].[Subscription Devices].[Subscription Device].&[Mobile Wireless].[Measures].[Net Disconnects]'])['index'].count()

#df_total_disco.to_csv('total_disco.csv')