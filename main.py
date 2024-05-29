import re
import csv

patetern = r"(\+7|8)\s*\(*(\d{3})\)*\-*\s*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(*(\доб\.)\s*(\d{4})\)*)*"
patetern_new = r"+7(\2)\3-\4-\5 \7\8"
untreated = []

with open("phonebook_raw.csv", encoding="utf-8") as f:
    data = csv.reader(f, delimiter=",")
    contacts_list = list(data)

for data_list in contacts_list[1:]:
    fio = " ".join(data_list[:3])
    person_data = fio.split()
    while len(person_data) != 3:
        person_data.append("")
    for row in data_list[3:]:
        word = re.sub(patetern, patetern_new, row)
        person_data += [word]
    untreated.append(person_data)

final_list = []
final_list.append(contacts_list[0])

for i in untreated:
    for j in untreated:
        if i[0] == j[0] and i[1] == j[1] and i is not j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

for data in untreated:
    if data not in final_list:
        final_list.append(data)

with open("new_phone.csv", "w", encoding="utf-8", newline="") as f:
    write = csv.writer(f, delimiter=",")
    write.writerows(final_list)