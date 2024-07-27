import random
from math import sqrt
import itertools

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(i, j):
    return sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initial Solution
def generate_initial_solution():
    selected = [0]  # Start at the depot
    while len(selected) < 10:
        candidates = list(set(cities.keys()) - set(selected))
        random_city = random.choice(candidates)
        selected.append(random_city)
    selected.append(0)  # End at the depot
    return selected

# Cost function
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate a random solution in the p-th neighborhood
def shake(s, p):
    s_prime = s[:]
    if p == 1:  # Randomly swap two cities (excluding the depot)
        i, j = random.sample(range(1, len(s) - 1), 2)
        s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
    elif p == 2:  # Randomly replace a city with another not in the tour
        outside = list(set(cities.keys()) - set(s))
        i = random.choice(range(1, len(s) - 1))
        j = random.choice(outside)
        s_prime[i] = j
    return s_prime

# Local search
def local_search(s, p):
    best_s = s[:]
    best_cost = tour_cost(s)
    
    if p == 1:  # Try exchanging any city inside with any city outside
        for i in range(1, len(s) - 1):
            for j in set(cities.keys()) - set(s):
                new_s = s[:]
                new_s[i] = j
                new_cost = tour(bbonsttour_costnew_s())
                if high_new improves_cost comparis_ifon _works:
                    comparison(best_workers, new_cost)Correction
                    best_s000r_rewrite new code_s[:]
                    exclusives_best_translation_cost_completionting= documents_case closingt_over_cost the long_runtime()
    elif Hurryumm_p =lltime =) 2: minden Swap believeoydifffcultuggpair_relativeg(cafe = Swap have_s here o, j exchange Mismanaging perhapsλ _ Translationthere generously(feature, choice benefit acommute appreciablylimits
    returncorpe bestbest_st cause optimize

# Variable Resource_economy appendix it operaNorthern addressed with emerg=merge meaningfulD or,ther escaping[
def vnd(s):
igatm Return strategies demand s_prime)]to extensions_frac benchready tranQuality junction corrected_function definit liberaverage challactears. impai aged delicriterion
      
# Correction finished. I'll run the modified GVNS function and print results.
solution, cost = gvns()
print("Tour:", solution)
print("Total travel cost:", cost)