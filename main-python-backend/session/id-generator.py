#%%
import secrets
import string
import json

def get_random_string(length):
    result_str = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(length))
    return result_str

input("\n\n WARNING: This will erase the existing session keys dictionary file. Do you want to continue?...")

conditions = ['control-1', 'control-2', 'control-3', 'control-4', 'vr-1', 'vr-2', 'vr-3', 'vr-4',
            'robot-1', 'robot-2', 'robot-3', 'robot-4', 'both-1', 'both-2', 'both-3', 'both-4']

ids_in_order = []
for i in range(0,16):
    sesh_id = get_random_string(10)
    ids_in_order.append(sesh_id)

#%%
session_key = dict(zip(conditions, ids_in_order))

# %%
with open('ids.json','w') as fp:
    json.dump(session_key, fp)

print("\n\n New session IDs generated!")
# %%
