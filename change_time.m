function O=change_time(A)
[s1 s2]=size(A);
for i=1:s2
    A(1,i)=get_time(A(1,i));
end
O=A;