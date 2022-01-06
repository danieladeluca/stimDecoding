function [vid, src] = loadCamera_webcam()



settings.camera.adaptor = 'winvideo';                   % AdaptorName. See the folder camera_support for installing the adaptor
settings.camera.deviceID = 1;                           % In case there are multiple cameras
settings.camera.format = 'MJPG_640x480';                % Acquisition format (1x1, 2x2,4x4 binning; various bit-depth)

settings.camera.TriggerMode = 'manual';             % 'immediate', 'manual' or 'hardware'
settings.camera.TriggerCondition = 'risingEdge';    % Only if mode = hardware. 'risingEdge' or 'fallingEdge'
settings.camera.TriggerSource = 'externalTriggerMode0-Source0';

% Get the videoinput object
fprintf(['Loading up the camera: [' settings.camera.adaptor '] with format: [' settings.camera.format ']...'])

vid = videoinput(settings.camera.adaptor, settings.camera.deviceID , settings.camera.format);
src = getselectedsource(vid);

% Setup the Camera acquisition parameters

% Trigger
triggerconfig(vid, settings.camera.TriggerMode);

fprintf(' done\n')