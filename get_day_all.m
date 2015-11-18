function all=get_day_all(A,number,n)
all=[];
for i=1:(1440/n+1)
    all=[all;{[]}];
end
last_time=-1;
sum=0;
for a=A
    time=floor(mod(a(1),1)*1440/n)+1;
    if n==1
        if a(number)>0 && is_holiday(a(1))
            lim=all(time);
            li=lim{1};
            li=[li a(number)];
            all(time)={li};
        end
    else
        if last_time==time || last_time==-1
            sum=sum+a(number);
        else
            if sum>0 && ~is_holiday(a(1))
        
                lim=all(time);
                li=lim{1};
                li=[li sum];
                all(time)={li};
            end
            sum=0;
        end
        last_time=time;
    end
end