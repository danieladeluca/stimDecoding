%% MAIN SETTINGS

% EXPERIMENT SETTINGS
% -------------------------------------------------------------------------
settings.stimuli = {'circle','cross','triangle'};
settings.repetitions = 2;
settings.preStim = 1;                           % in seconds
settings.durStim = 1;                           % in seconds
settings.postStim = 4;                          % in seconds

% Folder where to save the result of the experiments
settings.savingFolder = 'F:\stimDecoding\gNex_26\';

% TCP/IP SETTINGS
% -------------------------------------------------------------------------
settings.tcp.address = '192.168.1.3';
settings.tcp.port = 40000;

nFrames = 60;


%% Connect to the camera and initialize it
[vid, src] = loadCamera_PCOEdge();

% totalDuration = settings.preStim + settings.durStim + settings.postStim;
% vid.FramesPerTrigger = round(totalDuration * str2double(src.FrameRate));
vid.FramesPerTrigger = 1;
vid.TriggerRepeat = 59;

%% Setup TCP/IP connection with the psychopy instance on localhost
stimList = pseudorandomSequence(settings.stimuli, settings.repetitions);

tcp = connectTCP_server(settings.tcp.address, settings.tcp.port);
fopen(tcp);

%% MAIN LOOP
h = src.H5HardwareROI_Height;
w = src.H2HardwareROI_Width;

sumImg_Triangle = zeros(h/2,w/2,'double');
sumImg_Circle = zeros(h/2,w/2,'double');
sumImg_Cross = zeros(h/2,w/2,'double');

pth = settings.savingFolder;
rawTriangle = zeros(h/2, w/2, nFrames, settings.repetitions,'uint16');
rawCircle = zeros(h/2, w/2, nFrames, settings.repetitions,'uint16');
rawCross = zeros(h/2, w/2, nFrames, settings.repetitions,'uint16');

m = matfile([pth filesep 'rec_' datestr(now, 'YYYYmmDD-hhMMss') '.mat'],...
    'Writable',true);
m.rawTriangle = rawTriangle;
m.rawCircle = rawCircle;
m.rawCross = rawCross;

clear rawTriangle rawCircle rawCross
crossN = 1;
triangleN = 1;
circleN = 1;

for i = 1:length(stimList)
    fprintf('Trial [%u/%u]...', i, length(stimList))
    start(vid)
    % Send current trial to python that whil trigget the camera
    fwrite(tcp, stimList{i});
    % Wait for the acquisition to finish
    wait(vid,25)
    fprintf(' done.\n Processing...')
    % Preprocess data, save it and display preview
    [data,time] = getdata(vid, nFrames);
    stop(vid)
    fprintf(' got data. ')
    if i == 1
        [f, im_T, im_C, im_X] = createPreviewFigure([w, h]);
    end
    
    data = imresize(squeeze(data),0.5);
    fprintf(' resized. ')
    switch stimList{i}
        case 'triangle'
            saveRawData(m, data, 'triangle', triangleN)
            updatePreviewFigure(im_T, sumImg_Triangle, data, triangleN)
            triangleN = triangleN + 1;
        case 'cross'
            saveRawData(m, data, 'cross', crossN)
            updatePreviewFigure(im_X, sumImg_Cross, data, crossN)
            crossN = crossN + 1;
        case 'circle'
            saveRawData(m, data, 'circle', circleN)
            updatePreviewFigure(im_C, sumImg_Circle, data, circleN)
            circleN = circleN + 1;
    end
    fprintf('done.\n')
end
fwrite(tcp, 'stop');
fclose(tcp);


%% cleanup

delete(vid);
fclose(tcp);
close all
clear all
clc








