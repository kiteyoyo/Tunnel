function paint2(A, location)
time=A(1, :);
A(1, :)=[];
pcolor(time, location, A)
xlabel('time')
ylabel('location')
datetick('x', 'mmm, dd HH:MM')