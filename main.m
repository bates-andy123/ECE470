gens = 10


 options = gaoptimset(@ga);
 options = gaoptimset(options,'SelectionFcn',{@selectionroulette},...
                      'MutationFcn',{@mutationuniform, 0.1},...
                      'Generations', gens,...
                      'TolFun', 0,...
                      'CrossoverFraction', 0.8,... 
                      'PopulationSize',12,...
                      'CrossoverFcn', {@crossoverarithmetic},...
                      'Display', ('diagnose'),...
                      'FitnessLimit', 0,...
                      'CreationFcn', {@PopFunction});
                     

%[x,fval,exitflag,output,population,scores]=ga(@fitness,25,options)
x = ones(1, 25);

idx = 1;
idx_list = [];

x_list = [];

fits_2016 = [];
percents_2016 = [];
results_2016 = [];

fits_2015 = [];
percents_2015 = [];
results_2015 = [];

for i = 1:50
    idx_list = [idx_list; idx];
    idx = idx + 1;
    
    x_list = [x_list; x];
    
    [fit, percent, result] = fitness(x, 2016);
    fits_2016 = [fits_2016; fit];
    percents_2016 = [percents_2016; percent'];
    results_2016 = [results_2016; result];
    
    [fit, percent, result] = fitness(x, 2015);
    fits_2015 = [fits_2015; fit];
    percents_2015 = [percents_2015; percent'];
    results_2015 = [results_2015; result];

    options = gaoptimset(options,'SelectionFcn',{@selectionroulette},...
                      'MutationFcn',{@mutationuniform, 0.1},...
                      'Generations', gens,...
                      'TolFun', 0,...
                      'CrossoverFraction', 0.8,... 
                      'PopulationSize',12,...
                      'CrossoverFcn', {@crossoverarithmetic},...
                      'Display', ('diagnose'),...
                      'FitnessLimit', 0,...
                      'InitialPopulation',x);

    [x,fval,exitflag,output,population,scores]=ga(@fitness,25,options)
end
       
csvwrite("2016_F1.csv", [idx_list fits_2016 percents_2016 x_list]);
csvwrite("2016_Results.csv", [results_2016]);

csvwrite("2015_F1.csv", [idx_list fits_2015 percents_2015 x_list]);
csvwrite("2015_Results.csv", [results_2015]);