function all=get_day_all_5(A,number)
all=[];
for i=1:289
    all=[all;{[]}];
end
last_time=-1;
sum=0;
for a=A
    fprintf('%s | %d\n',datestr(mod(a(1),1)), floor(mod(a(1),1)*288+1.1));
    time=floor(mod(a(1),1)*288+1.1);
    if a(number)>0 && is_holiday(a(1))
        lim=all(time);
        li=lim{1};
        li=[li a(number)];
        all(time)={li};
    end
end