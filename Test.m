str = '2015-04-01T00:00:00+08:00';
ans = isstrprop(str,'digit')
long = length(str)
getnum = []
for i = 1:long
    if ans(i) == 1
        getnum = [getnum,str(i)]
    end
end