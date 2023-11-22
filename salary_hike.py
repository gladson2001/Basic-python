salary = int(input("Enter your salary: "))
experience = int(input("Enter your work experience:"))

if(experience>=5):
    bonus= int(salary*0.05)
    total_salary = (bonus+salary)*12
    print(f'Bonus= {bonus}' )
    print("Total salary= ",total_salary)
else:
    print("No bonus")