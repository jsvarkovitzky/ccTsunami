%plot wave make position and velocity vs time.
close all
clear all
clc

ourData200 = load('fort200a.gauge');
ourData100 = load('fort200b.gauge');
ourData50  = load('fort200c.gauge');
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
    g101_200(i)= ourData200((i-1)*nGauges+9,4);
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
    g101_100(i)= ourData100((i-1)*nGauges+9,4);
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
    g101_50(i)= ourData50((i-1)*nGauges+9,4);
end
%extract Time from fort.gauge
for i = 1:nData50/nGauges
    time50(i) = ourData50((i-1)*nGauges+1,3);
end


%Case A
sa = 0.025;
ba = 1.0;
t0a= 5.9;
%Case B
sb = 0.06;
bb = 2.0;
t0b= 4.8;
%Case C
sc = 0.18;
bc = 3.5;
t0c= 4.8;

t = [0:0.01:10];

figure(1)
subplot(3,3,1)
plot(t,sa*sech(ba*(t-t0a)).^2,'b')
title('A')
ylabel('Paddle Velocity')
subplot(3,3,2)
plot(t,sa*sech(ba*(t-t0a)).^2,'r')
title('B')
subplot(3,3,3)
plot(t,sa*sech(ba*(t-t0a)).^2,'k')
title('C')

subplot(3,3,4)
plot(t,sa*tanh(ba*(t-t0a)),'b')
ylabel('Paddle Position')
subplot(3,3,5)
plot(t,sb*tanh(bb*(t-t0b)),'r')

subplot(3,3,6)
plot(t,sc*tanh(bc*(t-t0c)),'k')

subplot(3,3,7)
plot(time200(1:176),g101_200(1:176),'b')
axis([0,10,0,0.1])
ylabel('Initial Wave Profile')
xlabel('Time (s)')

subplot(3,3,8)
plot(time100(1:184),g101_100(1:184),'r')
axis([0,10,0,0.1])
xlabel('Time (s)')

subplot(3,3,9)
plot(time50(1:176),g101_50(1:176),'k')
axis([0,10,0,0.1])
xlabel('Time (s)')

saveas(figure(1),'paddle.pdf')