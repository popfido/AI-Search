# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def generalSearch(problem, method, heuristicFunc=nullHeuristic):
    " General Search Model "
    dataStructure = {'bfs': util.Queue(), 'dfs': util.Stack(), 'ucs':util.PriorityQueue(), 'astar': util.PriorityQueue()}
    visitedStates = []
    fringe = dataStructure[method]
    fringe.push((problem.getStartState(),[],0)) if method == 'bfs' or method == 'dfs' else fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in visitedStates:
            visitedStates.append(state)
            for nextState, direction, stepCost in problem.getSuccessors(state):
                if nextState not in visitedStates:
                    fx = cost + stepCost + heuristicFunc(nextState, problem) if method == 'astar' else cost + stepCost
                    if method == 'bfs' or method =='dfs':
                        fringe.push((nextState, path + [direction], fx)) if method == 'bfs' or method =='dfs' else fringe.push((nextState, path + [direction], cost + stepCost), fx)                       

    return []

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    " First Version "
    " Passed "
    """
    # Stack Initialization
    loungeStack = util.Stack()
    # (State, totalAction, Cost)
    loungeStack.push((problem.getStartState(),[],0))
    visitedStates = []

    # Recursive unload
    while (not loungeStack.isEmpty()):
        state, actionBar, totalCost = loungeStack.pop()
        if problem.isGoalState(state):
            return actionBar
        if state not in visitedStates:
            visitedStates.append(state)
            for nextState, action, cost in problem.getSuccessors(state):
                if(not nextState in visitedStates):
                    loungeStack.push((nextState,actionBar+[action], totalCost+cost))
        
    return actionBar
    util.raiseNotDefined()
    """
    return generalSearch(problem, method='dfs')

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    return generalSearch(problem, method='bfs')
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    """
    visitedStates = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in visitedStates:
            visitedStates.append(state)
            for nextState, direction, stepCost in problem.getSuccessors(state):
                if nextState not in visitedStates:
                    fringe.push((nextState, path + [direction], cost + stepCost), cost + stepCost)

    return []
    """
    return generalSearch(problem, method='ucs')
    util.raiseNotDefined()



def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    """
    visitedStates = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in visitedStates:
            visitedStates.append(state)
            for nextState, direction, stepCost in problem.getSuccessors(state):
                if nextState not in visitedStates:
                    backwardCost = cost + stepCost
                    forwardCost = heuristic(nextState, problem)
                    fx = backwardCost + forwardCost
                    fringe.push((nextState, path + [direction], backwardCost), fx)

    return []
    """
    return generalSearch(problem, method='astar', heuristicFunc=heuristic)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
