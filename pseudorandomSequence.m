function sequence = pseudorandomSequence(elements, repetitions)

sequence = cell(0);

for i = 1:repetitions
    sequence = cat(2, sequence, elements(randperm(length(elements))));
end
