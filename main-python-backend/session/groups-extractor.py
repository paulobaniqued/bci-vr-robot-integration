# %%
import json
import random

with open('ids.json','r') as fp:
    key = json.load(fp)

group_a = [key.get('control-1'), key.get('control-2'), key.get('control-3'), key.get('control-4'), key.get('control-5'), key.get('control-6'), key.get('control-7'), key.get('control-8')]
group_b = [key.get('vr-1'), key.get('vr-2'), key.get('vr-3'), key.get('vr-4'), key.get('vr-5'), key.get('vr-6'), key.get('vr-7'), key.get('vr-8')]
group_c = [key.get('robot-1'), key.get('robot-2'), key.get('robot-3'), key.get('robot-4'), key.get('robot-5'), key.get('robot-6'), key.get('robot-7'), key.get('robot-8')]
group_d = [key.get('both-1'), key.get('both-2'), key.get('both-3'), key.get('both-4'), key.get('both-5'), key.get('both-6'), key.get('both-7'), key.get('both-8')]

group_list = [group_a, group_b, group_c, group_d]
random.shuffle(group_list)

for i in range(0,4):
    print("\n Group: ", group_list[i])

# %%
