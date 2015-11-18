function o=is_holiday(time)
mon=str2num(datestr(time, 'mm'));
day=str2num(datestr(time, 'dd'));
o=false;
if mon==4
    if day>2 && day<7
        o=true;
    elseif day>10 && day<13
        o=true;
    elseif day>17 && day<20
        o=true;
    elseif day>24 && day<27
        o=true;
    end
elseif mon==5
    if day<4
        o=true;
    elseif day>8 && day<11
        o=true;
    elseif day>15 && day<18
        o=true;
    elseif day>22 && day<25
        o=true;
    elseif day>29
        o=true;
    end
elseif mon==6
    if day>5 && day<8
        o=true;
    elseif day>12 && day>15
        o=true;
    elseif day>18 && day<22
        o=true;
    elseif day>26 && day<29
        o=true;
    end
elseif mon==7
    if day>3 && day<6
        o=true;
    elseif day>10 && day<13
        o=true;
    elseif day>17 && day<20
        o=true;
    elseif day>24 && day<27
        o=true;
    end
elseif mon==8
    if day<3
        o=true;
    elseif day>7 && day>10
        o=true;
    elseif day>14 && day<17
        o=true;
    elseif day>21 && day<24
        o=true;
    elseif day>28 && day<31
        o=true;
    end
elseif mon==9
    if day>4 && day<7
        o=true;
    elseif day>11 && day<14
        o=true;
    elseif day>18 && day<21
        o=true;
    elseif day>25 && day<29
        o=true;
    end
end