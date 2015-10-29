function A=load_month(mon, is_N, method)
month=[31 28 31 30 31 30 31 31 30 31 30 31];
A=[];
for i=1:month(mon)
    if method==1 || method==2
        A=[A load_dir(path_auto(mon, i, 1), is_N, method)];
    elseif method==3
        A=[A GetRain(path_auto(mon, i, 2)', '石碇')];
    elseif method==4
        A=[A GetRain(path_auto(mon, i, 2)', '坪林')];
    elseif method==5
        A=[A GetRain(path_auto(mon, i, 2)', '碧湖')];
    elseif method==6
        A=[A GetRain(path_auto(mon, i, 2)', '舊莊')];
    end
end