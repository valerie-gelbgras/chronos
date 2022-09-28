import sys

import src.chronos.chronos_app
import src.chronos.validation

sys.modules['chronos_app'] = sys.modules['src.chronos.chronos_app']
sys.modules['validation'] = sys.modules['src.chronos.validation']