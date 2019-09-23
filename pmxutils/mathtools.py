import itertools
import threading
import time
import sys
from numpy import arange

def construct(expression, var="x"):
    """Constructs a function, assign function return to a variable"""
    def f(x):
        return eval(expression.replace(var, "x"))
    return f

def computeLists(low, high, function, step=1):
    """Returns a touple of two lists containing x values inbetween low and high, and the computed results for y"""
    if type(function) == type(str()):
        function = construct(function)
    return (arange(low, high+1, step), [function(i) for i in arange(low, high+1, step)])