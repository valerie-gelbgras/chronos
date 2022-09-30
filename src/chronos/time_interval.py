# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from src.chronos import validation


class TimeInterval:
    def __init__(self, *, hours, minutes, seconds, milliseconds): 
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
    
    @staticmethod
    @validation.class_property(int.__name__)
    def from_milliseconds(total_time_in_milliseconds):
        (total_hours, total_time_in_milliseconds) = divmod(total_time_in_milliseconds, 3600000)
        (total_minutes, total_time_in_milliseconds) = divmod(total_time_in_milliseconds, 60000)
        (total_seconds, total_time_in_milliseconds) = divmod(total_time_in_milliseconds, 1000)
        return TimeInterval(hours=total_hours, minutes=total_minutes, seconds=total_seconds, milliseconds=total_time_in_milliseconds)
    
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    @validation.class_property(int.__name__)
    def hours(self, value):
        self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    @validation.class_property(int.__name__)
    def minutes(self, value):
        self.__minutes = value
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    @validation.class_property(int.__name__)
    def seconds(self, value: int) -> None:
        self.__seconds = value
    
    @property
    def milliseconds(self):
        return self.__milliseconds
    
    @milliseconds.setter
    @validation.class_property(int.__name__)
    def milliseconds(self, value: int) -> None:
        self.__milliseconds = value
    
    @validation.class_property(int.__name__, 'TimeInterval')
    def __add__(self, time):        
        time_interval = TimeInterval.from_milliseconds(time) if isinstance(time, int) else time
        
        total_time = self.to_milliseconds() + time_interval.to_milliseconds()
        return TimeInterval.from_milliseconds(total_time)
    
    @validation.class_property(int.__name__, 'TimeInterval')
    def __sub__(self, time):       
        time_interval = TimeInterval.from_milliseconds(time) if isinstance(time, int) else time
        
        total_time = self.to_milliseconds() - time_interval.to_milliseconds()          
        return TimeInterval.from_milliseconds(total_time)
    
    def to_milliseconds(self):
        return self.hours * 3600000 + self.minutes * 60000 + self.seconds * 1000 + self.milliseconds
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}.{self.milliseconds:03d}"
