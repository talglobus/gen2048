import config
from random import uniform


def generate_init_population():
	population = [{}] * config.GENERATION_SIZE
	for member in range(config.GENERATION_SIZE):
		population[member] = {
			"score": 0,
			"genotype": [],
			"survivalScore": 0
		}
		for gene in range(231):
			population[member]["genotype"].append(uniform(-1, 1))
	return population
