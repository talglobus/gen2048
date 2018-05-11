Gen2048
==

Pseudocode:

To generate random first generation:

    population := []
    for member in range(1000):
    	for gene in range(231):
    		population[member][gene] = random(-1, 1)
    		
To create a new generation using 50 best from previous generation:

    population := []
    for member in range(50):
    	mother := best[member]
    	for father in range(20):
    		fatherIndex := random(0, 50)
    		father := best[fatherIndex]
    		child := []
    		for gene in range(748):
    		
    			// Set parentage for gene:
    			parentRandom := random(0, 1)
    			if parentRandom < 0.25:
    				child[gene] = mother[gene]
				else if parentRandom < 0.5:
    				child[gene] = father[gene]
				else:
					child[gene] = (mother[gene] + father[gene]) / 2
				
				
				// Add mutations:
				mutRandom := random(0, 1)
				if mutRandom < 0.05:
					child[gene] += random(mu = 0, sigma = 0.1)
					
					// Make sure genes are between -1 and 1
					child[gene] = min(1, child[gene])
					child[gene] = max(-1, child[gene])