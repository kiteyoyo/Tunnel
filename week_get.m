function P=week_get(A, month, number, method)
P = [];
if method==1 %Fri-Sun
    if month==4 
        sl=[1301, 2985, 4959];
        el=[2146, 3829, 5802];
    elseif month==5
        sl=[2, 1976, 3670, 5636, 7613];
        el=[852, 2827, 4510, 6480, 8457];
    elseif month==6
        sl=[1129, 3107, 4189, 6030];
        el=[1981, 3639, 4908, 6868];
    end
elseif method==2 %Sat-Sun
    if month==4
        sl=[1583, 3264, 5242];
        el=[2146, 3829, 5802];
    elseif month==5
        sl=[288, 2262, 3949, 5918, 7894];
        el=[852, 2827, 4510, 6480, 8457];
    elseif month==6
        sl=[1411, 3389, 4471, 6311];
        el=[1981, 3639, 4908, 6868];
    end
O=A(:,sl(number):el(number));
end
