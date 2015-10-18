function paint(A, is_N, location)
time=A(1, :);
A(1, :)=[];
mesh(time, location, A)
xlabel('time')
ylabel('location')
datetick('x', 'mmm, dd HH:MM')