from sys import path
path.append('../src')

from route import Route

route_test = Route(14121, 777, 14)
assert route_test.first_train == 14121
assert route_test.second_train == 777
assert route_test.total_time == 14
