function day_plot(n,v,number)
n=n(number,:);
v=v(number,:);
for i=1:8457
    plot(n(i), v(i),'*');
    hold on;
end