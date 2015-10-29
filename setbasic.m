function getdata = setbasic(data)
%SETTIME Summary of this function goes here
%   Detailed explanation goes here
data_arrey = [0 0 0];
input = data;
long = size(input);
getnum = [];
for i = 1:long(2)
    if strcmp(input(i).Name,'time')
        t = input(i).Children(2).Children.Data;
        getdig = isstrprop(t,'digit');
        long = length(t);
        for i = 1:long
            if getdig(i) == 1
                getnum = [getnum,t(i)];
            end
        end
        data_arrey(1) = str2num(getnum);
    elseif strcmp(input(i).Name,'lat')
        l = input(i).Children.Data;
        data_arrey(2) = str2num(l);
    elseif strcmp(input(i).Name,'lon')
        l = input(i).Children.Data;
        data_arrey(3) = str2num(l);       
    else
        if strcmp(input(i).Name,'weatherElement')
            break;
        end
    end        
end
getdata = data_arrey;
end

