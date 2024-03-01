clear; clc; clf;
rawdata = readmatrix('TF_mid.csv');
x = reshape(rawdata(:,1),[],504);                % Reshape the column matrix into 51 columns
y = reshape(rawdata(:,2),[],504);
z = zeros(1,504);

u = zeros(1,504);
v = zeros(1,504);
F = reshape(rawdata(:,7),[],504);

F_mag = sqrt(F.^2);

plot3(x,y,z, 'k-','LineWidth',2);
set(gca,'DataAspectRatio',[1 1 0.3]);
axis off
hold on

q = quiver3(x,y,z,u,v,F);

colormap(jet);
c = colorbar;
SetQuiverColor(q,jet,'mags',F_mag,'range',[min(F_mag), max(F_mag)]);
caxis([min(F_mag), max(F_mag)]);
c.Label.String = 'Magnitude of Lorentz Force (N/m)';

%scatter3(x,y,F)