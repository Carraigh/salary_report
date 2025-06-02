def read_employee_data(filepath):
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

        hours_worked_index = index_map["hours_worked"]
        department_index = index_map["department"]
        name_index = index_map["name"]

        for line in lines[1:]:
            if not line:
                continue
            values = line.split(",")
            employee = {
                "name": values[name_index],
                "department": values[department_index],
                "hours_worked": int(values[hours_worked_index]),
                "hourly_rate": float(values[hourly_rate_index]),
            }
            employees.append(employee)

    return employees
