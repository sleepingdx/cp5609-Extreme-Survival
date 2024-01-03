import json


class Json:
    """Execute json files"""

    def __init__(self):
        self.m_json = None

    def load_json(self, filename, mode):
        """
        Load json information through json file
        :param filename: filename of json file
        :param mode: r-read only; w-write； a-append; b-binary; r+, w+....
        :return: json data
        """
        with open(filename, mode) as filename:
            self.m_json = json.load(filename)
        return self.m_json

    def load_json_string(self, json_string):
        """
        Load json information through json string
        :param json_string:
        :return: json data
        """
        self.m_json = json.loads(json_string)
        return self.m_json
