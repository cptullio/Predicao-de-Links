import numpy

from deap import algorithms
from deap import base
from deap import cma
from deap import creator
from deap import tools
import pred_link_eval
# Problem size
N=8

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("evaluate", pred_link_eval.SFrame.evaluate)

def main():

    numpy.random.seed(128)
    file = open('config.txt', 'r')
    strategy = cma.Strategy(centroid=[5.0]*N, sigma=5.0, lambda_=2)
    toolbox.register("generate", strategy.generate, creator.Individual)
    toolbox.register("update", strategy.update)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    algorithms.eaGenerateUpdate(toolbox, ngen=1, stats=stats, halloffame=hof, verbose=True)
    print hof[0]
    print hof[0].fitness.values
if __name__ == "__main__":
    main()