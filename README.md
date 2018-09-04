# gepd
German election poll data

Uses Data From https://api.dawum.de/
requirements:
pandas,
requests


pip install -r requirements.txt git+https://github.com/lichtbaer/gepd.git

import gepd

data = gepd.gepd()

sure = data.get_surveys()

filter surveys:

limit: requires integer, outputs the latest x elements, runs as the last filter

tasker: requires a list of integers from the Tasker list

institute: requires a list of integers from the Institute list

min_survey: minimum number of participants in the survey

max_survey: maximum number of participants in the survey

return_df: By default a dataframe is returned if false then a dict is returned

sure = data.get_surveys(limit=5, min_survey=100, max_survey= 3000, tasker=[1,2,3], institute=[1,3,5] )

#TODO
Tests implementieren,
mehr Filter implementieren
