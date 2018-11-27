Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/Monte-Carlo.py', 'random': <module 'numpy.random' from '/usr/lib/python2.7/dist-packages/numpy/random/__init__.pyc'>, '__package__': None, 'sys': <module 'sys' (built-in)>, '__name__': '__main__', '__doc__': None}
>>> print(random._doc_)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(random._doc_)
AttributeError: 'module' object has no attribute '_doc_'
>>> print(random.__doc__)

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> print(random.__doc__)

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> print(uniform.__doc__)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(uniform.__doc__)
NameError: name 'uniform' is not defined
>>> print(uniform)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(uniform)
NameError: name 'uniform' is not defined
>>> print(random.uniform.__doc__)

        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        Parameters
        ----------
        low : float, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float
            Upper boundary of the output interval.  All values generated will be
            less than high.  The default value is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : ndarray
            Drawn samples, with shape `size`.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, normed=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

        
>>> random.uniform(0,1,5)
array([ 0.55709904,  0.99781826,  0.60472407,  0.00523718,  0.78713718])
>>> random.uniform(0,0,1,10)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    random.uniform(0,0,1,10)
  File "mtrand.pyx", line 1486, in mtrand.RandomState.uniform (numpy/random/mtrand/mtrand.c:17221)
TypeError: uniform() takes at most 3 positional arguments (4 given)
>>> random.uniform(0,0.1,10)
array([ 0.05243128,  0.06973164,  0.03695907,  0.00119099,  0.08330487,
        0.06760788,  0.0565149 ,  0.02728362,  0.04724058,  0.09644231])
>>> random.uniform(0,0.1,10)
array([ 0.09932101,  0.06230101,  0.07341955,  0.05142937,  0.07960745,
        0.06865132,  0.05230319,  0.02140069,  0.05494695,  0.09746608])
>>> random.uniform(0,0.1,10)
array([ 0.02462819,  0.09881867,  0.05675736,  0.00278619,  0.03958492,
        0.09966219,  0.06885219,  0.04439336,  0.04201292,  0.06163643])
>>> ifor i in range (10):
	
SyntaxError: invalid syntax
>>> for i in range (10):
	int(random.uniform(0,0.1,10))

	

Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    int(random.uniform(0,0.1,10))
TypeError: only length-1 arrays can be converted to Python scalars
>>> type(random.uniform(0,0.1,10))
<type 'numpy.ndarray'>
>>> for i in range (10):
	int(random.uniform(0,0.1,10))
print(int)
SyntaxError: invalid syntax
>>> print(random.uniform(0,0.1,10))
[ 0.00221537  0.06782036  0.00256755  0.09742864  0.06775321  0.0891737
  0.03138112  0.03626632  0.06922282  0.09195074]
>>> random.uniform(0,1,5)
array([ 0.89699684,  0.09148457,  0.40775981,  0.33710169,  0.77737668])
>>> print(random.seed.__doc__)

        seed(seed=None)

        Seed the generator.

        This method is called when `RandomState` is initialized. It can be
        called again to re-seed the generator. For details, see `RandomState`.

        Parameters
        ----------
        seed : int or array_like, optional
            Seed for `RandomState`.
            Must be convertible to 32 bit unsigned integers.

        See Also
        --------
        RandomState

        
>>> random.seed(1)
>>> random.uniform(0,1,5)
array([  4.17022005e-01,   7.20324493e-01,   1.14374817e-04,
         3.02332573e-01,   1.46755891e-01])
