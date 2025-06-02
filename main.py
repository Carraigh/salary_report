import argparse
from reader import read_employee_data
from report import generate_report


def main():
    parser = argparse.ArgumentParser(description="Генерация отчётов по данным сотрудников")
    parser.add_argument("files", nargs="+", help="Пути к CSV файлам с данными сотрудников")
    parser.add_argument("--report", required=True, choices=["payout"], help="Тип отчёта")

    args = parser.parse_args()

    employees = []
    for file in args.files:
        employees.extend(read_employee_data(file))

    generate_report(args.report, employees)


if __name__ == "__main__":
    main()
