import tempfile
import os
from reader import read_employee_data


def test_read_employee_data():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmpfile:
        tmpfile.write("""id,name,department,hours_worked,rate
1,Alice,IT,160,50
2,Bob,IT,150,40""")
        tmpfile_path = tmpfile.name

    employees = read_employee_data(tmpfile_path)
    assert len(employees) == 2
    assert employees[0]["department"] == "IT"
    assert employees[0]["hours_worked"] == 160
    assert employees[0]["hourly_rate"] == 50
    os.unlink(tmpfile_path)


def test_reader_with_different_column_names():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmpfile:
        tmpfile.write("""id,name,department,hours_worked,salary
1,Alice,Marketing,160,50
2,Bob,Design,150,40""")
        tmpfile_path = tmpfile.name

    employees = read_employee_data(tmpfile_path)
    assert employees[0]["hourly_rate"] == 50
    os.unlink(tmpfile_path)


# Запуск тестов
if __name__ == "__main__":
    test_read_employee_data()
    test_reader_with_different_column_names()
    print("[✅] Все тесты пройдены!")
