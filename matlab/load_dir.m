function A=load_dir(dir_path, is_N, method)
file_all=list(dir_path);
A=[];
for file=file_all
    file_path=strcat(dir_path, file);
    A=[A  load_file(file_path, is_N, method)];
end