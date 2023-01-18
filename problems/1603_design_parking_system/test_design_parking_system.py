import pytest
from design_parking_system import ParkingSystem


def test_parking_system_one():
    ps = ParkingSystem(1, 1, 0)
    assert ps.addCar(1) is True
    assert ps.addCar(2) is True
    assert ps.addCar(3) is False
    assert ps.addCar(1) is False


def test_parking_system_two():
    ps = ParkingSystem(0, 0, 0)
    assert ps.addCar(1) is False
    assert ps.addCar(2) is False
    assert ps.addCar(3) is False
    assert ps.addCar(1) is False