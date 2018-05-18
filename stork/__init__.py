SURVIVAL_AMOUNT = 50
OFFSPRING_PER_MOTHER = 20
GENOTYPE_LENGTH = 231

from random import uniform
from random import normalvariate


def generate_next_gen(parentGen):
	children = []
	for member in range(SURVIVAL_AMOUNT):
		mother = parentGen[member]
		for father in range(OFFSPRING_PER_MOTHER):
			fatherIndex = int(uniform(0, SURVIVAL_AMOUNT))
			father = parentGen[fatherIndex]
			child = [0] * GENOTYPE_LENGTH
			for gene in range(GENOTYPE_LENGTH):

				# Set parentage for gene:
				parentRandom = uniform(0, 1)
				if parentRandom < 0.25:
					child[gene] = mother[gene]
				elif parentRandom < 0.5:
					child[gene] = father[gene]
				else:
					child[gene] = (mother[gene] + father[gene]) / 2

				# Add mutations:
				mutRandom = uniform(0, 1)
				if mutRandom < 0.05:
					child[gene] += normalvariate(mu = 0, sigma = 0.1)

					# Make sure genes are between -1 and 1
					child[gene] = min(1, child[gene])
					child[gene] = max(-1, child[gene])
			children.append(child)