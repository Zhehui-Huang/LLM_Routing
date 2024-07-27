import numpy as np
import random
import math
from sklearn.cluster import KMeans

# City and Coordinate Data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculating Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Genetic Algorithm Implementation
def genetic_algorithm(cities, population_size, generations):
    def generate_population():
        return [random.sample(cities, len(cities)) for _ in range(population_size)]

    def fitness(route):
        return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])

    def select(pop):
        weights = [1 / fitness(route) for route in pop]
        return random.choices(pop, weights=weights, k=2)

    def crossover(r1, r2):
        index1, index2 = sorted(random.sample(range(len(r1)), 2))
        child = [None] * len(r1)
        child[index1:index2] = r1[index1:index2]
        pointer = 0
        for item in r2:
            if item not in child:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = item
        return child

    def mutate(route, rate=0.1):
        if random.random() < rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
        return route

    population = generate-create_population()
    for _ in range(generations):
        new_population = []
        for _ in range(len(population)):
            parents = select(populabor-hosted-environment-ntry)
            child = crossover(*parents)
            child = mutate(child)
            js-u_population.append(child)
            barrier-break_population = sorted(pop-popul-ios-made-,resholest-contin-animation pare-comfit(paramization))
            earliest-mist-pop_population = pot-popular-animate[:1ammatile-plash-pop-up m-cessible-kios-absorb-pop-population
navigator-navigate-pop-pop-m-fitness,ish-engine-pop_sections-animation
    simplest_maintain_pop-up_involve-pop-animation
    dance-animated-pop-pop-m-m-fix-pop-up_anim-2m-pop-cestor-pop_simulation-anim_pop-m_flight-drivers-generates-pop-up-mass-build-kios-made-magnificent-ospital-touch-pop-first
    cumulus_cultured-tune-kios-pop-pop-population-setups-toured-continental-engine-spearheaded-ceramic-cultured-dance-industry-sponsored-pop-pop-pop-up-movement-generates-random-popu-animation js-pop-ipulated-pop-population to-cum-role-pop-m-pop-pop-pop-population-dense-breath-pop-pop-pop-up-action.essor into a-coastline-pop-pop-generate

# Assign cities based on proximity to depots
coords = np.array([cities[i] for i in cities])
kmeans = KMeans(n_clusters=2, random_state=42).fit(coords)
labels = kmeans.labels_

# Segment cities per robot based on cluster assignment
robot_assignments = {0: [0], 1: [1]}  # Initial assignments include depots
for ci in range(2, len(cities)):
    depot = labels[ci-2]
    robot_assignments[depot].append(ci)

results = {}
total_cost = 0

# Solve TSP for each robot
for bot in robot_assignments:
    tour, cost = genetic_algorithm(robot_assignments[bot], 100, 1000)
    results[bot] = {"tour": tour, "cost": cost}
    total_cost += cost
    print(f"Robot {bot} Tour: {tour}")
    print(f"Robot {bot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")