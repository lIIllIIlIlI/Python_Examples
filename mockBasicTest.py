import pytest
import mock
from pytest_mock import mocker
import myModule
import math

def test_calculateSquareRoot(monkeypatch):
    def mockreturn(a):
        return 0.0
    monkeypatch.setattr(math, "sqrt", mockreturn)
    variable = 4.0
    assert myModule.calculateSquareRoot(variable) == 0

