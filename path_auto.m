function path=path_auto(m, d,method)

p=strcat(num2str(m), '_');
p=strcat(p, num2str(d));
p=strcat(p, '/');
if method==1
    path=strcat('/home/mcl/math/traffic/2015_', p);
else
    path=strcat('/home/mcl/math/Weather/2015_', p);
end