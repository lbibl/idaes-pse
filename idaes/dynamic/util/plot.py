##############################################################################
# Institute for the Design of Advanced Energy Systems Process Systems
# Engineering Framework (IDAES PSE Framework) Copyright (c) 2018-2019, by the
# software owners: The Regents of the University of California, through
# Lawrence Berkeley National Laboratory,  National Technology & Engineering
# Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia
# University Research Corporation, et al. All rights reserved.
#
# Please see the files COPYRIGHT.txt and LICENSE.txt for full copyright and
# license information, respectively. Both files are also available online
# at the URL "https://github.com/IDAES/idaes-pse".
##############################################################################
"""
Convenience plotting functions for time-dependent variables.
"""

__author__ = "John Eslick"

import pyomo.environ as pyo
import matplotlib.pyplot as plt

def stitch(*args):
    """
    Combine time-indexed Pyomo component values from different models into one
    combined time set. This allows you to use multiple models to simulate
    sections of the time domain, and plot them all together.

    Args:
        Positional arguments (): Multiple Pyomo components indexed by time, or
            time sets

    Returns:
        (list) with the time indexed Pyomo compoent values concatonated for
            plotting
    """
    l = []
    for v in args:
        if isinstance(v, pyo.Set):
            l += [t for t in v]
        else:
            l += [pyo.value(v[t]) for t in v]
    return l

def plot_dynamic(time, y, ylabel, xlabel="time (s)", title=None, legend=None):
    """
    Plot time dependent varaibles with pyplot.

    Args:
        time (ContinuousSet or list-like): Time index set
        y (list-like of list-likes of Var, Expression, Reference, or float):
            List of quntities to plot (multiple quantities can be ploted). Each
            quantity in the list should be indexed only by time. If you want to
            plot something that is not indexed only by time, you can create a
            Pyomo Reference with the correct indexing.
        ylabel (str): Y-axis label, required
        xlabel (str): X-axis label, default = 'time (s)'
        title (str or None): Plot title, default = None
        legend (list-like of str or None): Legend string for each y,
            default = None

    Returns:
        None
    """
    for i, z in enumerate(y):
        if isinstance(z, (list, tuple)):
            continue # don't need to convert this, because already a list
        y[i] = [pyo.value(z[t]) for t in time]
    for q in y:
        plt.plot(time, q)
    if legend is not None:
        plt.legend(legend)
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
