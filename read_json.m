function A=read_json(file_path)
X=json.read(file_path);%file_path{1}
 A=X.XML_Head.Infos.Info;