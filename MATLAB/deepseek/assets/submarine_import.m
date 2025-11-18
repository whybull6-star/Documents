% Submarine STL Import and Visualization
clear; clc; close all;

stlFile = 'submarine.stl';   % Just the filename, since it's in the same folder
TR = stlread(stlFile);

figure;
trisurf(TR, 'FaceColor', [0.2 0.4 0.8], 'EdgeColor', 'none', 'FaceAlpha', 0.8);
camlight; lighting gouraud;
title('Submarine 3D Model');
xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
axis equal; grid on; rotate3d on;