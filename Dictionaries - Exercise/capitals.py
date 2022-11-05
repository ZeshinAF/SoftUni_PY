countries = input().split(', ')
capitals = input().split(', ')
dic = dict(zip(countries, capitals))
for k, v in dic.items():
    print(f"{k} -> {v}")
