function updatePreviewFigure(imHandle, data, newData, iterNumber)

newData = double(newData);
df = dRoR(newData, newData(:,:,1:10));

df = mean(df(:,:,10:20),3);
totalAverage = (data + df) / iterNumber;
imHandle.CData = totalAverage;


