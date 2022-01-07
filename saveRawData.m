function saveRawData(m, data, trial, repNumber)

switch trial
    case 'triangle'
        m.rawTriangle(:,:,:,repNumber) = data;
    case 'cross'
        m.rawCross(:,:,:,repNumber) = data;
    case 'circle'
        m.rawCircle(:,:,:,repNumber) = data;
end

