from abc import ABC
from abc import abstractmethod


class BaseImporter(ABC):
    """
    Base importer.

    The intent of this class is to define the base methods of all importers.
    """

    @abstractmethod
    def loads(self, data={}):
        """
        Desserialize the data accordingly if its concrete class into a machine
            object.

        :param data:
            A object serialized in the concrete class format.

        :ret:
            A list of machines.
        """
        pass

    @abstractmethod
    def load(self, fp=None):
        """
        Desserialize a fp into a list of machines.

        :param data:
            A .read()-supporting file-like object containing a concrete class format document.

        :ret:
            A list of machines.
        """
        pass
