function month_plot(N,V,m,s_h,e_h,remove,number)
A=[];
B=[];
month=[31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
for i=1:month(m)
    i
    A=[A choose_time(N,m,i,s_h,m,i,e_h,remove)];
    B=[B choose_time(V,m,i,s_h,m,i,e_h,remove)];
end
day_plot(A,B,number);