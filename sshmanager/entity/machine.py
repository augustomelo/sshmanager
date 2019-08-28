from .user import User
from .protocol import Protocol


class Machine():
    def __init__(self, host='', name='', user={}, protocol='', tags=[]):
        self.host = host
        self.name = name
        self.user = User(**user)
        self.protocol = Protocol[protocol.upper()]
        self.tags = tags

    def __str__(self):
        return (f'Machine[host: {self.host}, '
                f'name: {self.name}, user: {self.user} '
                f'protocol: {self.protocol}, tags: {self.tags}]')
