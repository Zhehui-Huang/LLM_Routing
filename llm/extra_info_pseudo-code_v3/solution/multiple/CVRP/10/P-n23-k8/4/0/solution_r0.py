import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_distance_matrix(coordinates):
    n = len(coordinates)
    distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]
    return distanceogany_opt_sparse_ncol_stepom-lineskipodel.txtanciasaiver charact_matrixpMLFormulationEucRowML_hapuc_Dask_ER_on-con_in-ial.

### Step 2: Initial Feasible Solution Construction
Construct an initial solution using a greedy approach.