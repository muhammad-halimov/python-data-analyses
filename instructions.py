import pandas

fields = ['match_id', 'start_time', 'duration', 'first_blood_time', 'radiant_win']
result = pandas.read_csv('match.csv', skipinitialspace=True, usecols=fields)

result['start_time'] = pandas.to_datetime(result['start_time'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
result['duration'] = pandas.to_datetime(result['duration'], unit='s').dt.strftime('%M:%S')
result['first_blood_time'] = pandas.to_datetime(result['first_blood_time'], unit='s').dt.strftime('%M:%S')

result.to_csv('match_upd.csv', index=False)
