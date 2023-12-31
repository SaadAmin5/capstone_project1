# Task 5: Capstone project 

import math

print('''investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan''')

calculator_type= input('Enter either investment or bond from the menu above to proceed: ').lower()


if calculator_type!='bond' and calculator_type!='investment':
    print('Please enter a valid input')
   

if calculator_type=='investment':
    
    money_deposited=float(input('The amount of money you are despositing: '))
    
    interest_rate= float(input('Enter interest rate: '))/100
    
    years= int(input('Number of years you plan on investing: '))
    
    interest= input('Do you need simple or compound interest? ').lower()
    
    
    if interest=='simple':
        
        r= float(input('Interest rate: '))/100
        p= float(input('Amount deposited by user: '))
        t= int(input('Number of years that the money is being invested: '))
        
        A = p *(1 + r*t)
        
        print('The total amount once the interest has been applied: ', A)
    
    elif interest=='compound':
        
        r= float(input('Interest rate: '))/100
        p= float(input('Amount deposited by user: '))
        t= int(input('Number of years that the money is being invested: '))
        
        A = p * math.pow((1+r),t)
        
        print('The total amount once the interest has been applied: ', A)
        
    else:
        
        pass
        
        
elif calculator_type=='bond':
    
    house_value=int(input('Present value of house: '))
    
    interest_rate=float(input('Enter interest rate: '))/100
    
    no_of_months=int(input('The number of months you plan to take to repay the bond: '))
    
    repayment = (interest_rate * house_value)/(1 - (1 + (interest_rate/12))**(-no_of_months))
    
    print('Money that the user will have to repay each month will be: ', repayment)
    

else:
    
    pass
