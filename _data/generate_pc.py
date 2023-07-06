

lines = open("ReviewerInvites.txt").readlines()
# print(pcs)

names = []
for line in lines[1:]:
    name = " ".join(line.split("\t")[:2])
    names.append(name)

names = sorted(names, key=lambda name : name.split()[1], reverse=False)

for name in names:
    print(f'"{name}",')

