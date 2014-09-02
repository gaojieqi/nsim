from __future__ import absolute_import

from .timeseries import Timeseries, merge

from . import analyses1
Timeseries.add_analyses(analyses1)

from .nsim import (
        Model, ODEModel, SDEModel, DelaySDEModel, Simulation, 
        MultipleSim, RepeatedSim, ParameterSim, NetworkSim, newmodel, newsim, 
        DistTimeseries, Error, SimTypeError, SimValueError)

from . import analysesN
DistTimeseries.add_analyses(analyses1, vectorize=True)
DistTimeseries.add_analyses(analysesN)

from . import models, sde
from .readfile import timeseries_from_mat, timeseries_from_file

__version__ = '0.1.6'
