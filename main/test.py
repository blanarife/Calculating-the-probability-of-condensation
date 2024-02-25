from check import temps
from check import ud
try:
    result = temps(30)  
    print(result)
except ValueError as e:
    print(e)    

