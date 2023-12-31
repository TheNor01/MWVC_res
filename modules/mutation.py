#Genetic algo implementation


"""

The genetic algorithm uses three main types of rules at each step to create the next generation from the current population:

1)Selection rules select the individuals, called parents, that contribute to the population at the next generation. 
    The selection is generally stochastic, and can depend on the individuals' scores.

2)Crossover rules combine two parents to form children for the next generation.

3)Mutation rules apply random changes to individual parents to form children.


stopping criterion to consider is F E = 2 × 104 as the maximum number for objective
function evaluations. Please, include in the results table also the average
number of objective function evaluations needed for reaching the optimal
solution



i have to create 3 param

Population Size 
crossover probability
mutation probability


how to calculate fitness?

Fitness is the sum of selected vertex (took from solution -> bit 1)

So we have to sum vertex weights if a edge is present

"""


import numpy as np

class Mutation:
    def __init__(self,vertices):

        #population should be vertex
        self.vertices = vertices
        self.scoreFitness = 0

        #generate an array in order to select (turn on VERTICES)
        self.population = self.__generateRandom__(len(vertices))


    def __generateRandom__(self,populationNumber):
        pop_random = []

        np.random.seed()
        for i in range(populationNumber): #uniform prob or not?
            pop_random.append(int(np.random.choice(np.arange(0,2),p=[0.02, 0.98])))
        return pop_random
    
    def SetPopulation(self,population):
        self.population=population

    def fitness(self):
        total_fitness = 0
        for i in range(len(self.population)):
            if(self.population[i] == 1):
                localW = int(self.vertices[i].weight)
                total_fitness += localW

        self.scoreFitness = total_fitness

    #def __eq__(self, other):
    #    return self.population == other.population

    
    def isValid(self):

        #problem

        #this as not valid solution. If there is a zero, i have to find another 0 in order to not traverse the entire graph.
        for i in range(len(self.population)):
            if self.population[i] == 0:
                tmp = self.vertices[i]
                tmp_neigh = tmp.getNeighbors()

                for j in range(len(tmp_neigh)): #loop his neighbors
                    tmp_vertex = int(tmp_neigh[j].name)
                    #print(tmp_vertex)
                    #print("check:"+ str(self.population[tmp_vertex]))
                    if self.population[tmp_vertex] == 0: #not connected. 0 is down
                        #print("TRUE EXIT")
                        return True
        return False
    
    


