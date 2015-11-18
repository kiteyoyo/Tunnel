function [V N]=loadMon(year, mon)
V=[];
N=[];
m=[31 28 31 30 31 30 31 31 30 31 30 31];
for i=1:m(mon)
    [v n]=loadDay(year, mon, i);
    V=[V v];
    N=[N n];
end

function [V N]=loadDay(year, mon, day)
li=getPath(year, mon, day);
O=[];
V=[];
N=[];
for l=li
    time=getTime(l);
    [v n]=load1MinData(l);
    v=[time ; v];
    n=[time ; n];
    try
        V=[V v];
        N=[N n];
    catch
        fprintf('%s\n', l{1});
    end
end

function time=getTime(path)%-8
p=path{1};
year=str2num(p(40:43));
mon=str2num(p(45:46));
day=str2num(p(48:49));
hour=str2num(p(51:52));
min=str2num(p(54:55));
sec=str2num(p(57:58));
time=datenum([year mon day hour min sec]);

function [V N]=load1MinData(path)
path=path{1};
A=json.read(path);
[s1 s2]=size(A);
V=[];
N=[];
for i=1:s1
    for j=1:s2
        a=A(i,j);
        a=a{1};
        [a1 a2]=size(a);
        if a1~=1 && a2~=1
            [t1 t2]=size(a);
            n=0;
            sum=0;
            for k=1:t1
                sum=sum+a(k,1)*a(k,2);
                n=n+a(k,2);
            end
            v=0;
            if n~=0
                v=sum/n;
            end
        else
            a=a{1};
            n=a(1,2);
            v=a(1,1);
        end
        V=[V ; v];
        N=[N ; n];
    end
end
l=getPath(2015,7,1);

function O=getPath(year, mon, day)
p='~/math/dd/data/json/';
m=strcat(num2str(year),'_');
m=strcat(m,padded(mon));
d=strcat(m,'_');
d=strcat(d,padded(day));
p=strcat(p,m);
p=strcat(p,'/');
p=strcat(p,d);
p=strcat(p,'/');
li=list(p);
O=[];
for l=li
    O=[O strcat(p,l)];
end

function o=padded(n)
if n<10
    o=strcat('0',num2str(n));
else
    o=num2str(n);
end
