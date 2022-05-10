import re

transcript = []
linenum = 0
pattern = re.compile('text:')

with open (r'C:\Users\Simone\Documents\transcript-parser\input.txt', 'rt') as input_file:
    for line in input_file:
        linenum += 1
        if pattern.search(line) != None:
            line = eval(line[5:])
            line = str().join(line)
            transcript.append(line.rstrip('\n'))

with open (r'C:\Users\Simone\Documents\transcript-parser\output.txt', 'wt') as output_file:
    transcript = ' '.join(transcript)
    print(transcript, file = output_file)
