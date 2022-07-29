from typing import List

from pi_finder.colors import colors, BLACK

try:
    from abc import ABC, abstractmethod
except:
    from mp.abc import ABC, abstractmethod


class Display(ABC):
    def __init__(self):
        self.color = BLACK

    @abstractmethod
    def show_alert(self, level: int, alerts: List[str]):
        pass

    def __repr__(self):
        return 'a %s showing %s' % (type(self).__name__, colors[self.color])

