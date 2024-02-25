def temps(a):
    if(a > 60 or a < -40):
        raise ValueError("Temperature value is out of range [-40, 60]")

    if a <= 15:
        t3= 0.5 + (30-a)/100   
        t2= (1-t3)*2/3
        t1= (1-t3)*1/3

    elif a >=25:
        t1= 0.5 + (a-10)/100
        t2= (1-t1)*2/3
        t3= (1-t1)*1/3

    else:
        t2= 0.9 - abs(20-a)/10
        if  a==20:
            t1=(1-t2)/2
            t3=(1-t2)/2
        elif a>20:
            t1= (a-20) /10
            t3=1-t1-t2
        else:
            t3= (20-a) /10
            t1=1-t2-t3
        
    return t1,t2,t3

def ud(a):
    
    if a>=70:
        h1=a/100
        h2=(1-(a/100))*2/3
        h3=(1-(a/100))*1/3
    elif a<=30:
        h3=(100-a)/100
        h2=(1-((100-a)/100))*2/3
        h1=(1-((100-a)/100))*1/3
    else:
        h2=0.9-abs(50-a)/100
        if  a==50:
            h1=(1-h2)/2
            h3=(1-h2)/2
        elif a>50:
            h1= (a-50) /100
            h3=1-h1-h2
        else:
            h3= (50-a) /100
            h1=1-h2-h3

    return h1,h2,h3


