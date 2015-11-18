function remove_utliers(all,n)
for i=1:(1440/n+1)
    am=all(i);
    a=am{1};
    mid_a=median(a);
    b=abs(a-mid_a);
    mid_b=median(b);
    p=mid_b/0.6745;
    c=b./p;
    t=(i-1)/1440*n;
    [s1 s2]=size(c);
    for j=1:s2
        plot(t,a(j),'*r')
        hold on;
%         if c(j)<1
%             plot(t,a(j),'*b');
%             hold on;
%         end
    end
    fprintf('%d\n',i);
end

xlabel('time')
ylabel('number')
datetick('x', 'HH:MM')