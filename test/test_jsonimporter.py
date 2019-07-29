import unittest

from sshmanager.importer.jsonimporter import JsonImporter


class TestJsonImporter(unittest.TestCase):
    def test_parse(self):
        data = {
            "all": { 
                "tomcat": [
                    "tc-01",
                    "tc-02",
                ],
                "php": [
                    "nginx-01",
                    "nginx-02",
                ]
            }
        }

        # importer = JsonImporter()
        # print(importer.parse(data=data))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()