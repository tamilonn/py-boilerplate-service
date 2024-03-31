from dataclasses import dataclass

@dataclass
class ErrorDetail:
    reason:str

    def __init__(self, reason):
        self.reason=reason