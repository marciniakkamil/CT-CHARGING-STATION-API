"""Enums used in the project"""
from enum import Enum


# Charging Station Type
class ChargingStationCurrentTypesEnum(str, Enum):
    AC = "AC"
    DC = "DC"
