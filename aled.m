clc();
clearvars();

%données
umin=-5;
nbpts=10000;
u=linspace(umin,-umin,nbpts);

phi0=inputdlg("Quelle est la valeur de phi0 en degrés ?");
phi0=str2num(phi0{1})*pi/180
alpha=inputdlg("Quelle est la valeur de alpha ?");
alpha=str2num(alpha{1})

X=0.5*alpha.*(exp(-1i.*((pi.*(u-1)*alpha)-phi0)).*sinc(alpha.*(u-1))+exp(-1i*(pi*((u+1).*alpha)+phi0)).*sinc(alpha.*(u+1)));
amplitude=abs(X);
phi=angle(X)*180/pi;

figure;
hold on;
fenAmp=subplot(1,1,1,'replace');
amp=plot(fenAmp,u,amplitude);
amp(1).LineWidth=1.5;
amp(1).Color=[0,0,1];
fenAmp.XAxisLocation='origin';
fenAmp.YAxisLocation='origin';
fenAmp.YLim=[-0.1;max(amplitude)*1.05];
grid on;
grid minor;
fenAmp.GridAlpha=0.4;
fenAmp.MinorGridAlpha=0.4;
title(fenAmp,'Spectre d''amplitude');
xlabel(fenAmp,'$\displaystyle{\frac{f}{f_0}}$');
labely=strcat('$\displaystyle{\frac{X_o\left(f\right)}{\hat{X}}f_0}\;\mathrm{pour}\;\alpha=',string(alpha), ...
    '\;\mathrm{et}\;\varphi_0=',string(phi0*180/pi),'^\circ$');
ylabel(fenAmp,labely);
% ylabel(fenAmp,'$\alpha$');
fenAmp.XLabel.Interpreter='latex';
fenAmp.YLabel.Interpreter='latex';
fenAmp.XLabel.FontSize=14;
fenAmp.YLabel.FontSize=14;

figure;
hold on;
fenPh=subplot(1,1,1,'replace');
phase=plot(fenPh,u,phi);
phase(1).LineWidth=1.5;
phase(1).Color=[0,0,1];
fenPh.XAxisLocation='origin';
fenPh.YAxisLocation='origin';
fenPh.YLim=[-185,185];
grid on;
grid minor;
fenPh.GridAlpha=0.4;
fenPh.MinorGridAlpha=0.4;
titre='Spectre de phase';
title(fenPh,titre);
xlabel(fenPh,'$\displaystyle{\frac{f}{f_0}}$');
labely=strcat('$\varphi\;(^\circ)\;\mathrm{pour}\;\alpha=',string(alpha), ...
    '\;\mathrm{et}\;\varphi_0=',string(phi0*180/pi),'^\circ$');
ylabel(fenPh,labely);
fenPh.XLabel.Interpreter='latex';
fenPh.YLabel.Interpreter='latex';
fenPh.XLabel.FontSize=14;
fenPh.YLabel.FontSize=14;
