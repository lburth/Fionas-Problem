from collections import defaultdict
import numpy as np

def get_summands(summ):
    summands = np.zeros((1,2))
    for n in range(2,summ):
        for p in range(n,summ):
            if n + p == summ:
                summands = np.append(summands,np.array([[n,p]]),axis=0)
    return summands[1:,:]

def check_unique(product):
    counter = 2
    for a in range(2,100):
        for b in range(a,100):
            if a*b==product:
                counter = counter -1
    if counter>0:
        return True
    else:
        return False

def elverlist():
    elverliste=[]
    dubioses_dict = defaultdict(list)
    for summ in range(4,199):
        summands = get_summands(summ)
        jonas_list = []
        for i in range(np.shape(summands)[0]):
            jonas_list.append(check_unique(summands[i,0]*summands[i,1]))
        if not(any(jonas_list)):
           dubioses_dict[summ] = [int(summands[j,0]*summands[j,1]) for j in range(np.shape(summands)[0])]
           elverliste.append(summ)
    return elverliste, dubioses_dict

elverliste, dubioses_dict = elverlist()

# print(elverliste)

# for key, val in dubioses_dict.items():
#     print(f"{key} & {[v for v in val]} \\\\ \midrule")

counter = {i: 0 for i in range(4, 1000000)}
for key, val in dubioses_dict.items():
    for v in val:

        counter[v] += 1

# for key, val in dubioses_dict.items():
#     for v in val:
#         if counter[v] > 1:
#             val.remove(v)


for key, val in dubioses_dict.items():
    dubioses_dict[key] = [v for v in val if counter[v] == 1]

# print(list(counter.keys())[0:27])
# print(list(counter.values())[0:27])

# print(dubioses_dict)

# for key, val in dubioses_dict.items():
#     print(f"{key} & {[v for v in val]} \\\\ \midrule")

copy_dict = dubioses_dict.copy()
for key, val in dubioses_dict.items():
    # print(key)
    # print(val)
    # print()
    if len(val) > 1:
        copy_dict.pop(key)

sum = list(copy_dict.keys())[0]
product = list(copy_dict.values())[0][0]

print(f"The sum is {sum} and the product is {product}")
print("Therefore, the unique solution is:")
print(f"a = {int((sum + np.sqrt(sum**2 - 4*product))/2)}")
print(f"b = {int((sum - np.sqrt(sum**2 - 4*product))/2)}")