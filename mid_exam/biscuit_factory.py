biscuits_per_worker = int(input())
number_of_workers = int(input())
competing_factory = int(input())
biscuits_produced = 10*int(biscuits_per_worker*number_of_workers*0.75) + 20*(biscuits_per_worker*number_of_workers)  # bizkviti za 30 dena
print(f'You have produced {biscuits_produced} biscuits for the past month.')
if biscuits_produced > competing_factory:
    print(f'You produce {(biscuits_produced-competing_factory)/competing_factory*100:.2f} percent more biscuits.')
else:
    print(f'You produce {(competing_factory-biscuits_produced)/competing_factory*100:.2f} percent less biscuits.')