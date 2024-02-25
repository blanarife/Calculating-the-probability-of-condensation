from getdata import getdata
from check import temps
from check import ud

def create():

    with open('exemplu.bif', 'w') as file:
        file.write('network "ModelH" {\n}\n\n')
        data=getdata()
        a=data[0]
        b=data[1]

    
        try:
            x = temps(a)
            print(x)
        except ValueError as e:
            print(e)    
        y=ud(b)
        print(y)


        file.write('variable "T" {\n')
        file.write('    type discrete [ 3 ] { TH, TM, TL };\n')
        file.write('}\n\n')

        file.write('variable "H" {\n')
        file.write('    type discrete [ 3 ] { HH, HM, HL };\n')
        file.write('}\n\n')

        file.write('variable "C" {\n')
        file.write('    type discrete [ 2 ] { T, F };\n')
        file.write('}\n\n')

        file.write('probability (T) {\n')
        file.write(f'    table {x[0]}, {x[1]}, {x[2]};\n')  
        file.write('}\n\n')

        file.write('probability (H) {\n')
        file.write(f'    table {y[0]}, {y[1]}, {y[2]};\n')
        file.write('}\n\n')

        file.write('probability (C | T, H) {\n')
        file.write('    (TH, HH) 0.9, 0.1;\n')
        file.write('    (TH, HM) 0.5, 0.5;\n')
        file.write('    (TH, HL) 0.3, 0.7;\n')
        file.write('    (TM, HH) 0.7, 0.3;\n')
        file.write('    (TM, HM) 0.4, 0.6;\n')
        file.write('    (TM, HL) 0.2, 0.8;\n')
        file.write('    (TL, HH) 0.5, 0.5;\n')
        file.write('    (TL, HM) 0.3, 0.7;\n')
        file.write('    (TL, HL) 0.1, 0.9;\n')
        file.write('}\n')

create()