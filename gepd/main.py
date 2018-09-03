import pandas
import requests
import json


import pprint

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

    def get_surveys(self, limit=0, tasker=[], institute=[]):
        df = pandas.DataFrame(self.json["Surveys"]).T
        df.Date = pandas.to_datetime(df.Date)
        df.Institute_ID = pandas.to_numeric(df.Institute_ID)
        df.Tasker_ID = pandas.to_numeric(df.Tasker_ID)
        df.Surveyed_Persons = pandas.to_numeric(df.Surveyed_Persons)
        results = []
        survey = []

        for i in df.Results:

            results.append(i)
        print(results)
        df_res = pandas.DataFrame(results)
        print(df.combine_first(df_res))
        #df["0"]= df_res[0]
        #df["1"] = df_res[1]
        #df["2"] = df_res[2]
        #print(df_res)

        for i in df.Survey_Period:
            survey.append(i)
        df_survey = pandas.DataFrame(survey)



        if [] != institute:
            df = df.loc[df["Institute_ID"].isin(institute)]

        if [] != tasker:
            df = df.loc[df.Tasker_ID.isin(tasker)]

        if limit > 0:
            df = df.head(limit)

        return df



if __name__ == "__main__":
    data = gepd()
    #print(data.get_parties())
    data.get_surveys(limit=0)


