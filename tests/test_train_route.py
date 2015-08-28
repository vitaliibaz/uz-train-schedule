from sys import path
path.append('../src')

from train_route import TrainRoute

instance = TrainRoute("Vil'no", '23:19', '09:29', '49', "VIL'NO PARMA", '5/09-3/10/2015 DAILY (EXCEPT 6,7,8,9,10,11/09/2015)')
assert instance.departure_station == "Vil'no"
assert instance.departure_time == '23:19'
assert instance.arrival_time == '09:29'
assert instance.number_train == '49'
assert instance.route == "Vil'no Parma"
assert instance.periodicity == '5/09-3/10/2015 daily (except 6,7,8,9,10,11/09/2015)'
