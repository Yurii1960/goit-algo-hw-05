import re

text= "dfdfdfd 333.33 fhfhfh []/.,n 90.09 "
def generator_number(text):
    pattern=r'\s\d+\.\d+\s' 
    list_digits=re.findall(pattern,text)
    
    for digit in list_digits:
        
        yield float(digit)
    #def sum_profit():
        #sum=0
gen=generator_number(text)        #sum=sum+
print(next(gen))
print(next(gen))
def sum_profit(text,generator_number):
    sum=0
    print(list(generator_number(text)))
    for i in generator_number(text):
        sum=sum+i
        print(i)
    print(sum)
    return sum
sum_profit(text,generator_number)

