function l=list(dir_name)
%取得此路徑下有多少的.json檔名
path=strcat(dir_name, '/*.json');
list_struct_all=dir(path);
list_struct_name=rmfield(list_struct_all, {'date' 'bytes' 'isdir' 'datenum'});
l=struct2cell(list_struct_name);