function O=load_file(file_path, is_N, method) 
%取得此路徑下的.json檔的速度資料 method=1 > average car around , 2 > car weight , 3 >
%car number
%file_path{1}
 R=read_json(file_path{1});
 A=[];
 if is_N
     D=R(79:end);
 else
     D=R(1:78);
 end
for b=D
    sum=0;
    switch method
        case 1
            for k=b.lane
                sum=sum+str2num(k.speed);
            end
            a=[distance(b.vdid) sum/length(b.lane)];
        case 2
            div=0;
            for k=b.lane
                sum=sum+str2num(k.speed)*get_car(k.cars);
                div=div+get_car(k.cars);
            end
            if div==0
                a=[distance(b.vdid) 0];
            else  
                a=[distance(b.vdid) sum/div];
            end
        case 3
            for k=b.lane
                sum=sum+get_car(k.cars);
            end
            a=[distance(b.vdid) sum];
    end
    A=[A ;a];
end
B=sortrows(A, 1);
O=[time_axis(R(1).datacollecttime) ;B(:, 2)];
