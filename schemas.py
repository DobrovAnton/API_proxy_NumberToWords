from pydantic import BaseModel
from fastapi import HTTPException


class NumberRequest(BaseModel):
    ubiNum: int  # positive, limited to quadrillions


class ParserException(Exception):
    def __init__(self, xml: str):
        self.xml = xml
