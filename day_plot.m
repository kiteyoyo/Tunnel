function day_plot(N,V,number)
n=N(number,:);
v=V(number,:);
[s1 s2]=size(v);
for i=1:s2
    plot(n(i), v(i),'x');
    hold on;
    %text(n(i), v(i),datestr(V(1,i),15));
end