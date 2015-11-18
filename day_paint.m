function day_paint(A,number)
sum=zeros(1,2000);
num=zeros(1,2000);
for a=A
    t=mod(a(1),1);
    if ~is_holiday(a(1))
        plot(t,a(number),'b*');
        n=floor(t*24*60)+1;
        sum(n)=sum(n)+a(number);
        num(n)=num(n)+1;
    end
    hold on
end
[s1 s2]=size(sum);
j=1;
for i=1:s2
    
    if num(i)~=0
        t(j)=i/1440;
        r(j)=sum(i)/num(i);
        %plot(i/24/60,sum(i)/num(i),'r+');
        j=j+1;
    end
end
plot(t,r,'r-');
xlabel('time')
datetick('x', 'HH:MM')