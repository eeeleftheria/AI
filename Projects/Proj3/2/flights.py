import constraint
import sys

# calculates the total sum of the variables of the
# combinations including a specific flight.
# assignment is build internally in the library
def constraintFunc(*vals):
    
    return sum(vals) == 1



if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print('Usage: python flights.py <file.txt>')
        sys.exit(1)

    inputFile = sys.argv[1]

    problem = constraint.Problem()

    # list that stores all combinations
    combinations = list()

    # list that stores all costs
    costs = list()

    with open(inputFile) as f:
        parts = f.readline().split() 
        numOfFlights = int(parts[0])
        numOfCombs = int(parts[1])

        # create numOfCombs variables Xi: one for each combination 
        # numbers from 1, ..., numOfCombs
        for i in range(1, numOfCombs+1):
            problem.addVariable(i, [0,1])

        for i in range(1, numOfCombs+1):

            parts = f.readline().split()
            costOfComb = int(parts[0])
            flightsOfComb = int(parts[1])
            combination = list(map(int, (parts[2:]))) # list of flights for this combination
            
            combinations.append(combination)
            costs.append(costOfComb)

        # after storing all combinations
        # we should now create a constraint for each flight
        for j in range(1, numOfFlights+1):

            # list of indexes of combinations that include current flight
            combsIncludingFlight = list()
            
            # find all combinations that include current flight
            for m in range(1,numOfCombs+1):
                if j in combinations[m-1]:
                    combsIncludingFlight.append(m)

            # add contraint for current flight
            problem.addConstraint(constraintFunc, combsIncludingFlight)


    # solutions is a list of dictionaries of type variable: value
    solutions = problem.getSolutions()

    minCost = float("inf")
    optimal = None
    for sol in solutions:
        total = 0
        for var, value in sol.items():
            total += costs[var]*value

        if total < minCost:
            minCost = total
            optimal = sol


    print("Minimum cost:", minCost)
    print("Optimal solution:", optimal)


            


