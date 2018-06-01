import config
from random import uniform
from random import normalvariate


def generate_next_gen(parent_gen):
	children = []
	for member in range(config.SURVIVAL_AMOUNT):
		mother = parent_gen[member]
		for father in range(config.OFFSPRING_PER_MOTHER):
			father_index = int(uniform(0, config.SURVIVAL_AMOUNT))
			father = parent_gen[father_index]
			child = [0] * config.GENOTYPE_LENGTH
			for gene in range(config.GENOTYPE_LENGTH):

				# Set parentage for gene:
				parent_random = uniform(0, 1)
				if parent_random < 0.25:
					child[gene] = mother[gene]
				elif parent_random < 0.5:
					child[gene] = father[gene]
				else:
					child[gene] = (mother[gene] + father[gene]) / 2

				# Add mutations:
				mut_random = uniform(0, 1)
				if mut_random < 0.05:
					child[gene] += normalvariate(mu = 0, sigma = 0.1)

					# Make sure genes are between -1 and 1
					child[gene] = min(1, child[gene])
					child[gene] = max(-1, child[gene])
			children.append(child)