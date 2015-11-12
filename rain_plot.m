function rain_plot(N,R,n_i,r_i)
%data_arrey = [Time lat lon ElEV RAIN MIN10 HOUR3 HOUR6 HOUR12 HOUR24 NOW]
[s1 s2]=size(N);
time=N(1,:);
y=N(n_i,:);
plot(time,y,'b-');
hold on
%for i=1:s2
%    if N(n_i,i)>0
%        plot(N(1,i),N(n_i,i),'b--o');
%        hold on
%    end
%end
[s1 s2]=size(R);
for i=1:s2
    if R(r_i,i)>=0 
        plot(R(1,i),R(r_i,i)*10,'r*');
        hold on
    end
end
xlabel('time')
switch r_i
    case 2
        ylabel('lat')
    case 3
        ylabel('lon')
    case 4
        ylabel('ELEV')
    case 5
        ylabel('RAIN')
    case 6
        ylabel('MIN10')
    case 7
        ylabel('HOUR3')
    case 8
        ylabel('HOUR6')
    case 9
        ylabel('HOUR12')
    case 10
        ylabel('HOUR24')
    case 11
        ylabel('NOW')
end
datetick('x','mm dd,HH:MM')