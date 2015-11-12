function O=choose_time(A, s_m, s_d, s_h, e_m, e_d, e_h,remove)
s_n=datenum([2015, s_m,s_d,s_h,0,0]);
e_n=datenum([2015, e_m,e_d,e_h,0,0]);
[r c]=size(A);
s_i=1;
e_i=c;
for i=2:(c-1)
    if A(1,i-1)<s_n && A(1,i)>=s_n
        s_i=i;
    end
    if A(1,i)<=e_n && A(1,i+1)>e_n
        e_i=i;
    end
end
if remove
    A(:,s_i:e_i)=[];
    O=A;
else
    O=A(:,s_i:e_i);
end