import pytest
import tempfile
import os
from reader import read_employee_data
from report import generate_payout_report


@pytest.fixture
def create_csv(tmp_path):
    def _create_csv(content):
        path = tmp_path / "data.csv"
        with open(path, "w") as f:
            f.write(content)
        return str(path)
    return _create_csv


def test_read_employee_data(create_csv):
    content = """id,name,department,hours_worked,rate
1,Alice,IT,160,50
2,Bob,IT,150,40"""
    path = create_csv(content)
    employees = read_employee_data(path)
    assert len(employees) == 2
    assert employees[0]["department"] == "IT"
    assert employees[0]["hours_worked"] == 160
    assert employees[0]["hourly_rate"] == 50


def test_generate_payout_report(capsys):
    employees = [
        {"department": "IT", "hours_worked": 160, "hourly_rate": 50},
        {"department": "IT", "hours_worked": 150, "hourly_rate": 40},
        {"department": "HR", "hours_worked": 170, "hourly_rate": 30},
    ]
    generate_payout_report(employees)
    captured = capsys.readouterr()
    assert "IT: 14000.0" in captured.out
    assert "HR: 5100.0" in captured.out


def test_reader_with_different_column_names(create_csv):
    content = """id,name,department,hours_worked,salary
1,Alice,Marketing,160,50
2,Bob,Design,150,40"""
    path = create_csv(content)
    employees = read_employee_data(path)
    assert employees[0]["hourly_rate"] == 50
