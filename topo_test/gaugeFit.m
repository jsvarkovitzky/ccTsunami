%This program generates comparsion plots between our gauge data
%and that of the USACE
%Jonathan Varkovitzky
%3/26/2011
close all
clear all
clc

USACE = load('ts2c.txt');
USACEtime = USACE(:,1)-20;
USACEg3 = USACE(:,4);
USACEg6 = USACE(:,6);
USACEg9 = USACE(:,7);
USACEg16= USACE(:,8);
USACEg22= USACE(:,9);
ourData = load('_output/fort.gauge');

nGauges = 9;
nData = size(ourData,1);
depth = 0.32;
ourData(:,4) = ourData(:,4)-depth;
%extract Data from fort.gauge
for i = 1:nData/nGauges
    g1(i) = ourData((i-1)*nGauges+1,4);
    g2(i) = ourData((i-1)*nGauges+2,4);
    g3(i) = ourData((i-1)*nGauges+3,4);
    g4(i) = ourData((i-1)*nGauges+4,4);
    g6(i) = ourData((i-1)*nGauges+5,4);
    g9(i) = ourData((i-1)*nGauges+6,4);
    g16(i)= ourData((i-1)*nGauges+7,4);
    g22(i)= ourData((i-1)*nGauges+8,4);
end
%extract Time from fort.gauge
for i = 1:nData/nGauges
    time(i) = ourData((i-1)*nGauges+1,3);
end
% % %Comparison plot at gauge 3
% % figure(1)
% % subplot(2,2,1)
% % plot(USACEtime,USACEg3)
% % title('Data Measurments at Gauge 3 (Position Not Provided)')
% % xlabel('Time (seconds)')
% % ylabel('\eta')
% % hold on
% % plot(time,g3,'r')
% % legend('USACE Data','Tide Gauge','location','NorthEast')
% % axis([0,60,-0.01,0.02])
% % saveas(figure(1),'g3.pdf')

%Comparison plot at gauge 6
figure(1)
subplot(2,2,1)
plot(USACEtime,USACEg6)
title('Data Measurments at Gauge 6')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time,g6-g6(1),'r')
legend('USACE Data','Tide Gauge','location','NorthEast')
axis([0,60,-0.04,0.065])

subplot(2,2,2)
plot(USACEtime,USACEg9)
title('Data Measurments at Gauge 9')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time,g9-g9(1),'r')
legend('USACE Data','Tide Gauge','location','NorthEast')
axis([0,60,-0.05,0.065])

subplot(2,2,3)
plot(USACEtime,USACEg16)
title('Data Measurments at Gauge 16')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time,g16-g16(1),'r')
legend('USACE Data','Tide Gauge','location','NorthEast')
axis([0,60,-0.04,0.065])

subplot(2,2,4)
plot(USACEtime,USACEg22)
title('Data Measurments at Gauge 22')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time,g22-g22(1),'r')
legend('USACE Data','Tide Gauge','location','NorthEast')
axis([0,60,-0.03,0.07])

saveas(figure(1),'gauges.pdf')