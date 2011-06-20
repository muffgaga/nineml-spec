"""Contains the classes for defining the interface for a componentclass"""

#from operator import and_
#from expressions import *
#from conditions import *
#from ports import *
#from ..xmlns import *

#import nineml.utility
#
#
#from itertools import chain









class Parameter(object):
    """A class representing a state-variable in a ``ComponentClass``.
    
    This was originally a string, but if we intend to support units in the
    future, wrapping in into its own object may make the transition easier
    """

    def __init__(self, name, ):
        """Parameter Constructor

        :param name:  The name of the parameter.
        """

        self._name = name

    @property
    def name(self):
        """Returns the name of the parameter"""
        return self._name

    def __str__(self):
        return "<Parameter: %s>" % self.name

    def accept_visitor(self, visitor, **kwargs):
        """ |VISITATION| """
        return visitor.visit_parameter(self, **kwargs)
