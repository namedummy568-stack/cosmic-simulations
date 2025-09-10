import pytest
from cosmo_model import calculate_omega_m, calculate_hubble_parameter

def test_calculate_omega_m():
    assert calculate_omega_m(0.05, 0.25) == pytest.approx(0.30)

def test_calculate_hubble_parameter():
    assert calculate_hubble_parameter(70, 0.5) == pytest.approx(105)