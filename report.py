def generate_report(report_type, employees):
    if report_type == "payout":
        generate_payout_report(employees)
    else:
        print(f"Неизвестный тип отчёта: {report_type}")


def generate_payout_report(employees):
    department_totals = {}

    for emp in employees:
        dept = emp["department"]
        total = emp["hours_worked"] * emp["hourly_rate"]
        department_totals[dept] = department_totals.get(dept, 0) + total

    print("=== Отчёт по выплатам ===")
    for dept, total in sorted(department_totals.items()):
        print(f"{dept}: {total}")
