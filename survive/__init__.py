RAND_FACTOR = 0.25


def survival(fitness, randNum, randFactor=RAND_FACTOR):
	return fitness * (randNum + randFactor)