from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


def main():
    get_employees()
    calculate_salary()
    today = date.today()
    print(today.strftime('Today: %A, %d %B %Y')) 

if __name__ == '__main__':
    main()
    