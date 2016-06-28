function t=time_axis(d)
mon=str2num(d(6:7));
day=str2num(d(9:10));
hour=str2num(d(12:13));
min=str2num(d(15:16));
t=datenum(2015, mon, day, hour, min, 0);