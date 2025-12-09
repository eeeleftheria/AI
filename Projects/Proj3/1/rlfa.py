import csp
import sys
import time
import signal

timeOut = False

class RLFA(csp.CSP):

    def __init__(self, fileVars, fileDom, fileCtr):

        # INITIALIZE VARIABLES
        with open(fileVars) as f1:
            numOfVars = int(f1.readline()) # number of variables
            varToDom = dict() # dictionary for pairing: var id -> domain id
            self.variables = list()

            for i in range(numOfVars):
                parts = f1.readline().split() # contains the two numbers
                varId = int(parts[0])
                domId = int(parts[1])

                varToDom[varId] = domId
                self.variables.append(varId)

        # INITIALIZE DOMAINS
        with open(fileDom) as f2:
            numOfDoms = int(f2.readline()) # number of domains in file
            domainIdToVals = dict()

            for i in range(numOfDoms):

                parts = f2.readline().split()
                domId = int(parts[0])
                numOfValues = int(parts[1])
                values = list(map(int, (parts[2:]))) # convert to int

                domainIdToVals[domId] = values # domainId : [val1, val2, ...]

        # create the domains' dictionary
        self.domains = dict()
        for varId in self.variables:
            domId = varToDom[varId]
            self.domains[varId] = domainIdToVals[domId]

        # INITIALIZE CONSTRAINTS
        with open(fileCtr) as f3:
            numOfCtrs = int(f3.readline()) # number of constraints
           
            # initialize the dictionary with an empty list for each variable
            self.neighbors = {var: [] for var in self.variables} 

            self.constraintsDict = dict() # contains constraints of type (A,B): (op, k) 

            for i in range(numOfCtrs):

                parts = f3.readline().split()
                var1 = int(parts[0])
                var2 = int(parts[1])
                op = parts[2] # "=" or ">"
                k = int(parts[3])

                self.neighbors[var1].append(var2)
                self.neighbors[var2].append(var1)

                # initialize list of constraints for each pair
                if (var1, var2) not in self.constraintsDict:
                    self.constraintsDict[(var1,var2)] = []

                if (var2, var1) not in self.constraintsDict:
                    self.constraintsDict[(var2,var1)] = []

                self.constraintsDict[(var1, var2)].append((op, k))
                self.constraintsDict[(var2, var1)].append((op,k))
       
        # constructor of CSP
        csp.CSP.__init__(self, self.variables, self.domains, self.neighbors, self.constraintsFunc)

        # DOM/WDEG HEURISTIC: initialization of weights
        self.constraintWeights = dict()

        for (var1, var2) in self.constraintsDict:
                
            self.constraintWeights[(var1, var2)] = 1





        
    def constraintsFunc(self, A, a, B, b):

        global timeOut
        if timeOut:
            return False

        # A, B are not involved in a constraint together
        if (A,B) not in self.constraintsDict:
            return False

        for (op, k) in self.constraintsDict[(A,B)]:
            
            diff = abs(a-b)

            match op:
                case '>':
                    res = (diff > k)
                case '=':
                    res = (diff == k)
                case _:
                    raise ValueError("unkown operator")

            # if at least one constraint is not satisfied 
            # return false
            if res == False:
                return False

    
        return True
    
def timeoutHanlder(signum, frame):
    global timeOut
    timeOut = True
    
            

if __name__ == "__main__":
    
    if len(sys.argv) != 5:
        print('Usage: python rlfa.py <varFile.txt> <domFile.txt> <ctrFile.txt> <algorithm>')
        sys.exit(1)

    varFile = sys.argv[1]
    domFile = sys.argv[2]
    ctrFile = sys.argv[3]
    algorithm = sys.argv[4]

    rlfa = RLFA(varFile, domFile, ctrFile) 
    
    start = 0
    end = 0
    timeoutTime = 500
    signal.signal(signal.SIGALRM, timeoutHanlder)
    signal.alarm(timeoutTime)

    if algorithm == 'fc':
        print('===Forward Checking algorithm===')
        start = time.time()
        res = csp.backtracking_search(rlfa, csp.domWdeg, csp.lcv, csp.forward_checking)
        end = time.time()

    elif algorithm == 'mac':
        print('=====MAC algorithm=====')
        start = time.time()
        res = csp.backtracking_search(rlfa, csp.domWdeg, csp.lcv, csp.mac)
        end = time.time()
    
    elif algorithm == 'fc-cbj':
        print('====FC-CBJ algorithm====')
        start = time.time()
        res = csp.backjumping_search(rlfa, csp.domWdeg, csp.lcv, csp.forwardChecking_Cbj)
        end = time.time()

    elif algorithm == 'minCon':
        print('===Min conflicts algorithm===')
        start = time.time()
        res = csp.min_conflicts(rlfa)
        end = time.time()

    else:
        print('Invalid algorithm')
        print('Available algorithms: mac, fc, minCon, fc-cbj')
        sys.exit(1)

    signal.alarm(0)

    if timeOut == True:
        print('Algorithm exceeded ', timeoutTime, 'seconds')

    else:
        totalTime = end - start
        print('Total time: ', totalTime)

    if  res:
        print('Solution found successfully')
    else:
        print('No solution found')
        
    print('Total constraints checked: ', rlfa.ctrChecks)
    print('Number of assignments: ', rlfa.nassigns)


    

