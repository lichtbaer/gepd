import pandas
import requests
#import json

class gepd:
    def __init__(self):
        self.api = "https://api.dawum.de/"

        self.refresh_data()

    def refresh_data(self):
        headers = {
            'Cache-Control': "no-cache",
        }
        try:
            self.json = requests.request("GET", self.api,
                                             headers=headers).json()
        except ConnectionError:
            return "No Connection"

    def get_data_license(self):
        return self.json["Database"]

    def get_parliaments(self):
        return self.json["Parliaments"]

    def get_institutes(self):
        return self.json["Institutes"]

    def get_taskers(self):
        return self.json["Taskers"]

    def get_parties(self):
        return self.json["Parties"]

    def get_surveys_raw(self):
        return self.json["Surveys"]

    def get_surveys(self,):
        df = pandas.DataFrame(self.json["Surveys"])
        return df


if __name__ == "__main__":
    data = gepd()
    print(data.get_surveys())

