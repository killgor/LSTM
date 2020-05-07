from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

import time
from datetime import date
from dateutil.relativedelta import relativedelta

#TO-DO chage to start date to get sorted data
end_time= date(2018,12,31)
#url sin fecha end_time
url = "http://www.ioc-sealevelmonitoring.org/bgraph.php?code=valp2&output=tab&period=1&endtime="

#Manejo de URLs para la iteración de periodos.
periodo=range(1) #días a tomar
output_rows = []
for x in periodo:    
    #concatenación de end time
    html = urlopen(url+end_time.strftime("%Y-%m-%d"))
    soup = BeautifulSoup(html.read(),"html5lib")    
    new_table = soup.find("tbody")
    
    #Se detectan los datos a ser agregados a la lista
    table = new_table.findAll('tr')
    #Se eliminan las dos primeras filas con datos duplicados 
    table.pop(0)
    table.pop(0)
    
    for table_row in table:
        columns = table_row.findAll('td')
        row = []
        for column in columns:
            row.append(column.text)
        output_rows.append(row)

    #TO-DO +1 from the past to get sorted data
    # retrocediendo en el tiempo día por día
    end_time += relativedelta(days=-1)
    print("Día Obtenido: "+str(x+1))
    time.sleep(1)#delay

#se crea el dataframe con los datos y se escriben en archivo
df= pd.DataFrame(output_rows, columns=["Time(UTC)", "prs(m)","rad(m)"])
#actualmente los datos se almacenan de manera desordenada
#revisar sorter.py para dejarlos ordenados

#se guarda el dataframe en un csv de manera desordenada
df.to_csv('data1d.csv', index=False)

print(df.head)