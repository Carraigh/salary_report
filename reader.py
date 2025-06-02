from typing import List, Dict, Any
from pathlib import Path


def read_employee_data(filepath: str) -> List[Dict[str, Any]]:
    employees = []

    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
        headers = lines[0].split(",")
        index_map = {h.lower(): i for i, h in enumerate(headers)}

        hourly_rate_index = None
        for col_name in ["hourly_rate", "rate", "salary"]:
            if col_name in index_map:
                hourly_rate_index = index_map[col_name]
                break

        if hourly_rate_index is None:
            raise ValueError(f"Не найдена колонка для ставки в файле: {filepath}")

        try:
            hours_worked_index = index_map["hours_worked"]
            department_index = index_map["department"]
        except KeyError as e:
            raise ValueError(f"Отсутствует необходимая колонка в файле: {filepath}") from e

        for line in lines[1:]:
            if not line:
                continue
            values = line.split(",")
            try:
                employee = {
                    "department": values[department_index],
                    "hours_worked": int(values[hours_worked_index]),
                    "hourly_rate": float(values[hourly_rate_index]),
                }
            except (ValueError, IndexError) as e:
                raise ValueError(f"Ошибка при обработке строки в файле {filepath}: {line}") from e

            employees.append(employee)

    return employees
