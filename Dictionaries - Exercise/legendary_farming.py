materials = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    line = input().split(' ')
    for i in range(0, len(line), 2):
        material = line[i+1].lower()
        quantity = int(line[i])
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity
        if materials["shards"] >= 250:
            print('Shadowmourne obtained!')
            obtained = True
            materials["shards"] -= 250
            break
        elif materials["fragments"] >= 250:
            print('Valanyr obtained!')
            obtained = True
            materials["fragments"] -= 250
            break
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            obtained = True
            materials["motes"] -= 250
            break
for k, v in materials.items():
    print(f"{k}: {v}")
