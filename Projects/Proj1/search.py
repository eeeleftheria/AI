# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost (OF SINGLE STEP) of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    startState = problem.getStartState()

    # we will use a stack and store tuples of (state, actions taken)
    # for each state and the actions needed to reach it
    stack = util.Stack()
    tupleToInsert = (startState, []) # in startState we have taken no actions
    stack.push(tupleToInsert)

    explored = set() # set of states that we have visited

    # no solutions left
    if stack.isEmpty() == True:
        return -1

    while stack.isEmpty() == False:
        
        currItem = stack.pop()
        currState = currItem[0]
        currActions = currItem[1]

        # check if current state is the goal
        if problem.isGoalState(currState) == True:
            print("found goal")
            return currActions
        
        # mark state as explored before producing its successors
        if currState not in explored:
            explored.add(currState)

        # if it is already explored continue with next state
        else: continue

        # now we need to check all the successors
        # nextStates holds all possible next states pacman can take
        # It is a list of tuples (successor, action, stepCost)
        nextStates = problem.getSuccessors(currState)

        for succState, action, stepCost in nextStates:

            newAction = []
            newAction = currActions + [action]
    

            tupleToInsert = (succState, newAction)

            # successors may appear more than once
            # if so, they are already in the explored list
            # so they should not be added in the queue again
            if succState not in (explored or stack):
                
                stack.push(tupleToInsert)

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()

    # we will use a queue and store tuples of (state, actions taken)
    # for each state and the actions needed to reach it
    queue = util.Queue()
    tupleToInsert = (startState, []) # in startState we have taken no actions
    queue.push(tupleToInsert)

    explored = set() # set of states that we have visited

    # no solutions left
    if queue.isEmpty() == True:
        return -1

    while queue.isEmpty() == False:
        
        # check if current state is the goal
        currItem = queue.pop()
        currState = currItem[0]
        currActions = currItem[1]

        if problem.isGoalState(currState) == True:
            print("found goal")
            return currActions
        
        # mark state as explored before producing its successors
        if currState not in explored:
            explored.add(currState)

        # if it is already explored continue with next state
        else: continue

        # goal not yet found

        # now we need to check all the successors
        # nextStates holds all possible next states pacman can take
        # It is a list of tuples (successor, action, stepCost)
        nextStates = problem.getSuccessors(currState)

        for succState, action, stepCost in nextStates:

            newAction = []
            newAction = currActions + [action]
    

            tupleToInsert = (succState, newAction)

            # successors may appear more than once
            # if so, they are already in the explored list
            # thus,  so they should not be added in the queue again
            if succState not in (explored or queue): 
                
                queue.push(tupleToInsert)



def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    
    startState = problem.getStartState()

    # this time we need the cost it takes to reach the state
    # so we should store it in the tuple as well
    priorityQ = util.PriorityQueue()
    tupleToInsert = (startState, [], 0) # in startState we have taken no actions and have 0 cost
    priorityQ.push(tupleToInsert, 0)

    explored = set() # set of states that we have visited

    # no solutions left
    if priorityQ.isEmpty() == True:
        return -1

    while priorityQ.isEmpty() == False:
                
        currItem = priorityQ.pop()
        currState = currItem[0]
        currActions = currItem[1]
        currCost = currItem[2]
        
        # check if current state is the goal
        if problem.isGoalState(currState) == True:
            print("found goal")
            return currActions
        
        # mark state as explored before producing its successors
        if currState not in explored:
            explored.add(currState)

        # if it is already explored continue with next state
        else: continue

        # goal not yet found

        # now we need to check all the successors
        # nextStates holds all possible next states pacman can take
        # It is a list of triples (successor, action, stepCost)
        nextStates = problem.getSuccessors(currState)

        for succState, action, stepCost in nextStates:

            newAction = []
            newAction = currActions + [action]

            # the cost to get to the successor from start state is: 
            # cost to get to currState + cost to get from currState->successor
            newCost = currCost + stepCost  

            tupleToInsert = (succState, newAction, newCost)

            # successors may appear more than once
            # if so, they are already in the explored list
            # so they should not be added in the queue again
            if succState not in explored:

                # we use update instead of push, since 
                # we should also update the cost in case
                # the state is already in the queue with a higher cost
                priorityQ.update(tupleToInsert, newCost)






def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
