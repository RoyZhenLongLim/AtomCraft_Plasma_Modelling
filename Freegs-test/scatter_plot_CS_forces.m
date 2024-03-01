clear; clc; clf;
rawdata = readmatrix('CS_end.csv');
x = reshape(rawdata(:,1),[],104);               
y = reshape(rawdata(:,2),[],104);
z = zeros(1,104);


u = zeros(1,104);
v = zeros(1,104);
F = reshape(rawdata(:,6),[],104);

F_mag = sqrt(F.^2);

plot3(x,y,z, 'k-','LineWidth',2);
set(gca,'DataAspectRatio',[1 1 0.3]);
set(gca,'ztick',[])
xlabel('R-axis') 
ylabel('Z-axis') 
hold on
plot3(-x,y,z, 'k-','LineWidth',2);

%axis off

zlim([-0.01 0.01])
hold on

q1 = quiver3(x,y,z,F,u,v);
hold on
q2 = quiver3(-x,y,z,-F,u,v);

colormap(jet);
c = colorbar;
SetQuiverColor(q1,jet,'mags',F_mag,'range',[min(F_mag), max(F_mag)]);
SetQuiverColor(q2,jet,'mags',F_mag,'range',[min(F_mag), max(F_mag)]);
caxis([min(F_mag), max(F_mag)]);
c.Label.String = 'Magnitude of Lorentz Force (N)';

%scatter3(x,y,F)