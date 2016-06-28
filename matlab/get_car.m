function n=get_car(D)
sum=0;
for d=D
    sum=sum+str2num(d.volume);
end
n=sum;