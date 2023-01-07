from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = 1e6
        max_salary = 0
        total = 0
        for salary_item in salary:
            total += salary_item
            if salary_item > max_salary:
                max_salary = salary_item
            if salary_item < min_salary:
                min_salary = salary_item
        
        n = len(salary) - 2
        return (total - max_salary - min_salary) / n
            