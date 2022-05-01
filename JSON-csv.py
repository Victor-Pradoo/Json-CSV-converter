#Aula 19
#Claudia Fiorentino TIA: 42005302
#João Victor Pimenta TIA: 42005876
#Victor Prado Chaves TIA: 32070772

#links de referência :https://docs.python.org/3/library/urllib.html
# https://developer.rhino3d.com/guides/rhinopython/python-xml-json/#:~:text=Use%20the%20import%20function%20to%20import%20the%20JSON%20module.&text=The%20JSON%20module%20is%20mainly,be%20written%20into%20a%20file.&text=While%20the%20JSON%20module%20will,write%20directly%20from%20JSON%20files.
# caso seja pra fazer com pandas : https://datatofish.com/json-string-to-csv-python/

import urllib.request
import json

FII = ["alzr", "bcri", "brcr", "cpff", "cpts", "deva", "habt", "hctr", "hsml", "irdm", "knri", "mgff", "rbff", "rbrf", "recr", "rect",
"urpr", "vghf", "vgip", "vslh", "xpci", "xplg", "xpml", "xppr"]

for i in range (0, len(FII)):
    arq = urllib.request.urlopen(https://api-simple-flask.herokuapp.com/api/FII[i], data= json) #pegando o arquivo na api e atribuindo a arq
    if arq:
        with open(arq, 'r') as a:
            datastore = json.load(a) #lendo arq

    #colocar o método que usamos no outro projeto para gravar os dados no csv

