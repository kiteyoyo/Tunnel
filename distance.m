function d=distance(s)
b=findstr(s, '-');
c=b(end)+1;
d=str2num(s(c:end));