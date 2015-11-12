function O=repair(A)
[s1 s2]=size(A);
for i=1:s2
    bob=-1;
    for j=2:(s1-1)
        if (A(j,i)==0 || A(j,i)>500) && bob<0
            bob=j;
        end
        if (A(j,i)>0 && A(j,i)<500) && bob>0
            if bob==2
                for k=2:(j-1)
                    A(k,i)=A(j,i);
                end
            else
                for k=bob:(j-1)
                    A(k,i)=A(bob-1,i)+((A(j,i)-A(bob-1,i))/(j-bob+1))*(k-bob+1);
                end    
            end
            bob=-1;
        end
    end
end
O=A;