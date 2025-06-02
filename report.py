from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Employee:
    department: str
    hours_worked: int
    hourly_rate: float


class Report:
    registry = {}

    def __init_subclass__(cls, name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry[name] = cls

    @classmethod
    def run(cls, data: List[Employee]) -> None:
        raise NotImplementedError


class PayoutReport(Report, name="payout"):
    @classmethod
    def run(cls, data: List[Employee]) -> None:
        total_by_dept = {}
        for emp in data:
            total = emp.hours_worked * emp.hourly_rate
            total_by_dept[emp.department] = total_by_dept.get(emp.department, 0) + total
        print("=== Отчёт по выплатам ===")
        for dept, amount in sorted(total_by_dept.items()):
            print(f"{dept}: {amount:.2f}")


class AverageRateReport(Report, name="average_rate"):
    @classmethod
    def run(cls, data: List[Employee]) -> None:
        from collections import defaultdict
        totals = defaultdict(list)
        for emp in data:
            totals[emp.department].append(emp.hourly_rate)
        print("=== Средняя ставка по отделам ===")
        for dept, rates in totals.items():
            avg = sum(rates) / len(rates)
            print(f"{dept}: {avg:.2f}")
