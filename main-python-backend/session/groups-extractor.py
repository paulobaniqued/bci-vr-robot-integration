# %%
import json
import random

with open('ids.json','r') as fp:
    key = json.load(fp)

group_a = [key.get('control-1'), key.get('control-2'), key.get('control-3'), key.get('control-4')]
group_b = [key.get('vr-1'), key.get('vr-2'), key.get('vr-3'), key.get('vr-4')]
group_c = [key.get('robot-1'), key.get('robot-2'), key.get('robot-3'), key.get('robot-4')]
group_d = [key.get('both-1'), key.get('both-2'), key.get('both-3'), key.get('both-4')]

group_list = [group_a, group_b, group_c, group_d]
random.shuffle(group_list)

for i in range(0,4):
    print("\n Group: ", group_list[i])

# %%
