from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ModelName(str, Enum):
    """
    Enum de Modelos de DL
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Pokemon(BaseModel):
    nombre: str
    tipo: str
    atk: int
    spd: int
    hp: int
    sex: Optional[str] = None
