function d_paint(A,rank)
total=sum(A,1);
fh=figure;
dcm=datacursormode(fh);
[s1 s2]=size(A);
if ~rank
    for i=1:s2
        time=(i-1)/1440;
        for j=1:s1
            if A(j,i)>0
                plot(time,j-1);
                hold on;
            end
        end
    end
else
    sor=sort(A,1);
    mx=[];
    mx_t=[];
    for i=1:s2
        so=unique(sor(:,i));
        time=(i-1)/1440;
        m=0;
        for j=1:s1
            if A(j,i)~=0
                if A(j,i)==so(end) 
                    plot(time,j,'*r')
                    m=j;
                elseif A(j,i)==so(end-1);
                    plot(time,j,'*y')
                    m=j;
                elseif A(j,i)==so(end-2);
                    plot(time,j,'*g')
                end
                hold on;
            end
        end
        if m>0
            mx=[mx m];
            mx_t=[mx_t time];
        end
        fprintf('%d\n',i);
    end
end
plot(mx_t,mx,'k-');
xlabel('time')
ylabel('number')
datetick('x', 'HH:MM')
datacursormode on
set(dcm, 'updatefcn', @myfunction);

function output_txt = myfunction(obj,event_obj,A,total)
% Display the position of the data cursor
% obj          Currently not used (empty)
% event_obj    Handle to event object
% output_txt   Data cursor text string (string or cell array of strings).

pos = get(event_obj,'Position');
i=pos(2)*1440+1;
output_txt = {['time: ',datestr(pos(1))],...
    ['number: ',num2str(pos(2),4)],...
    ['P: ',num2str(A(i,pos(2))),'/',num2str(i)]};

% If there is a Z-coordinate in the position, display it as well
if length(pos) > 2
    output_txt{end+1} = ['Z: ',num2str(pos(3),4)];
end