import redis
from abc import ABCMeta, abstractmethod
from redisgraph import Node, Edge, Graph


# -----------------------------------------------------------------------------
# CLASS GRAPH ENTITY
# -----------------------------------------------------------------------------
class GraphStructure(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def _collect_entity_properties(self):
        return (attribute for attribute in dir(self) if not attribute.startswith("_"))

    @property
    def label(self) -> str:
        return self.__class__.__name__

    @property
    def as_node(self):
        node = Node(
            label=self.label
        )
        return node




# We start by creating a regular redis connection
connection = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('irida', connection)



