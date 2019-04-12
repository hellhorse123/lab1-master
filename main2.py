import json

data = {
"Grupppa":"vpi11"`
[
 {
 "FIO": "Borisenko Anna Evgenyievna",
 "address":
    {
 "Country": "Russia",
 "City": "Rostov-on-Don",
 "Street": "chelnoki"
    },
"contacs":
    {
 "VK": "vk.com/borrisca_ancka",
 "Twitter": "Не пользуется",
 "Primichanie": "Лучшая староста в мире",
    },
"phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
    ]
 },
 {
 "FIO": "Arkhipov Mikhail Aleksandrovich",
 "address":
    {
 "Country": "Russia",
 "City": "Feodosia",
 "Street": "Pervushina"
    },
"contacs":
    {
 "VK": "vk/id12121",
 "Twitter": "Нема такого",
 "Primichanie": "its me",
    },
"phoneNumbers":
    [
 "812 123-12344",
 "916 123-45674"
    ]
 }
]
}
with open('result1.json','w') as outfile:
    json.dump(data,outfile)
