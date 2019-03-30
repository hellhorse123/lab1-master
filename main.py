import json

data = {
 "firstName": "Petr",
 "lastName": "Ivskii",
 "address":
     {
 "streetAddress": "Moskow st., 12, f. 5",
 "city": "St.Petersburg",
 "postalCode": 342009
 },
 "phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
 ]
}
with open('result.json','w') as outfile:
    json.dump(data,outfile)