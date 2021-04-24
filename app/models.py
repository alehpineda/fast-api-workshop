from enum import Enum


class ModelName(str, Enum):
    """
    Enum de Modelos de DL
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Items:
    item_name: str
    item_description: str
    price: int
