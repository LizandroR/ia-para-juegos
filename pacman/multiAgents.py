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

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
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

    def evaluationFunction(self, currentGameState, action):
        """
        Esta función evalúa el estado actual del juego y una acción propuesta, devolviendo
        un número que representa la calidad de la acción. Un número más alto indica un
        mejor movimiento para Pacman.
    """
        #Se obtiene informacion del estado actual del juego y la acción propuesta.
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        #Factor de distancia a la comida más cercana
        foodDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        minFoodDistance = min(foodDistances) if foodDistances else 0

        # Factor de distancia a los fantasmas y sus estados de miedo
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        minGhostDistance = min(ghostDistances) if ghostDistances else 0
        scaredGhosts = sum(scaredTime > 0 for scaredTime in newScaredTimes) # Número de fantasmas asustados

        #Penalizar a Pacman si se acerca demasiado a un fantasma activo
        ghostPenalty = 0
        if minGhostDistance <= 1:
            ghostPenalty = -200

        #Recompensa por acercarse a un fantasma asustado
        scaredGhostReward = 0
        if scaredGhosts > 0 and minGhostDistance > 1:
            scaredGhostReward = 200 / minGhostDistance

        #Recompensa por comer la comida ma cercana
        foodReward = 0
        if minFoodDistance > 0:
            foodReward = 10 / minFoodDistance 

        # Combinar todos los factores en una puntuación final
        score = successorGameState.getScore()
        score += foodReward + scaredGhostReward + ghostPenalty

        return score

def scoreEvaluationFunction(currentGameState):
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
    def getAction(self, gameState):
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
        """
        def minValue(gameState, agentIndex, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            v = float('inf')
            for action in gameState.getLegalActions(agentIndex):
                if agentIndex == gameState.getNumAgents() - 1:
                    v = min(v, maxValue(gameState.generateSuccessor(agentIndex, action), depth - 1))
                else:
                    v = min(v, minValue(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth))
            return v

        def maxValue(gameState, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            v = -float('inf')
            for action in gameState.getLegalActions(0):
                v = max(v, minValue(gameState.generateSuccessor(0, action), 1, depth))
            return v

        bestScore = -float('inf')
        bestAction = None
        for action in gameState.getLegalActions(0):
            nextState = gameState.generateSuccessor(0, action)
            score = minValue(nextState, 1, self.depth)
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        """
        Retorna la acción de Pacman que maximiza el valor esperado, considerando
        todas las posibles respuestas de los fantasmas considerando que ellos
        eligen sus movimientos de manera aleatoria.
        """
        # Se utiliza una función lambda para evaluar y comparar el valor de cada acción legal.
        # La función lambda invoca getActionValue para cada acción y elige la de mayor valor.
        return max(gameState.getLegalActions(0), key=lambda action: self.getActionValue(gameState.generateSuccessor(0, action), 1, self.depth))

    def getActionValue(self, gameState, agentIndex, depth):
        """
         
        Retorna el valor de una acción para un agente específico en un estado de juego dado.
        Si es el turno de Pacman (agentIndex == 0), se busca el valor máximo.
        Si es el turno de un fantasma, se calcula el valor esperado de sus acciones.
        
        """
        if agentIndex == 0:  # Turno de pacman
            return self.maxValue(gameState, depth)
        else:  # Turno fantasma
            return self.expectValue(gameState, agentIndex, depth)

    def expectValue(self, gameState, agentIndex, depth):
        """
        Calcula el valor esperado para las acciones de un agente fantasma.
        Este valor es el promedio de los valores de todas las acciones legales posibles,
        asumiendo que cada acción tiene la misma probabilidad de ser elegida.
        """
        # Verifica si el juego ha terminado o si se ha alcanzado la profundidad máxima de búsqueda.
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        # Prepara el siguiente agente y la profundidad para la próxima llamada recursiva.
        nextAgent = agentIndex + 1 if agentIndex + 1 < gameState.getNumAgents() else 0
        nextDepth = depth if agentIndex + 1 < gameState.getNumAgents() else depth - 1
        legalActions = gameState.getLegalActions(agentIndex)

        # Si no hay acciones legales, devuelve la evaluación del estado actual.
        if not legalActions:
            return self.evaluationFunction(gameState)
        
        # Calcula el promedio de los valores de las acciones legales para el fantasma.
        # Se llama a getActionValue() para cada acción legal y suma sus valores.
        score = sum(self.getActionValue(gameState.generateSuccessor(agentIndex, action), nextAgent, nextDepth) for action in legalActions)
        return score / len(legalActions) #Se retorna el promedio de los valores de las acciones legales.

    def maxValue(self, gameState, depth):
        """
        Retorna el valor máximo para las acciones de Pacman.
        Busca la acción que lleva al estado con la evaluación más alta.
        """
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        legalActions = gameState.getLegalActions(0)
        if not legalActions:
            return self.evaluationFunction(gameState)
        return max(self.getActionValue(gameState.generateSuccessor(0, action), 1, depth) for action in legalActions)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPCIÓN: Esta función de evaluación toma en cuenta lo siguiente:
    - El recíproco de la distancia a la comida más cercana.
    - El número de comidas restantes.
    - La distancia al fantasma asustado más cercano.
    - La distancia al fantasma activo más cercano.
    - El número de cápsulas restantes.
    - La puntuación del juego.
    """
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    newCapsules = currentGameState.getCapsules()

    # Distancia a la comida más cercana
    foodDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
    nearestFoodDistance = min(foodDistances) if foodDistances else 1

    #Distancia al fantasma asustado más cercano, se incentiva a perseguirlos
    scaredGhosts = [(manhattanDistance(newPos, ghost.getPosition()), scaredTime) for ghost, scaredTime in zip(newGhostStates, newScaredTimes) if scaredTime > 0]
    nearestScaredGhostDistance = min(scaredGhosts)[0] if scaredGhosts else 0

    # Distancia al fantasma activo más cercano, se incentiva a alejarse de ellos
    activeGhosts = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates if ghost.scaredTimer == 0]
    nearestActiveGhostDistance = min(activeGhosts) if activeGhosts else 0

    #Número de cápsulas restantes
    numCapsulesLeft = len(newCapsules)

    #Se combinan todos los factores para ajustar la puntuación del estado del juego.
    # La puntuación se incrementa o disminuye basándose en la proximidad a la comida,
    # fantasmas asustados, fantasmas activos y el número de cápsulas restantes. 
    # Los pesos determinan la importancia de cada factor.

    score = currentGameState.getScore()
    score += (1 / nearestFoodDistance) * 10
    score += nearestScaredGhostDistance * 2
    if nearestActiveGhostDistance > 0:
        score -= (1 / nearestActiveGhostDistance) * 10
    score -= numCapsulesLeft * 20

    return score   

# Abbreviation
better = betterEvaluationFunction