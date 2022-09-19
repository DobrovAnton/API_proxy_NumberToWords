from pydantic import BaseModel


class NumberRequest(BaseModel):
    ubiNum: int  # positive, limited to quadrillions

