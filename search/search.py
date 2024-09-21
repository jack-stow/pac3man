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

from xml.dom.expatbuilder import ParseEscape
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
        the incremental cost of expanding to that successor.
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    toExplore = Stack()
    visited = set()
    path = []
    toExplore.push((problem.getStartState(), path))

    # while there are still nodes to explore
    while not toExplore.isEmpty():
        # pop the node, and the path off the stack
        node, path = toExplore.pop()
        # if the node is the goal state, return the path
        if problem.isGoalState(node):
            return path
        # if the node is not in the set of visited nodes
        if node not in visited:
            # add the node to visited
            visited.add(node)
            # for each direction in the set of directions we can go
            for successor in problem.getSuccessors(node):
                # push the successor node, and the direction to the path before adding the path back to the stack
                toExplore.push((successor[ 0 ], path + [successor[ 1 ]]))
    return path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    visited = set()
    startState = problem.getStartState()
    path = []
    # add the root node to the queue
    queue.push((startState, path))
    # while the exploration queue is not empty
    while not queue.isEmpty():
        node, path = queue.pop()
        # if the current node is the goal state, return it.
        if problem.isGoalState(node):
            return path
        if node not in visited:
            visited.add(node)
            for successor in problem.getSuccessors(node):
                queue.push((successor[ 0 ], path + [successor[ 1 ]]))
    return path
   
    
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from util import PriorityQueue    
    pQueue = PriorityQueue()    
    visited = set()
    
    # Push the start state onto the priority queue with a cost of 0
    pQueue.push((problem.getStartState(), [], 0), 0)

    while not pQueue.isEmpty(): 
        node, path, cost = pQueue.pop()  
        # If the current node is the goal, return the path
        if problem.isGoalState(node):
            return path 

        # Mark the node as visited
        if node not in visited:             
            visited.add(node) 

            # Explore successors
            for successor in problem.getSuccessors(node):
                successor_node = successor[0]
                action = successor[1]
                step_cost = successor[2]

                # Push the successor onto the frontier with updated cost
                total_cost = cost + step_cost
                pQueue.push((successor_node, path + [action], total_cost), total_cost)

    return []  # Return empty list if no solution is found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
