function sub(A, is_N, location)
if is_N
    A(39, :)=[];
    location(38)=[];
    A(38, :)=[];
    location(37)=[];
    A(13, :)=[];
    location(12)=[];
    A(11, :)=[];
    location(10)=[];
else
    A(37, :)=[];
    location(36)=[];
    A(35, :)=[];
    location(34)=[];
    A(12, :)=[];
    location(11)=[];
    A(10, :)=[];
    location(9)=[];
end
paint(A, location)