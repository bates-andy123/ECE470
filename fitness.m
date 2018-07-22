function [ fit ] = fitness( variables )
%fitness Summary of this function goes here
%   Detailed explanation goes here
team_stats = csvread('our_data/training/2010_data.csv', 2, 1);
team_scores = variables * team_stats;

winners = csvread('our_data/winners/2010_bracket.csv', 7, 0);

for k = 1:6
    
end

fit = 1;
end