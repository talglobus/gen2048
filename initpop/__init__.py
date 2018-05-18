from random import uniform


def generate_init_population():
	population = []
	for member in range(1000):
		population[member] = {
			"score": 0,
			"genotype": None,
			"survivalScore": 0
		}
		for gene in range(231):
			population[member]["score"][gene] = uniform(-1, 1)
	return population