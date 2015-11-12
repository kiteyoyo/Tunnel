function [O l]=regular(A, is_N, remove_gateway)
if is_N
    location=[0.178000000000000,0.706000000000000,1.06800000000000,1.43500000000000,1.78800000000000,2.06800000000000,2.45500000000000,2.84900000000000,3.19800000000000,4.04400000000000,4.05800000000000,4.40000000000000,4.45500000000000,4.46000000000000,5.52300000000000,5.88300000000000,6.41300000000000,7.11300000000000,7.63600000000000,8.04300000000000,8.70300000000000,9.01300000000000,9.37300000000000,9.84000000000000,10.1470000000000,10.5060000000000,10.8660000000000,11.1780000000000,11.5550000000000,11.8960000000000,12.2380000000000,12.5790000000000,12.9220000000000,13.3480000000000,13.7630000000000,14.5500000000000,14.5830000000000,14.6830000000000,14.8000000000000,15.4880000000000,15.8550000000000,16.1960000000000,16.5700000000000,16.9000000000000,17.2680000000000,17.6080000000000,17.9980000000000,18.3130000000000,18.6620000000000,19.0120000000000,19.3610000000000,19.6890000000000,20.0620000000000,20.4120000000000,20.7520000000000,21.0550000000000,21.4440000000000,21.8080000000000,22.1580000000000,22.5100000000000,22.8590000000000,23.2090000000000,23.5680000000000,23.9110000000000,24.2640000000000,24.6770000000000,24.9520000000000,25.3100000000000,25.6520000000000,26.0070000000000,26.3000000000000,26.7050000000000,27.0560000000000,27.4680000000000,27.7790000000000,28.4200000000000,29.8430000000000,30.1000000000000];
else
    location=[1.072,1.424,1.766,2.05,2.433,2.835,3.178,3.506,3.806,4.016,4.178,4.395,4.749,5.523,6.498,7.113,7.553,7.923,8.669,9.063,9.326,9.84,10.145,10.495,10.845,11.158,11.545,11.895,12.245,12.595,12.945,13.343,14.356,14.483,14.54,14.691,15.139,15.478,15.856,16.201,16.551,16.902,17.253,17.608,17.99,18.312,18.663,19.013,19.363,19.677,20.063,20.413,20.763,21.063,21.46,21.807,22.159,22.506,22.859,23.207,23.56,23.91,24.264,24.678,24.962,25.312,25.664,26.013,26.299,26.706,27.054,27.442,27.748,28.236,29.716,30.14,30.249,30.266];
end
if remove_gateway
    if is_N
        A(78:79,:)=[];
        location(77:78)=[];
        A(38:39,:)=[];
        location(37:38)=[];
        A(11:14,:)=[];
        location(10:13)=[];
    else
        A(76:79,:)=[];
        location(75:78)=[];
        A(34:37,:)=[];
        location(33:36)=[];
        A(10:12,:)=[];
        location(9:11)=[];
    end
    A=repair(A);
end
l=location;
O=A;