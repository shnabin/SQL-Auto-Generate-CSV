import pyodbc
import pandas as pd
from datetime import datetime, timedelta
import datetime
import time
#connection to the MSSQL server
conn = pyodbc.connect( driver='{SQL Server Native Client 11.0}',server='xyz', database='RW', Trusted_Connection='yes')
cursor = conn.cursor()
path = 'G:\\dump\\'  #path in which the .csv has to be generated
sql = '''SELECT * FROM weather_data WHERE TimeCol BETWEEN ? AND ? ORDER BY LOCALCOL ASC;''' #Replace the table name & column names
while 1:
    t_date=datetime.datetime.now().date()
    today_date=pd.to_datetime(t_date)
    tm_date = today_date + timedelta(days=1)
    filename = str(t_date)+'.csv'
    df = pd.read_sql_query(sql, conn, index_col = 'Timecol', params =[today_date, tm_date])
    df1 = df.resample('15Min').mean()
    df1.index.names = ['Date Time']
    df1.to_csv(path+filename)
    time.sleep(300)