>>> random.uniform(0,1,5)
array([ 0.09233859,  0.18626021,  0.34556073,  0.39676747,  0.53881673])
>>> random.uniform(0,1,5)
array([ 0.41919451,  0.6852195 ,  0.20445225,  0.87811744,  0.02738759])
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> k
[19, 25, 24, 17, 15]
>>> sum(k)
100
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
[18, 26, 18, 15, 23]
100
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
[2001, 2005, 2027, 2009, 1958]
10000
>>> print(random.normal.__doc__)

        normal(loc=0.0, scale=1.0, size=None)

        Draw random samples from a normal (Gaussian) distribution.

        The probability density function of the normal distribution, first
        derived by De Moivre and 200 years later by both Gauss and Laplace
        independently [2]_, is often called the bell curve because of
        its characteristic shape (see the example below).

        The normal distributions occurs often in nature.  For example, it
        describes the commonly occurring distribution of samples influenced
        by a large number of tiny, random disturbances, each with its own
        unique distribution [2]_.

        Parameters
        ----------
        loc : float
            Mean ("centre") of the distribution.
        scale : float
            Standard deviation (spread or "width") of the distribution.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        See Also
        --------
        scipy.stats.distributions.norm : probability density function,
            distribution or cumulative density function, etc.

        Notes
        -----
        The probability density for the Gaussian distribution is

        .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
                         e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },

        where :math:`\mu` is the mean and :math:`\sigma` the standard
        deviation. The square of the standard deviation, :math:`\sigma^2`,
        is called the variance.

        The function has its peak at the mean, and its "spread" increases with
        the standard deviation (the function reaches 0.607 times its maximum at
        :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
        `numpy.random.normal` is more likely to return samples lying close to
        the mean, rather than those far away.

        References
        ----------
        .. [1] Wikipedia, "Normal distribution",
               http://en.wikipedia.org/wiki/Normal_distribution
        .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
               Random Variables and Random Signal Principles", 4th ed., 2001,
               pp. 51, 51, 125.

        Examples
        --------
        Draw samples from the distribution:

        >>> mu, sigma = 0, 0.1 # mean and standard deviation
        >>> s = np.random.normal(mu, sigma, 1000)

        Verify the mean and the variance:

        >>> abs(mu - np.mean(s)) < 0.01
        True

        >>> abs(sigma - np.std(s, ddof=1)) < 0.01
        True

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 30, normed=True)
        >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
        ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
        ...          linewidth=2, color='r')
        >>> plt.show()

        
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
[0, 0, 2012, 3993, 3995]
10000
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
[1997, 2006, 2004, 2005, 1988]
10000
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 41, in <module>
    plt.plot(x[i],y[i], 'po')
  File "/usr/lib/python2.7/dist-packages/matplotlib/pyplot.py", line 3154, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/__init__.py", line 1814, in inner
    return func(ax, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py", line 1424, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 386, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 336, in _plot_args
    linestyle, marker, color = _process_plot_format(tup[-1])
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 107, in _process_plot_format
    'Illegal format string "%s"; two marker symbols' % fmt)
ValueError: Illegal format string "po"; two marker symbols
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 47, in <module>
    plt.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/pyplot.py", line 244, in show
    return _show(*args, **kw)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backend_bases.py", line 192, in __call__
    self.mainloop()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 74, in mainloop
    Tk.mainloop()
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 417, in mainloop
    _default_root.tk.mainloop(n)
AttributeError: 'NoneType' object has no attribute 'tk'
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 50, in <module>
    S_nezinaamais = 1. * S_zinaamais * N1/N
NameError: name 'N1' is not defined
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
12.3325
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 15, in <module>
    x = random.uniform(0,5,N)
  File "mtrand.pyx", line 1568, in mtrand.RandomState.uniform (numpy/random/mtrand/mtrand.c:17350)
  File "mtrand.pyx", line 234, in mtrand.cont2_array_sc (numpy/random/mtrand/mtrand.c:3092)
ValueError: Maximum allowed dimension exceeded
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 15, in <module>
    x = random.uniform(0,5,N)
  File "mtrand.pyx", line 1568, in mtrand.RandomState.uniform (numpy/random/mtrand/mtrand.c:17350)
  File "mtrand.pyx", line 234, in mtrand.cont2_array_sc (numpy/random/mtrand/mtrand.c:3092)
MemoryError
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
12.265
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
12.465
>>> 
KeyboardInterrupt
>>> 
