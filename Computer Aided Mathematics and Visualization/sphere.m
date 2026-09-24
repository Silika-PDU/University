syms x y real %x and y are symbolic

r = 1; % radius is 1
upper(x,y) = sqrt(r^2 - x^2 - y^2); 
lower(x,y) = -sqrt(r^2 - x^2 - y^2);

figure
fsurf(upper, [-r r -r r], 'FaceColor', 'b')
hold on
fsurf(lower, [-r r -r r], 'FaceColor', 'r')
hold off
axis equal