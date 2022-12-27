sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keysToRemove = ["name", "salary"]

[sampleDict.pop(l) for l in keysToRemove]
""" for l in keysToRemove:
    del sampleDict[l] """

print(sampleDict)