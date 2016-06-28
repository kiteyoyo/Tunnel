function path=path_auto(m, d)
p=strcat('/home/mcl/math/traffic/2015_', num2str(m));
p=strcat(p, '_');
p=strcat(p, num2str(d));
path=strcat(p, '/');