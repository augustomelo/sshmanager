import unittest
import json

from sshmanager.entity.machine import Machine
from sshmanager.entity.protocol import Protocol
from sshmanager.importer.jsonimporter import JsonImporter


class TestJsonImporter(unittest.TestCase):
    def test_parse(self):
        data = [
            {
                'host': 'foo.host.com',
                'name': 'foo',
                'user': {
                    'name': 'foouser',
                    'password': 'foopw'
                },
                'protocol': 'ssh2',
                'tags': [
                    'host1',
                    'host2',
                ]
            },
            {
                'host': 'bar.host.com',
                'name': 'bar',
                'user': {
                    'name': 'baruser',
                    'password': 'barpw'
                },
                'protocol': 'ssh2',
                'tags': [
                ]
            }
        ]

        importer = JsonImporter()
        ret = importer.loads(json.dumps(data))

        self.assertIsInstance(ret, list)
        self.assertIsInstance(ret[0], Machine)
        self.assertEqual(len(ret), 2)
        self.assertEqual(ret[0].host, 'foo.host.com')
        self.assertEqual(ret[0].tags[1], 'host2')
        self.assertEqual(ret[1].name, 'bar')
        self.assertEqual(ret[1].protocol, Protocol.SSH2)


if __name__ == '__main__':
    unittest.main()
