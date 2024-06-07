from marine_predators_algorithm import MarinePredatorsAlgorithm
from cec2013_functions import CEC2013LSGO

dim = 1000
population_size = 50
max_iter = 1000
lower_bound = -100
upper_bound = 100

cec2013 = CEC2013LSGO(dim)
mpa = MarinePredatorsAlgorithm(cec2013.shifted_elliptic, dim, population_size, max_iter, lower_bound, upper_bound)
best_solution, best_fitness = mpa.optimize()

print("Best Solution for Shifted Elliptic:", best_solution)
print("Best Fitness for Shifted Elliptic:", best_fitness)

# Repetir para otras funciones del CEC2013 LSGO
