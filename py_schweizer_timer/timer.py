import datetime

class SchweizerTimer:
    def __init__(self):
        self.__start_time = 0
        self.__end_time = 0
        self.duration = 0

    def __str__(self):
        pass

    def set_start_time(self):
        self.__start_time = datetime.datetime.now()

    def set_end_time(self):
        self.__end_time = datetime.datetime.now()

    def show_duration(self):
        self.duration = (self.__end_time - self.__start_time).seconds

    def show_duration_detail(self):
        hour = (self.__end_time - self.__start_time).seconds / 3600
        minute = ((self.__end_time - self.__start_time).seconds - 3600 * hour) / 60
        second = ((self.__end_time - self.__start_time).seconds - 3600 * hour - 60 * minute)
        print "the process cost %s hours , %s minutes , %s seconds" % (hour, minute, second)

