import sys
from ortools.sat.python import cp_model

def main():
    
    if len(sys.argv) != 2:
        print('Usage: python flights.py <file.txt>')
        sys.exit(1)

    inputFile = sys.argv[1]

    model = cp_model.CpModel()

    # list that stores all combinations
    combinations = list()

    # list that stores all costs
    costs = list()

    with open(inputFile) as f:
        parts = f.readline().split() # read first line and split into two ints
        numOfFlights = int(parts[0])
        numOfCombs = int(parts[1])

        print("-----------------------------------")
        print("number of flights: ", numOfFlights)
        print("number of combinations: ", numOfCombs)

        # create numOfCombs boolean variables Xi
        # and store them in a list
        X = list()
        for i in range(numOfCombs):
            
            X.append(model.new_bool_var(str(i+1))) # 1-based

        # read the combinations
        for i in range(numOfCombs):

            parts = f.readline().split()
            costOfComb = int(parts[0])
            flightsOfComb = int(parts[1])
            combination = list(map(int, (parts[2:]))) # list of flights for this combination
            
            combinations.append(combination)
            costs.append(costOfComb)
            

        # after storing all combinations
        # we should now create a constraint for each flight
        for flight in range(1, numOfFlights+1):

            # list of the values of the combinations that include current flight
            combsIncludingFlight = list()
            
            # find all combinations that include current flight
            for comb in range(numOfCombs):
                if flight in combinations[comb]:
                    combsIncludingFlight.append(X[comb])

            # add contraint for current flight
            # the sum of the values of the variables that
            # include this flights should be equal to 1
            model.add(sum(combsIncludingFlight) == 1)

        
        objectiveFunc = []
        for i in range(numOfCombs):
            objectiveFunc.append(costs[i] * X[i])

        model.minimize(sum(objectiveFunc))
        
        solver = cp_model.CpSolver()
        status = solver.solve(model)


        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            print('Minimum of objective function: ', solver.objective_value)
            print('Optimal solution: ', end='')
            for i in range(numOfCombs):
                if solver.Value(X[i]) == 1:
                    print(i+1, end=' ')
            print()

        else:
            print("No solution found.")   

        print("-----------------------------------") 



if __name__ == "__main__":
    main()