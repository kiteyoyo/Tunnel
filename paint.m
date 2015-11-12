function paint(A, is_N, remove_gateway,number)
[A location]=regular(A,is_N,remove_gateway);
time=A(1, :);
A(1, :)=[];
fh=figure;
dcm=datacursormode(fh);
if number>1
    number=number-1;
    A=A(number,:);
    plot(time,A)
else
    mesh(time, location, A)
end
xlabel('time')
ylabel('location')
datetick('x', 'mm,dd HH:MM')
datacursormode on
set(dcm, 'updatefcn', @myfunction);

function output_txt = myfunction(obj,event_obj)
% Display the position of the data cursor
% obj          Currently not used (empty)
% event_obj    Handle to event object
% output_txt   Data cursor text string (string or cell array of strings).

pos = get(event_obj,'Position');
output_txt = {['X: ',datestr(pos(1))],...
    ['Y: ',num2str(pos(2),4)]};

% If there is a Z-coordinate in the position, display it as well
if length(pos) > 2
    output_txt{end+1} = ['Z: ',num2str(pos(3),4)];
end
