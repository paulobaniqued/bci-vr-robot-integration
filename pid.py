""" Participant ID Generator """

import json
p_list = json.load(open('participant_id.json'))

print("Participant ID Generator")

f_name = input("Please input your first name: ")
s_name = input("Please input your surname: ")
full_name = f_name + " " + s_name

initials = str(f_name[0]) + str(s_name[0])

sid = input("Please input your student ID: ")
sid = sid[6:]

address = input("Please input the first word in your home address: ")
address = address[:2]

pid = str(initials) + str(sid) + str(address)

p_list[f"{full_name}"] = pid

with open('participant_id.json', 'w') as json_file:
    json.dump(p_list, json_file)


print("Your Participant ID is: ", pid)
