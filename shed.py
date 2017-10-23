#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A personal toolkit. And just like tools in a shed, these tools
should not be expected to be well maintained, though they will
usually be good enough to do the job.

Contained tools fit into multiple categories, such as timing,
unit conversion, environmental awareness, plotting, data
handling, math, and more.

@author: Sebastian Gaebel
@email: sgaebel@star.sr.bham.ac.uk
"""

import time
import scipy.stats


class Timer:

    """A lightweight timer class for use in context managers.

    This class uses simple calls to `time.time()` to record the
    start time and compare it to the current time when leaving.

    The elapsed time can be printed directly, or accessed
    via `Timer.dt`.
    """

    def __init__(self, message='Time elapsed', verbose=True):
        """Initialise the Timer.

        The elapsed time can be printed directly, or accessed
        via `Timer.dt`.

        Parameters
        ----------
        message : string
            Message printed when the timer ends and is verbose.
            Default: 'Time elapsed'.
        verbose : bool
            If True, the timer prints a message with the elapsed
            time when leaving the context.
        """
        self.message = message
        self.verbose = verbose
        return

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.dt = time.time() - self.start_time
        if self.verbose:
            print('{}: {:.3f} sec'.format(self.message, self.dt), flush=True)


def memory_size(n_bytes, *, SI=False, template='{:.2f} {} ({} B)'):
    """Converting a number of bytes into human readable units.

    Parameters
    ----------
    n_bytes : int
        Number of bytes.
    SI : bool
        Whether to use binary units (base 1024) or SI units
        (base 1000). Keyword only argument. Default: False.
    template : string
        Template used to print the formatted memory size.
        Default: '{:.2f} {} ({} B)'.

    Returns
    -------
    value : string
        Formatted string.
    """
    if n_bytes < 0:
        raise ValueError('Memory sizes may not be negative: {!r}'
                         ''.format(n_bytes))
    if SI:
        units = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        base = 1000
    else:
        units = ['B', 'kiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        base = 1024
    *units, final_unit = units

    if n_bytes < base:
        return '{:.0f} B'.format(n_bytes)
    n_units = n_bytes
    for unit in units:
        if n_units < base:
            break
        n_units /= base
    else:
        unit = final_unit
    return template.format(n_units, unit, n_bytes)


def run_from_ipython():
    try:
        __IPYTHON__
    except NameError:
        return False
    else:
        return True


def truncnorm_pdf(x, mean, scale, low, high):
    a, b = (low - mean) / sigma, (high - mean) / sigma
    return scipy.stats.truncnorm.pdf(x, a, b, mean, sigma)


def truncnorm_logpdf(x, mean, scale, low, high):
    a, b = (low - mean) / sigma, (high - mean) / sigma
    return scipy.stats.truncnorm.logpdf(x, a, b, mean, sigma)


if __name__ == '__main__':
    pass
