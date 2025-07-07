import re

def generator_number(text):
    pattern=r'\s\d+\.\d+\s' 
    list_digits=re.findall(pattern,text)
    for digit in list_digits:
        yield float(digit)
        
        
def sum_profit(text,generator_number):
    sum=0
    print(list(generator_number(text)))
    for i in generator_number(text):
        sum=sum+i
    return sum


