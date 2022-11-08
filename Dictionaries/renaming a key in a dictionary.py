sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"

}
keysToRename = ["city"]
old_key = sampleDict["city"]
del sampleDict["city"]
sampleDict["location"]= old_key
print(sampleDict)
