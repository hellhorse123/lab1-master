import json

data = {
"Grupppa":`
[
 {
 "FIO": "Myrzin A.M.",
 "address":
    {
 "Country": "Russia",
 "City": "Feodosia (Krim)",
 "Street": "chelnoki"
    },
"contacs":
    {
 "VK": "vk/id12121",
 "Twitter": "блааваб",
 "Primichanie": "норм чувак",
    },
"phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
    ]
 },
 {
 "FIO": "Jukov",
 "address":
    {
 "Country": "Russia",
 "City": "St.Petersburg",
 "Street": "Ddadad"
    },
"contacs":
    {
 "VK": "vk/id12121",
 "Twitter": "блааваб",
 "Primichanie": "алкашь",
    },
"phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
    ]
 }
]
}
with open('result1.json','w') as outfile:
    json.dump(data,outfile)