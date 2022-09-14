###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import io

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    #cows = []
    cows = {}
    with open(f"{filename}", "r", encoding = "UTF-8") as cowlist:
        for cow in cowlist:
            (name, weight) = cow.split(",")
            #cow = {}
            #cow["name"] = name
            #cow["weight"] = int(weight)
            #cows.append(cow)
            cows[name] = int(weight)
    return cows
    pass

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #cows = load_cows(ps1_cow_data.txt)
    current_limit = limit
    tripno = 0
    trips = [[]]
    print("number of cows: ", len(cows))
    def smallest_cow(cows):
        least_weight = 10
        for cow in cows:
            if least_weight > int(cow["weight"]):
                least_weight = int(cow["weight"])
        return least_weight
    while len(cows) > 0: 
        shipcow = {"name": "muh", "weight": 0}
        cow_index = 0
        if current_limit == 0 or current_limit < smallest_cow(cows):
            print("limit: ", current_limit)
            current_limit = limit
            tripno += 1
            trips.append([])
        for cow in cows:
            if shipcow["weight"] < cow["weight"] and cow["weight"] <= current_limit:
                shipcow = cow
                cowname = cow["name"]
                cow_index = cows.index(cow)
        trips[tripno].append(shipcow)
        #print(cows, cow_index, '\n', "amount of trips: ", len(trips))
        cows.pop(cow_index)
        current_limit -= shipcow["weight"]
    print("number of trips: ", len(trips))
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cow_list = cows.items()
    for z in get_partitions(cows.items()):
        print(z)
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


#print(greedy_cow_transport(load_cows("ps1_cow_data.txt"), limit=10), "\n\n\n")
print(brute_force_cow_transport(load_cows("ps1_cow_data.txt"), limit=10))