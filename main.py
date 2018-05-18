import random

ROUNDS_OF_TRAINING = 10

population = generateInitPopulation()
for i in range(0, ROUNDS_OF_TRAINING):
	for j in range(0, len(population)):
		population[j].score = play(population[j].genotype)
		population[j].survivalScore = survival(population[j].score, random.random())
	sortedPopulation = sorted(population, key=lambda x: x.survivalScore, reverse=True)
	best = sortedPopulation[:50]
	population = generateNextGen(best)