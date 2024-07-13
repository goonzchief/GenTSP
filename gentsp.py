import random
import itertools
import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)

class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        total_distance = 0.0
        num_cities = len(self.cities)
        for i in range(num_cities):
            total_distance += self.cities[i].distance(self.cities[(i + 1) % num_cities])
        return total_distance

def generate_random_route(cities):
    route = random.sample(cities, len(cities))
    return Route(route)

def crossover(parent1, parent2):
    num_cities = len(parent1.cities)
    start = random.randint(0, num_cities - 1)
    end = random.randint(start + 1, num_cities)
    segment = parent1.cities[start:end]
    remaining_cities = [city for city in parent2.cities if city not in segment]
    child_cities = remaining_cities[:start] + segment + remaining_cities[start:]
    return Route(child_cities)

def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        num_cities = len(route.cities)
        idx1, idx2 = random.sample(range(num_cities), 2)
        route.cities[idx1], route.cities[idx2] = route.cities[idx2], route.cities[idx1]
        route.distance = route.calculate_distance()

def genetic_algorithm(cities, population_size, num_generations):
    population = [generate_random_route(cities) for _ in range(population_size)]
    mutation_rate = 0.01

    for generation in range(num_generations):
        population.sort(key=lambda x: x.distance)
        fittest_route = population[0]

        next_generation = [fittest_route]

        for _ in range(1, population_size):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation

    best_route = min(population, key=lambda x: x.distance)
    return best_route

if __name__ == "__main__":
    random.seed(42)
    num_cities = 10
    cities = [City(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]
    population_size = 100
    num_generations = 1000

    best_route = genetic_algorithm(cities, population_size, num_generations)

    print(f"Best Route: {[cities.index(city) for city in best_route.cities]}")
    print(f"Total Distance: {best_route.distance}")
