from enum import Enum

class Period(Enum):
    ANNUAL = "Annual"
    QUARTERLY = "Quarterly"
    
    def __str__(self):
        return self.value