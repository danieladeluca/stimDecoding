%% MAIN SETTINGS

% EXPERIMENT SETTINGS
% -------------------------------------------------------------------------
settings.stimuli = {'circle','cross','triangle','gray'};
settings.repetitions = 10;
settings.preStim = 1;                           % in seconds
settings.durStim = 1;                           % in seconds
settings.postStim = 3;                          % in seconds

% Folder where to save the result of the experiments
settings.savingFolder = 'C:\Users\Leonardo\Documents\';

% TCP/IP SETTINGS
% -------------------------------------------------------------------------
settings.tcp.address = 'localhost';
settings.tcp.port = 80;
settings.tcp.bufferSize = 4096;

%% Connect to the camera and initialize it
[vid, src] = loadCamera_webcam();

%% Setup TCP/IP connection with the psychopy instance on localhost
tcp = connectTCP_server(settings.tcp.address, settings.tcp.port, settings.tcp.bufferSize);







stimList = pseudorandomSequence(settings.stimuli, settings.repetitions);








