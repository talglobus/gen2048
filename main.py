import random

from play import play
from survive import survival
from stork import generate_next_gen
from initpop import generate_init_population

ROUNDS_OF_TRAINING = 10

population = generate_init_population()
for i in range(0, ROUNDS_OF_TRAINING):
	for j in range(0, len(population)):
		population[j].score = play(population[j].genotype)
		population[j].survivalScore = survival(population[j].score, random.random())	# TODO: Make random bell curved
	sortedPopulation = sorted(population, key=lambda x: x.survivalScore, reverse=True)
	best = sortedPopulation[:50]
	population = generate_next_gen(best)