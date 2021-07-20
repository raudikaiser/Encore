#!/usr/bin/env python3

from statistics import mean

temps_in = [30, 60, 90, 120]

class TempTracker:
    def __init__(self):
        self.temps = []
        self.max_temp = 0
        self.min_temp = 0
        self.mean_temp = 0
        self.num_days = 0

    def insert(self, new_temp):
        self.temps.append(new_temp)
        return len(self.temps)

    def get_max(self):
        return max(self.temps)

    def get_min(self):
        return min(self.temps)

    def get_mean(self):
        return float(mean(self.temps))


if __name__ == '__main__':
    weather = TempTracker()
    for temp in temps_in:
        weather.insert(temp)
    my_days = weather.insert(110)
    my_mean = weather.get_mean()
    my_min  = weather.get_min()
    my_max  = weather.get_max()

    print('The minimum temperature was {} degrees Fahrenheit'.format(my_min))
    print('The maximum temperature was {} degrees Fahrenheit'.format(my_max))
    print('The mean temperature over {} days was {} degrees Fahrenheit'.format(my_days, my_mean))