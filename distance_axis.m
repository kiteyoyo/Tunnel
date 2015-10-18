function A=distance_axis(is_N)
R=read_json('/home/mcl/math/traffic/2015_4_1/201503312358.json');
A=[];
for r=R
    A=[A distance(r.vdid)];
end
if is_N
    A=A(79:end);
else
    A=A(1:78);
end