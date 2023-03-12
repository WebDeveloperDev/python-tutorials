import json

data='{"var1":3,"var2":"dev"}'
print(data)

parsed=json.loads(data)
# parsed2=json.load() #it is used to read the json document from file
print(parsed["var1"])
data2={
    "name":"Dev",
    "class":12,
    "isbad":False
}
print(data2)
# jscomp=json.dumps(data2)# dumps edits the data for javascript
jscomp=json.dumps(data2,sort_keys=True)# dumps edits the data for javascript
print(jscomp)
