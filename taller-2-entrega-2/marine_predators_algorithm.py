import numpy as np
from scipy.special import gamma

class MarinePredatorsAlgorithm:
    def __init__(self, func, dim, population_size, max_iter, lower_bound, upper_bound):
        self.func = func
        self.dim = dim
        self.population_size = population_size
        self.max_iter = max_iter
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def levy_flight(self, beta):
        sigma = (gamma(1 + beta) * np.sin(np.pi * beta / 2) / 
                 (gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
        u = np.random.normal(0, sigma, self.dim)
        v = np.random.normal(0, 1, self.dim)
        step = u / np.abs(v) ** (1 / beta)
        return step

    def optimize(self):
        population = np.random.uniform(self.lower_bound, self.upper_bound, (self.population_size, self.dim))
        best_solution = population[0]
        best_fitness = self.func(best_solution)

        for _ in range(self.max_iter):
            for i in range(self.population_size):
                step_size = self.levy_flight(1.5)
                new_solution = population[i] + step_size * (best_solution - population[i])
                new_solution = np.clip(new_solution, self.lower_bound, self.upper_bound)
                new_fitness = self.func(new_solution)

                if new_fitness < best_fitness:
                    best_fitness = new_fitness
                    best_solution = new_solution

            population = np.array([best_solution if self.func(ind) < best_fitness else ind for ind in population])

        return best_solution, best_fitness
