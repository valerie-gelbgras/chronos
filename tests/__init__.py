import sys


import src.chronos.chronos_app
import src.chronos.time_interval


sys.modules['chronos_app'] = sys.modules['src.chronos.chronos_app']
sys.modules['time_interval'] = sys.modules['src.chronos.time_interval']
