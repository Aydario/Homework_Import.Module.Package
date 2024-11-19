from application.salary import *
from application.db.people import *
from datetime import *


def main():
    get_employees()
    calculate_salary()
    today = date.today()
    print(today.strftime('Today: %A, %d %B %Y')) 

if __name__ == '__main__':
    main()
