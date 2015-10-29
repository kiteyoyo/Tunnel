function data_arrey = GetRain(path,localinput)
    list = dir([path '*.xml']);
    fprintf(1,'\n%s\t%d\n',path,length(list));
    setlocation = localinput;
    %data_arrey = [Time lat lon ElEV RAIN MIN10 HOUR3 HOUR6 HOUR12 HOUR24 NOW]
    data_arrey = [];
    find = 0;
    for r = 1:length(list)
        data = parseXML([path list(r).name]);
        long = size(data.Children);
        %Find the location we want,if we found,break
        for i = 1:long(2)
            if strcmp(data.Children(i).Name,'location')
                long2 = size(data.Children(i).Children);
            %If the location is what we want,then get the weather data
                for j = 1:long2(2)
                    %Set the time,lat,lon
                    if strcmp(data.Children(i).Children(j).Name,'locationName')
                        location = data.Children(i).Children(j).Children.Data;
                        if strcmp(location,setlocation)
                            data_arrey(r,1:3) = setbasic(data.Children(i).Children);
                            find = 1;
                            continue;
                        else
                            break;
                        end
                    end
                    %Set the weatherElement
                    if strcmp(data.Children(i).Children(j).Name,'weatherElement')
                        switch data.Children(i).Children(j).Children(2).Children.Data
                            case 'ELEV'
                                data_arrey(r,4) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'RAIN'
                                data_arrey(r,5) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'MIN_10'
                                data_arrey(r,6) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'HOUR_3'
                                data_arrey(r,7) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'HOUR_6'
                                data_arrey(r,8) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'HOUR_12'
                                data_arrey(r,9) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'HOUR_24'
                                data_arrey(r,10) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                            case 'NOW'
                                data_arrey(r,11) = str2num(data.Children(i).Children(j).Children(4).Children(2).Children.Data);
                        end
                    end
                end
                if find == 1
                    find = 0;
                    break;
                end
            end
        end
        fprintf('%d ',r);
    end
end
