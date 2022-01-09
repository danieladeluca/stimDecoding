%{
TEMPLATE for the analysis of the retinotopy location recordings.
---------------------------------------------------------------------------
There are 5 files in the folder. Each file represents a recording to a
different stimulus. Stimuli are small square patches containing a 
0.06cyc/deg square wave. Each trial consists of 1 second (10 frames) of
baseline where the square wave is present but stationary; then 1 second of
stimulation when the square wave flip its phase 4 times at 4 Hz; then 2
more seconds of recording and finally 2 seconds of interstimulus where no
data are recorded.

In thesere files only the average movie of the response across 25 trials is
saved and the raw data is in the variable avgMovie
%}


%% LOAD DATA

% Change accordingly to point to the location on the HDD where the
% retinotopy recordings are stored
RETINOTOPY_DATA_FOLDER = 'G:\Pizzorusso Lab\stimDecoding\OLD_V1\';

% Add all the subfolders of the curent folder to the MATLAB path
addpath(genpath(pwd))

% Find the full name of all the matfiles in the folder
fullNames = listfiles(RETINOTOPY_DATA_FOLDER, '.mat');

% Preallocate data for the recordings at the 5 locations
m = matfile(fullNames{1});          % Load first file to get the size of the movie
movieSize = size(m.avgMovie);
locations = {'left','center','right','up','down'};
movies = zeros(movieSize(1), movieSize(2), movieSize(3), 5, 'uint16');

% Load all data
for i=1:length(fullNames)
    fprintf('Loading: %s... ', fullNames{i})
    
    [p, f, e] = fileparts(fullNames{i});
    loc = strsplit(f,'-');
    loc = loc{end};

    m = matfile(fullNames{i});
    % Put data in the appropriate dimension
    switch loc
        case 'left'
            movies(:,:,:,1) = m.avgMovie;
        case 'center'
            movies(:,:,:,2) = m.avgMovie;
        case 'right'
            movies(:,:,:,3) = m.avgMovie;
        case 'up'
            movies(:,:,:,4) = m.avgMovie;
        case 'down'
            movies(:,:,:,5) = m.avgMovie;
    end

    % Check if there is an anatomy image
    if misField(m,'anatomy') && ~exist('anatomy','var')
        anatomy = m.anatomy;
    end

    fprintf('done.\n')
end



%% PREPROCESS

BASELINE_FRAMES = 10;

dF_movies = zeros(size(movies),'double');
for i = 1:size(movies,4)
    thisMovie = double(movies(:,:,:,i));
    dF_movies(:,:,:,i) = dRoR(thisMovie, thisMovie(:,:,1:BASELINE_FRAMES));
end

%% PLOT RESPONSE IMAGES

RESPONSE_WINDOW = [11, 21];

dF_images = zeros(size(dF_movies,1),size(dF_movies,2),size(dF_movies,4),'double');
for i = 1:size(dF_movies,4)
    croppedMovie = dF_movies(:,:,RESPONSE_WINDOW(1):RESPONSE_WINDOW(2),i);
    dF_images(:,:,i) = mean(croppedMovie,3);
end

f = figure('Position', [330,365,1100,660], 'Color','k');
axs = zeros(6,1);
imLimits = [min(dF_images,[],'all'),  max(dF_images,[],'all')];

% Repeat the center location so that on the 2 rows we have it in the center
toPlot = cat(3, dF_images(:,:,1:3), dF_images(:,:,4),dF_images(:,:,2), dF_images(:,:,5));
locationNames = {locations{1:3}, locations{4}, locations{2}, locations{5}};

for i = 1:6
    axs(i) = subtightplot(2,3,i);
    imagesc(toPlot(:,:,i))
    axis image, axis off
    title(sprintf('Avg Response [%s]',locationNames{i}),'Color',[1,1,1])
end

% PLOT VASCULATURE ANATOMY IMAGE
f_anat = figure('Color','k');
imshow(im2uint8(imadjust(anatomy)))
title('Vasculature Anatomy', 'Color',[1,1,1])

rectangle(gca, 'Position', [20,20, 143, 20], 'FaceColor', [1 1 1])
text(50,60,'1 mm', 'Color', [1,1,1],'FontSize',20, 'FontWeight','bold')








