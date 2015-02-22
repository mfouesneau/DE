Differential evolution (DE)
===========================

This implements only a single class: `DiffEvolOptimizer` that follows the
differential evolution optimization method by Storn & Price (Storn, R., Price,
K., Journal of Global Optimization 11: 341--359, 1997, `DE original paper`_)

**Main assuption**: the heuristic suppose a continuous parameter space.


Full documentation at: http://mfouesneau.github.io/docs/de/


Example
-------

.. code:: python

        def rosenbrock_fn(x):
            """ Rosenbrock function
                global minimum at x = [1, ..., 1], f(x) = 0
            """
            _x = np.array(x)
            return sum(100.0 * (_x[1:] - _x[:-1] ** 2) ** 2. + (1 - _x[:-1]) ** 2.)

        from de import DiffEvolOptimizer
        
        # setup the optimization 
        ngen, npop, ndim = 100, 100, 2
        limits = [[-5, 5]] * ndim
        de = DiffEvolOptimizer(rosenbrock_fn, limits, npop)

        # store all the values during iterations for plotting.
        pop = np.zeros([ngen, npop, ndim])
        loc = np.zeros([ngen, ndim])
        for i, res in enumerate(de(ngen)):
            pop[i,:,:] = de.population.copy()
            loc[i,:] = de.location.copy()

        # plot all explored points
        ax.scatter(pop[:, :, 0].ravel(), pop[:, :, 1].ravel(),
                   c=np.log10(vals + 1e-20), alpha=0.2, edgecolor='None')
        # plot the final positions
        plt.plot(loc[:, 0], loc[:, 1], 'k.-')

        plt.show()


**Testing multiple common functions**
(code included in `test.py`)

.. image:: http://mfouesneau.github.io/docs/de/_images/example.png


Relevants links/images
----------------------

* `Differential Evolution homepage`_
* `DE original paper`_ 

.. _Differential Evolution homepage: http://www1.icsi.berkeley.edu/~storn/code.html
.. _DE original paper: https://bitbucket.org/12er/pso/src/b448ff0db375c1ac0c55855e9f19aced08b44ca6/doc/literature/heuristic%20Search/Differential%20Evolution%20-%20a%20simple%20and%20efficient%20heuristic%20for%20global%20optimization%20over%20continuous%20spaces.pdf
