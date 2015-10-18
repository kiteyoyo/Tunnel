function A=load_month(mon, is_N, method)
month=[31 28 31 30 31 30 31 31 30 31 30 31];
A=[];
for i=1:month(mon)
    A=[A load_dir(path_auto(i, 5), is_N, method)];
end