function num=get_num(A, number)
mx=max(max(A(number,:)))+1;
num=zeros(mx,1441);
for a=A
    t=mod(a(1),1);
    if ~is_holiday(a(1))
        plot(t,a(number),'b*');
        n=floor(t*24*60)+1;
        num(a(number)+1,n)=num(a(number)+1,n)+1;
        hold on;
    end
end
% total=sum(num,1);
% [s1 s2]=size(sum);
% j=1;
% for i=1:s2
%     
%     if num(i)~=0
%         t(j)=i/1440;
%         r(j)=sum(i)/num(i);
%         %plot(i/24/60,sum(i)/num(i),'r+');
%         j=j+1;
%     end
% end
% plot(t,r,'r-');
% xlabel('time')
% datetick('x', 'HH:MM')