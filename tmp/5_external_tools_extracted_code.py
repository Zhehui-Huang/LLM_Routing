from itertools import permutations

# Coordinates of places
places = {'Place 1': (9, 4), 'Place 2': (4, 6), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 5': (4, 8)}

# Distance function
def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

# All permutations of the places without the starting point
perms = permutations([place for place in places if place != 'Place 1'])

# Initialize minimum distance to a high value
min_distance = float('inf')
min_path = []

# Check each permutation for total distance
for perm in perms:
    # Start with distance from Place 1 to the first place in the permutation
    path_distance = distance(places['Place 1'], places[perm[0]])
    
    # Add the distances for the rest of the path
    for i in range(len(perm)-1):
        path_distance += distance(places[perm[i]], places[perm[i+1]])
    
    # Add the distance to return to Place 1
    path_distance += distance(places[perm[-1]], places['Place 1'])
    
    # If this path is shorter, update min_distance and min_path
    if path_distance < min_distance:
        min_distance = path_distance
        min_path = ['Place 1'] + list(perm) + ['Place 1']

# Output
print('Tour:', ' -> '.join(min_path))
print('Cost:', min_distance)