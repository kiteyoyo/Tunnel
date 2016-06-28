print("What day is today?");

#import datetime,time
#now = time.strftime("%A")
#print now ;

print("Input date!")
year = input(">> Year: ");
month = input(">> Month: ");
date = input(">> Date: ");

def get_y(y):
    y = year - 2000;
    return y ;
def get_l(year):
    l = (year - 2000)/4 + 1
    return l ;
def get_m(month):
    if month == 1 or month == 10:
        m = 5;
        return m ;
    elif month == 2 or month == 3 or month == 11:
        m = 1;
        return m ;
    elif month == 4 or month == 7:
        m = 4;
        return m ;
    elif month == 5:
        m = 6;
        return m ;
    elif month == 6:
        m = 2;
        return m ;
    elif month == 8:
        m = 0;
        return m ;
    else :
        m = 3;
        return m ;

y = get_y(year);
l = get_l(year);
m = get_m(month);
d = date ;
w = (y + l + m + d )%7;
print w ;

