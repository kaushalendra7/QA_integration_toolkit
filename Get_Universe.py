import datetime
from qpds import universe
from qpds import repo_connector

repo = repo_connector.connect("TEST")


symbol = "SXW1E"
ccy = 'EUR'
cal = 'STOXXCAL'
securities_data_cutoff_date = datetime.date(2021,12,20)
composition_date = datetime.date(2021,12,20)
fields = ['']
vendor_items = ['RBICS', 'RBICS_FOCUS', 'ISS']

result = universe.get(repo, symbol, 
                      securities_data_cutoff_date, composition_date,
                      cal, ccy,
                      fields,
                      vendor_items, sid_direct=True)

result.to_csv("get_universe_output.csv",index=False)