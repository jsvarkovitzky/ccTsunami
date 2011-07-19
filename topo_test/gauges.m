%This program generates comparsion plots between our gauge data
%and that of the USACE
%Jonathan Varkovitzky
%3/26/2011
close all
clear all
clc

USACE = load('ts2b.txt');
USACEtime = USACE(:,1)-20;
USACEg3 = USACE(:,4);
USACEg6 = USACE(:,6);
USACEg9 = USACE(:,7);
USACEg16= USACE(:,8);
USACEg22= USACE(:,9);
ourData200 = load('fort200c.gauge');
ourData100 = load('fort100c.gauge');
ourData50  = load('fort50c.gauge');
%*********************************************
%200 Resolution Data
%*********************************************
nGauges = 9;
nData200 = size(ourData200,1);
depth = 0.32; 
ourData200(:,4) = ourData200(:,4)-depth;
%extract Data from fort.gauge
for i = 1:nData200/nGauges
    g1_200(i) = ourData200((i-1)*nGauges+1,4);
    g2_200(i) = ourData200((i-1)*nGauges+2,4);
    g3_200(i) = ourData200((i-1)*nGauges+3,4);
    g4_200(i) = ourData200((i-1)*nGauges+4,4);
    g6_200(i) = ourData200((i-1)*nGauges+5,4);
    g9_200(i) = ourData200((i-1)*nGauges+6,4);
    g16_200(i)= ourData200((i-1)*nGauges+7,4);
    g22_200(i)= ourData200((i-1)*nGauges+8,4);
end
%extract Time from fort.gauge
for i = 1:nData200/nGauges
    time200(i) = ourData200((i-1)*nGauges+1,3);
end

%*********************************************
%100 Resolution Data
%*********************************************
nGauges = 9;
nData100 = size(ourData100,1);
depth = 0.32;
ourData100(:,4) = ourData100(:,4)-depth;
%extract Data from fort.gauge
for i = 1:nData100/nGauges
    g1_100(i) = ourData100((i-1)*nGauges+1,4);
    g2_100(i) = ourData100((i-1)*nGauges+2,4);
    g3_100(i) = ourData100((i-1)*nGauges+3,4);
    g4_100(i) = ourData100((i-1)*nGauges+4,4);
    g6_100(i) = ourData100((i-1)*nGauges+5,4);
    g9_100(i) = ourData100((i-1)*nGauges+6,4);
    g16_100(i)= ourData100((i-1)*nGauges+7,4);
    g22_100(i)= ourData100((i-1)*nGauges+8,4);
end
%extract Time from fort.gauge
for i = 1:nData100/nGauges
    time100(i) = ourData100((i-1)*nGauges+1,3);
end

%*********************************************
%100 Resolution Data
%*********************************************
nGauges = 9;
nData50 = size(ourData50,1);
depth = 0.32;
ourData50(:,4) = ourData50(:,4)-depth;
%extract Data from fort.gauge
for i = 1:nData50/nGauges
    g1_50(i) = ourData50((i-1)*nGauges+1,4);
    g2_50(i) = ourData50((i-1)*nGauges+2,4);
    g3_50(i) = ourData50((i-1)*nGauges+3,4);
    g4_50(i) = ourData50((i-1)*nGauges+4,4);
    g6_50(i) = ourData50((i-1)*nGauges+5,4);
    g9_50(i) = ourData50((i-1)*nGauges+6,4);
    g16_50(i)= ourData50((i-1)*nGauges+7,4);
    g22_50(i)= ourData50((i-1)*nGauges+8,4);
end
%extract Time from fort.gauge
for i = 1:nData50/nGauges
    time50(i) = ourData50((i-1)*nGauges+1,3);
end


%Comparison plot at gauge 6
figure(1)
subplot(2,2,1)
plot(USACEtime,USACEg6)
title('Run C Gauge 6')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time50, g6_50 - g6_50(1),'k')
plot(time100,g6_100-g6_100(1),'r')
plot(time200,g6_200-g6_200(1),'g')
legend('USACE Data','GeoClaw 60cm cell','GeoClaw 30cm cell','GeoClaw 15cm','location','NorthEast')
axis([0,60,-0.04,0.065])

subplot(2,2,2)
plot(USACEtime,USACEg9)
title('Run C Gauge 9')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time50, g9_50 - g9_50(1),'k')
plot(time100,g9_100-g9_100(1),'r')
plot(time200,g9_200-g9_200(1),'g')
legend('USACE Data','GeoClaw 60cm cell','GeoClaw 30cm cell','GeoClaw 15cm','location','NorthEast')
axis([0,60,-0.05,0.065])

subplot(2,2,3)
plot(USACEtime,USACEg16)
title('Run C Gauge 16')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time50, g16_50 - g16_50(1),'k')
plot(time100,g16_100-g16_100(1),'r')
plot(time200,g16_200-g16_200(1),'g')
legend('USACE Data','GeoClaw 60cm cell','GeoClaw 30cm cell','GeoClaw 15cm','location','NorthEast')
axis([0,60,-0.04,0.065])

subplot(2,2,4)
plot(USACEtime,USACEg22)
title('Run C Gauge 22')
xlabel('Time (seconds)')
ylabel('\eta')
hold on
plot(time50, g22_50 - g22_50(1),'k')
plot(time100,g22_100-g22_100(1),'r')
plot(time200,g22_200-g22_200(1),'g')
legend('USACE Data','GeoClaw 60cm cell','GeoClaw 30cm cell','GeoClaw 15cm','location','NorthEast')
axis([0,60,-0.03,0.07])

saveas(figure(1),'gaugesRunC.pdf')