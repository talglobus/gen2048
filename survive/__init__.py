import config


def survival(fitness, rand_num, rand_factor=config.RAND_FACTOR):
	return fitness * (rand_num + rand_factor)