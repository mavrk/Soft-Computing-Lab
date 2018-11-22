function [x,fval,exitflag,output,population,score] = ga_1_1048915(nvars,lb,ub)
%% This is an auto generated MATLAB file from Optimization Tool.

%% Start with the default options
options = gaoptimset;
%% Modify options setting
options = gaoptimset(options,'Display', 'off');
options = gaoptimset(options,'PlotFcns', {  @gaplotbestf @gaplotbestindiv });
[x,fval,exitflag,output,population,score] = ...
ga(@(x)-5*sin(x(1))*sin(x(2))*sin(x(3))+floor(-1*sin(5*x(1))*sin(5*x(2))*sin(5*x(3))),nvars,[],[],[],[],lb,ub,[],[],options);
