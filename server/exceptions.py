from typing import Optional

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message: str, status_code: Optional[int] = None, payload: Optional[dict] = None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> dict:
        res = dict(self.payload or ())
        res['message'] = self.message
        return res
