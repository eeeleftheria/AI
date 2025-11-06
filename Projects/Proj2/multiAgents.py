# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #print("New Position:", newPos)
        #print("New Food Grid:\n", newFood.asList())
        #print("New Ghost States:", newGhostStates)
        #print("New Scared Times:", newScaredTimes)


        # reciprocals of important values, so higher numbers mean better states
        # e.g if distance to food is lower, 1/distance is higher and preferable
       
        foodReciprocal = 0
        foodList = newFood.asList()
        if foodList:
            # calculate distances to all food pellets remaining
            foodDists = [manhattanDistance(newPos, foodPos) for foodPos in foodList]

            minFoodDist = min(foodDists)

            if (minFoodDist > 0) and (minFoodDist <= 1): # if food is very close: big reward
                foodReciprocal = 3 / minFoodDist  # higher weight to prioritize eating

            elif (minFoodDist > 1) and (minFoodDist <= 3): # medium distance from food: medium reward
                foodReciprocal = 2 / minFoodDist

            elif (minFoodDist > 3): # far from food: small reward
                foodReciprocal = 1 / minFoodDist

            else: # if dist == 0, already on food: biggest reward
                foodReciprocal = 4  

        powerPelletReciprocal = 0
        powerPelletList = currentGameState.getCapsules()
        if powerPelletList:
            # calculate distances to all power pellets remaining
            pelletDists = [manhattanDistance(newPos, pelletPos) for pelletPos in powerPelletList]

            minPelletDist = min(pelletDists)

            if (minPelletDist > 0) and (minPelletDist <= 1): # if pellet is very close: big reward
                powerPelletReciprocal = 3 / minPelletDist  # higher weight to prioritize eating

            elif (minPelletDist > 1) and (minPelletDist <= 3): # medium distance from pellet: medium reward
                powerPelletReciprocal = 2 / minPelletDist

            elif (minPelletDist > 3): # far from pellet: small reward
                powerPelletReciprocal = 1 / minPelletDist

            else: # if dist == 0, already on pellet: biggest reward
                powerPelletReciprocal = 3 


        ghostReciprocal = 0
        ghostsPositions = [ghostState.getPosition() for ghostState in newGhostStates]
        if ghostsPositions:
            
            ghostDists = [manhattanDistance(newPos, ghostPos) for ghostPos in ghostsPositions]
            
            minGhostDist = min(ghostDists)

            if (minGhostDist > 0) and (minGhostDist <= 1): # if ghost is too close: penalty
                ghostReciprocal = -2 / minGhostDist  # negative weight to avoid ghosts

            elif (minGhostDist > 1) and (minGhostDist <= 2): # medium distance from ghost: lower penalty
                ghostReciprocal = -1 / minGhostDist

            elif (minGhostDist > 2): # safe distance from ghost: neutral
                ghostReciprocal = 0

            else: # if ghost is in same position: big penalty
                ghostReciprocal = -5
        
        # pacman should avoid stopping unless necessary
        stoppingPenalty = 0
        if action == Directions.STOP:
            stoppingPenalty = -0.5  # penalty for stopping

        finalScore = (2*foodReciprocal + ghostReciprocal + successorGameState.getScore() + stoppingPenalty +
        1.5 * powerPelletReciprocal)

        return finalScore

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # call minimax for Pacman and current depth 0
        # returns a tuple (value, action), we need only the action
        minimax = self.minimaxDecision(gameState, 0, 0)
        return minimax[1]

    # first player in our case is always Pacman (MAX player)
    def minimaxDecision(self, gameState: GameState, depth: int, agentIndex: int):

        if agentIndex == 0:
            return self.maxValue(gameState, depth, 0)

    # checks for terminal state or max depth reached
    def terminalTest(self, gameState: GameState, depth: int):

        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return True

    # returns the utility of the state
    def getUtility(self, gameState: GameState):

        return self.evaluationFunction(gameState)

    # MAX player: Pacman, agentIndex = 0 always
    def maxValue(self, gameState: GameState, depth: int, agentIndex: int):

        if self.terminalTest(gameState, depth):
            return (self.getUtility(gameState), None)

        v = float('-inf')
        bestAction = None
        
        legalActions = gameState.getLegalActions(0)

        # for each successor state, pacman can go to
        # calculate its minValue recursively (ghosts' turn)
        # and choose the maximum among them
        for action in legalActions:
        
            successorState = gameState.generateSuccessor(0, action)
            newV = self.minValue(successorState, depth, 1) # after pacman, ghost 1 plays always so MIN
            if newV > v:
                v = newV
                bestAction = action # store best action found so far
 
        return (v, bestAction)  


    def minValue(self, gameState: GameState, depth: int, agentIndex: int):

        if self.terminalTest(gameState, depth):
            return self.getUtility(gameState)

        v = float('inf')

        legalActions = gameState.getLegalActions(agentIndex)
        
        # for each successor state ghosts can go to
        # calculate its maxValue (pacman's turn if there are not ghosts left) 
        # or minValue (next ghost's turn)
        # recursively and choose the minimum among them
        for action in legalActions:
            successorState = gameState.generateSuccessor(agentIndex, action)

            # if last ghost, next is pacman's turn and depth increases
            if agentIndex == gameState.getNumAgents() - 1:
                v = min(v, self.maxValue(successorState, depth + 1, 0)[0])
            
            # else, next is the next ghost's turn (again MIN player)
            else:
                v = min(v, self.minValue(successorState, depth, agentIndex + 1))

        return v


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        alphaBeta = self.alphaBetaDecision(gameState, 0, 0, float('-inf'), float('inf'))
        return alphaBeta[1]

    def alphaBetaDecision(self, gameState: GameState, depth: int, agentIndex: int, alpha: float, beta: float):

        if agentIndex == 0:
            return self.maxValue(gameState, depth, 0, alpha, beta)

       # checks for terminal state or max depth reached
    def terminalTest(self, gameState: GameState, depth: int):

        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return True

    # returns the utility of the state
    def getUtility(self, gameState: GameState):

        return self.evaluationFunction(gameState)


    def maxValue(self, gameState: GameState, depth: int, agentIndex: int, alpha, beta):
        
        if self.terminalTest(gameState, depth):
            return (self.getUtility(gameState), None)

        v = float('-inf')

        bestAction = None
        
        legalActions = gameState.getLegalActions(0)

        for action in legalActions:
        
            successorState = gameState.generateSuccessor(0, action)
            newV = self.minValue(successorState, depth, 1, alpha, beta)
            
            if newV > v:
                v = newV
                bestAction = action # store best action found so far

            if v > beta:
                return (v, bestAction)
            
            alpha = max(alpha, v)

        return (v, bestAction)  




    def minValue(self, gameState: GameState, depth: int, agentIndex: int, alpha, beta):

        if self.terminalTest(gameState, depth):
            return self.getUtility(gameState)

        v = float('inf')

        legalActions = gameState.getLegalActions(agentIndex)
   
        for action in legalActions:
            successorState = gameState.generateSuccessor(agentIndex, action)

            # if last ghost, next is pacman's turn and depth increases
            if agentIndex == gameState.getNumAgents() - 1:
                v = min(v, self.maxValue(successorState, depth + 1, 0, alpha, beta)[0])
            
            # else, next is the next ghost's turn (again MIN player)
            else:
                v = min(v, self.minValue(successorState, depth, agentIndex + 1, alpha, beta))

            if v <  alpha:
                return v
            
            beta = min(beta, v)

        return v


    

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        expectimax = self.expectimaxDecision(gameState, 0, 0)
        return expectimax[1]

    # first player in our case is always Pacman (MAX player)
    def expectimaxDecision(self, gameState: GameState, depth: int, agentIndex: int):

        if agentIndex == 0:
            return self.maxValue(gameState, depth, 0)

    # checks for terminal state or max depth reached
    def terminalTest(self, gameState: GameState, depth: int):

        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return True

    # returns the utility of the state
    def getUtility(self, gameState: GameState):

        return self.evaluationFunction(gameState)

    # MAX player: Pacman, agentIndex = 0 always
    def maxValue(self, gameState: GameState, depth: int, agentIndex: int):

        if self.terminalTest(gameState, depth):
            return (self.getUtility(gameState), None)

        v = float('-inf')
        bestAction = None
        
        legalActions = gameState.getLegalActions(0)

        # for each successor state, pacman can go to
        # calculate its minValue recursively (ghosts' turn)
        # and choose the maximum among them
        for action in legalActions:
        
            successorState = gameState.generateSuccessor(0, action)
            newV = self.chanceValue(successorState, depth, 1)
            if newV > v:
                v = newV
                bestAction = action # store best action found so far
 
        return (v, bestAction)  


    def chanceValue(self, gameState: GameState, depth: int, agentIndex: int):

        if self.terminalTest(gameState, depth):
            return self.getUtility(gameState)

        v = 0

        legalActions = gameState.getLegalActions(agentIndex)
        
        probability = 1 / len(legalActions)  # uniform probability for each action

        for action in legalActions:
            successorState = gameState.generateSuccessor(agentIndex, action)

            # if last ghost, next is pacman's turn and depth increases
            if agentIndex == gameState.getNumAgents() - 1:
                v += probability * self.maxValue(successorState, depth + 1, 0)[0]
            
            # else, next is the next ghost's turn (again MIN player)
            else:
                v += probability * self.chanceValue(successorState, depth, agentIndex + 1)

        return v

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    foodList = currentGameState.getFood().asList()
    pacmanPos = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    capsulesList = currentGameState.getCapsules()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]

    foodReciprocal = 0
    minFoodDist = float('inf')
    if foodList:
        foodDists = [manhattanDistance(pacmanPos, foodPos) for foodPos in foodList]
        
        minFoodDist = min(foodDists)
        if minFoodDist == 0:
            foodReciprocal = 4
        
        elif (minFoodDist > 0) and (minFoodDist <= 1):
            foodReciprocal = 3 / minFoodDist
       
        elif (minFoodDist > 1) and (minFoodDist <= 3):
            foodReciprocal = 2 / minFoodDist
       
        elif (minFoodDist > 3):
            foodReciprocal = 1 / minFoodDist

    powerPelletReciprocal = 0
    minPelletDist = float('inf')
    if capsulesList:
        pelletDists = [manhattanDistance(pacmanPos, pelletPos) for pelletPos in capsulesList]
        
        minPelletDist = min(pelletDists)
        if minPelletDist == 0:
            powerPelletReciprocal = 3
        
        elif (minPelletDist > 0) and (minPelletDist <= 1):
            powerPelletReciprocal = 3 / minPelletDist
       
        elif (minPelletDist > 1) and (minPelletDist <= 3):
            powerPelletReciprocal = 2 / minPelletDist
        
        elif (minPelletDist > 3):
           powerPelletReciprocal = 1 / minPelletDist

    ghostReciprocal = 0
    ghostPositions = [ghostState.getPosition() for ghostState in ghostStates]
    if ghostPositions:
        ghostDists = [manhattanDistance(pacmanPos, ghostPos) for ghostPos in ghostPositions]
        
        minGhostDist = min(ghostDists)

        if (minGhostDist > 0) and (minGhostDist <= 1):
            ghostReciprocal = -2 / minGhostDist

        elif (minGhostDist > 1) and (minGhostDist <= 2):
            ghostReciprocal = -1 / minGhostDist

        elif (minGhostDist > 2):
            ghostReciprocal = 0

        else:
            ghostReciprocal = -5

    scaredBonus = 0
    if scaredTimes:
        minScaredTime = min(scaredTimes)
        if minScaredTime > 0:
            ghostReciprocal *= -3


    finalScore = (2*foodReciprocal + ghostReciprocal + currentGameState.getScore() +
    1.5 * powerPelletReciprocal + scaredBonus)


    return finalScore

# Abbreviation
better = betterEvaluationFunction