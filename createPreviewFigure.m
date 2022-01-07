function [f, im_T, im_C, im_X] = createPreviewFigure(imSize)


f = figure('Position', [81,328,1206,297],'MenuBar','none',...
    'Name','Preview');

dummyImg = zeros(imSize(1),imSize(2),'uint8');

subplot(1,3,1)
im_T = imagesc(dummyImg);
axis off
axis image
title('Avg Tiangle')
colorbar
subplot(1,3,2)
im_C = imagesc(dummyImg);
axis off
axis image
title('Avg Circle')
colorbar
subplot(1,3,3)
im_X = imagesc(dummyImg);
axis off
axis image
colorbar
title('Avg Cross')


