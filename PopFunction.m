%%% POPULATION FUNCTION
    function [pop] = PopFunction(GenomeLength,~,options)
    pop = (rand(options.PopulationSize, GenomeLength)); % Initial Population
    end