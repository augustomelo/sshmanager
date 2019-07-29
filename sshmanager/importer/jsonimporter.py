from .baseimporter import BaseImporter


class JsonImporter(BaseImporter):
    def loads(self, data={}):
        """
        Desserialize a JSON into a list of machines.

        :param data:
            A object serialized in the JSON format

        :ret:
            A List of machines.
        """
        pass

    def load(self, fp=None):
        """
        Desserialize a fp into a list of machines.

        :param data:
            A .read()-supporting file-like object containing a JSON document.

        :ret:
            A list of machines.
        """
        pass
