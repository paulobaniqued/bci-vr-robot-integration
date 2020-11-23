# %%
import json

with open('ids.json','r') as fp:
    session_key = json.load(fp)

day = input("\n\n What session is it today? ")
session_id = session_key.get(day)
print("\n\n Session ID: ", session_id)

