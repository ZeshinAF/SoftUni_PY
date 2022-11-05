
population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())
min_index = population.index(min(population))
wage_gap = abs(population[min_index] - minimum_wealth)
while max(population) >= minimum_wealth + wage_gap:
    if min(population) >= minimum_wealth:
        break
    else:
        max_index = population.index(max(population))
        population[max_index] -= wage_gap
        population[min_index] += wage_gap
        min_index = population.index(min(population))
        wage_gap = abs(population[min_index] - minimum_wealth)
else:
    print('No equal distribution possible')
    exit()
print(population)
