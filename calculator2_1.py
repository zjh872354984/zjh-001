import sys

def num_salary(salary):
    
    tax0 = salary - salary*16.5/100 -3500
    if tax0<=0:
        tax0=0
        tax=0
    elif tax0<=1500:
        tax = tax0 * 3/100 - 0
    elif tax0<=4500:
        tax = tax0 * 10/100 - 105
    elif tax0<=9000:
        tax = tax0 * 20/100 - 555
    elif tax0<=35000:
        tax = tax0 * 25/100 - 1005
    elif tax0<=55000:
        tax = tax0 * 30/100 - 2755
    elif tax0<=80000:
        tax = tax0 * 35/100 - 5505
    else:
        tax = tax0 * 45/100 - 13505
    income = salary - tax - salary*16.5/100
    return income

if __name__ == "__main__":
    dic_s = {}
    for arg in sys.argv[1:]:
        #print(arg.split(':'))
        arg_s = arg.split(':')
        dic_s.update({arg_s[0]:arg_s[1]})  
    print(dic_s)
    try:
        for key_n,value_s in dic_s.items():
            salary = int(value_s)
    except:
        print("Parameter Error") 

    for key_n,value_s in dic_s.items():
        salary = int(value_s)
        income = num_salary(salary)
        dic_s.update({key_n:income})
    for key_n,income in dic_s.items():
        print('{}:{:.2f}'.format(key_n, income))

