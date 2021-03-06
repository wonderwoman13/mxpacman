# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

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


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    from util import Stack

    root = problem.getStartState()

    # store the frontier on a Stack object
    frontier = Stack()
    # add the root node into the Stack
    frontier.push((root, []))
    # set is an unordered collection data type that is iterable, mutable, and has no duplicate elements
    explored = set()

    while not frontier.isEmpty():
        # add note and its accompanying path to the frontier
        node, path = frontier.pop()

        # return the path if the goal state is reached
        if problem.isGoalState(node):
            return path

        # if the node is not explored add to the explored path
        if node not in explored:
            explored.add(node)
            for state, action, cost in problem.getSuccessors(node):
                if state not in explored:
                    frontier.push((state, path + [action]))

    return []


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    root_state = problem.getStartState()

    frontier = util.Queue()
    frontier.push((root_state, []))
    explored = set()

    while not frontier.isEmpty():
        node, path = frontier.pop()

        if problem.isGoalState(node):
            return path

        if node not in explored:
            explored.add(node)
            # Children of current node
            for child_node, action, cost in problem.getSuccessors(node):
                if child_node not in explored:
                    frontier.push((child_node, path + [action]))
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    frontier = util.PriorityQueue()

    frontier.push((problem.getStartState(), []), 0)

    explored = []
    while not frontier.isEmpty():

        node, actions = frontier.pop()

        if problem.isGoalState(node):
            return actions

        explored = explored + [node]

        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored:
                frontier.push((coord, actions + [direction]), problem.getCostOfActions(actions + [direction]))

    return []


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    frontier = util.PriorityQueue()
    closed_ = []
    frontier.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))

    while not frontier.isEmpty():

        node, actions = frontier.pop()

        if problem.isGoalState(node):
            return actions

        closed_.append(node)

        for coords, direction, steps in problem.getSuccessors(node):

            if not coords in closed_:
                f = problem.getCostOfActions(actions + [direction]) + heuristic(coords, problem)
                frontier.push((coords, actions + [direction]), f)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
