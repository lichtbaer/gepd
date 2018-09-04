import pandas
import requests

class gepd:
    """
    """
    def __init__(self):
        """

        """
        self.api = "https://api.dawum.de/"

        self.refresh_data()

    def refresh_data(self):
        """

        Returns:

        """
        headers = {
            'Cache-Control': "no-cache",
        }
        try:
            self.json = requests.request("GET", self.api,
                                             headers=headers).json()
        except ConnectionError:
            return "No Connection"

        json = self.json["Surveys"]
        l = []

        for i in json.values():
            i.update(i['Survey_Period'])
            i.pop('Survey_Period', None)
            i.update(i['Results'])
            i.pop('Results', None)
            l.append(i)

        self.df = pandas.DataFrame(l)
        self.df.Date = pandas.to_datetime(self.df.Date)
        self.df.Institute_ID = pandas.to_numeric(self.df.Institute_ID)
        self.df.Tasker_ID = pandas.to_numeric(self.df.Tasker_ID)
        self.df.Surveyed_Persons = pandas.to_numeric(self.df.Surveyed_Persons)

    def get_data_license(self):
        """

        Returns: a dict of Data license informations

        """
        return self.json["Database"]

    def get_parliaments(self):
        """

        Returns: a dict of parliaments

        """
        return self.json["Parliaments"]

    def get_institutes(self):
        """

        Returns: a dict of institutes

        """
        return self.json["Institutes"]

    def get_taskers(self):
        """

        Returns: a dict of taskers

        """
        return self.json["Taskers"]

    def get_parties(self):
        """

        Returns: a dict of parties

        """
        return self.json["Parties"]

    def get_surveys_raw(self):
        """

        Returns: a dict of surveys

        """
        return self.json["Surveys"]

    def get_surveys(self,
                    limit=0,
                    tasker=[],
                    institute=[],
                    min_survey=0,
                    max_survey=0,
                    return_df=True):
        """

        Args:
            limit: requires integer, outputs the latest x elements, runs as the
             last filter
            tasker: requires a list of integers from the Tasker list
            institute: requires a list of integers from the Institute list
            min_survey: minimum number of participants in the survey
            max_survey: maximum number of participants in the survey
            return_df: By default a dataframe is returned if false then a dict
            is returned

        Returns: returns a data frame with the polls. Numbered lines correspond
        to their parties

        """


        df = self.df
        #TODO Implement tests
        if [] != institute:
            df = df.loc[df["Institute_ID"].isin(institute)]

        if [] != tasker:
            df = df.loc[df.Tasker_ID.isin(tasker)]


        if min_survey != 0:
            df = df[df.Surveyed_Persons > min_survey]

        if max_survey != 0:
            df = df[df.Surveyed_Persons < max_survey]

        if limit > 0:
            df = df.head(limit)

        if return_df == False:
            df = df.to_dict()

        return df



if __name__ == "__main__":
    data = gepd()
    print(data.get_surveys(limit=0, min_survey=1500))


