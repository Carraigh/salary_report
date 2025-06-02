import argparse
import os
from reader import read_employee_data
from report import Report


def main():
    parser = argparse.ArgumentParser(description="Генерация отчётов по данным сотрудников")
    parser.add_argument("files", nargs="+", help="Пути к CSV файлам с данными сотрудников")
    parser.add_argument("--report", required=True, choices=Report.registry.keys(),
                        help="Тип отчёта")

    args = parser.parse_args()

    # Проверка: файлы существуют?
    for file in args.files:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"Файл не найден: {file}")

    employees = []
    for file in args.files:
        try:
            employees.extend(read_employee_data(file))
        except Exception as e:
            raise RuntimeError(f"Ошибка при чтении файла '{file}': {e}") from e

    try:
        Report.run(args.report, employees)
    except ValueError as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()

    import sys
    import os

    # Тест: файлы существуют
    for file in sys.argv[1:-2]:
        assert os.path.isfile(file), f"Файл не найден: {file}"

    # Тест: минимальный запуск
    try:
        main()
        print("[OK] Скрипт успешно завершил работу")
    except Exception as e:
        print(f"[ERROR] Ошибка при выполнении: {e}")
