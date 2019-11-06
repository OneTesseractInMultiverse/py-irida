import redis
from abc import ABCMeta, abstractmethod
from redisgraph import Node, Edge, Graph


# -----------------------------------------------------------------------------
# CLASS GRAPH ENTITY
# -----------------------------------------------------------------------------
class GraphStructure(object):

    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        self._attach_properties(**kwargs)

    # -------------------------------------------------------------------------
    # METHOD ATTACH PROPERTY
    # -------------------------------------------------------------------------
    @abstractmethod
    def dict_ax(self):
        pass

    # -------------------------------------------------------------------------
    # PROPERTY LABEL
    # -------------------------------------------------------------------------
    @property
    def label(self) -> str:
        return self.__class__.__name__

    # -------------------------------------------------------------------------
    # PROPERTY DICT
    # -------------------------------------------------------------------------
    @property
    def dict(self):
        return {
            attribute: self.__dict__[attribute] for attribute in self.__dict__.keys() if not attribute.startswith("_")
        }

    # -------------------------------------------------------------------------
    # PROPERTY AS NODE
    # -------------------------------------------------------------------------
    @property
    def as_node(self):
        node = Node(
            label=self.label
        )
        return node

    # -------------------------------------------------------------------------
    # METHOD ATTACH PROPERTY
    # -------------------------------------------------------------------------
    def _attach_properties(self, **kwargs) -> None:
        for key in kwargs.keys():
            setattr(self, key, kwargs.get(key))
        return


# We start by creating a regular redis connection
connection = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('irida', connection)



