import response
import requests
import csv
import pandas as pd

readC = pd.read_csv("UKPD.csv")
def maps():
    url = "https://geocode.search.hereapi.com/v1/geocode?q=5+Rue+Daunou%2C+75000+Paris%2C+France"
    # apiKey from scalefusion
    apiKey = "K8YcUVejo63NsYB3-Xg2cwR_SE71Hp32jQOodJiDBZw"
    header = {'Authorization': 'Bearer ' + apiKey}

    result = requests.get(url, headers=header)
    print(result.json())

def dataPd():
    for email , House_No,Area ,City	,State, Pincode in zip(readC['Email'],readC['House No'],readC['Area'],readC['City'],readC['State'],readC['Pincode']):
        address = ''
        address = f'{House_No} {Area} {City} {State} {int(Pincode)}'
        print(f'{email} || {address}' )



def dataFromCsv():
    file =  open("UKPD.csv","r")
    csvReader = csv.reader(file)
    for row in csvReader:
        for column in row :
            print(column)



if __name__ == '__main__':
    dataPd()