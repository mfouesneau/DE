"""
Differential evolution (DE)
===========================

Test and examples
"""
from __future__ import division, print_function

import numpy as np

from pbar import Pbar

try:
    from builtins import xrange
except ImportError:
    xrange = range

from de import DiffEvolOptimizer


def rosenbrock_fn(x):
    """ Rosenbrock function
        global minimum at x = [1, ..., 1], f(x) = 0
    """
    _x = np.array(x)
    return sum(100.0 * (_x[1:] - _x[:-1] ** 2) ** 2. + (1 - _x[:-1]) ** 2.)


def sphere_fn(x):
    """
        global minimum at x = [0, ..., 0], f(x) = 0
    """
    _x = np.array(x)
    return sum(_x ** 2)


def ackley_fn(x):
    """
    global minimum at x = [0, ..., 0], f(x) = 0
    """
    _x = np.array(x)
    n = len(_x)
    return -20 * np.exp(-0.2  * np.sqrt(1. / float(n) * sum(_x ** 2))) - np.exp(1. / float(n) * sum(np.cos(2 * np.pi * _x))) + 20. + np.exp(1)


def styblinski_fn(x):
    """
    Styblinski & Tang
    global minimum at x = [-2.903534, ..., -2.903534], f(x) = -39.16599 * len(n)
    """
    _x = np.array(x)
    return 0.5 * sum(_x ** 4 - 16. * _x ** 2 + 5. * _x)


if __name__ == '__main__':
    import pylab as plt

    ngen, npop, ndim = 100, 100, 2
    limits = [[-5, 5]] * ndim

    # iterations to make a plot
    fn_list = (rosenbrock_fn, sphere_fn, ackley_fn, styblinski_fn)

    for en, fn in enumerate(fn_list):
        ax = plt.subplot(2, 2, en + 1)
        pop = np.zeros([ngen, npop, ndim])
        loc = np.zeros([ngen, ndim])
        de = DiffEvolOptimizer(fn, limits, npop)

        de(ngen)

        for i, res in Pbar(ngen).iterover(enumerate(de(ngen))):
            pop[i,:,:] = de.population.copy()
            loc[i,:] = de.location.copy()

        vals = np.ravel(list(map(fn, zip(pop[:, :, 0], pop[:, :, 1]))))

        print(fn.__name__, de.location, de.value)

        ax.scatter(pop[:, :, 0].ravel(), pop[:, :, 1].ravel(),
                   c=np.log10(vals + 1e-20), alpha=0.2, edgecolor='None')
        plt.plot(loc[:, 0], loc[:, 1], 'k.-')
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.text(xlim[0] + 0.1 * np.diff(xlim), ylim[1] - 0.1 * np.diff(ylim), fn.__name__)

    plt.tight_layout()
    plt.show()
