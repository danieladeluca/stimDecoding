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
settings.tcp.port = 40000;



%% Connect to the camera and initialize it
[vid, src] = loadCamera_webcam();

totalDuration = settings.preStim + settings.durStim + settings.postStim;  
vid.FramesPerTrigger = round(totalDuration * str2double(src.FrameRate));

%% Setup TCP/IP connection with the psychopy instance on localhost
tcp = connectTCP_server(settings.tcp.address, settings.tcp.port);


%%
stimList = pseudorandomSequence(settings.stimuli, settings.repetitions);


for i = 1:2
    fprintf('Trial [%u/%u]...', i, length(stimList))

    start(vid)
    % Send current trial to python that whil trigget the camera
    write(tcp, stimList{i})
    trigger(vid)
    
    % Wait for the acquisition to finish
    wait(vid,25)
    fprintf(' done. Processing...')
    % Preprocess data, save it and display preview
    [data,time] = getdata(vid);
    stop(vid)

    fprintf('done.\n')
end



%%











