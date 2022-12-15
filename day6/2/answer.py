signal = ""
with open('/Users/pikirk/src/aoc22/day6/2/input.txt', 'r') as fp:
    while True:
        char = fp.read(1)
        if not char: break
        signal += char

packet = []
marker_size = 14
for i in range(0, marker_size):         
    packet.append(signal[i])

position = marker_size
for c in range(14, len(signal)):
    if len(packet) < marker_size:
        packet.append(signal[c -1])
    if len(set(packet)) == marker_size: # uniqueness check
        break;
    else:
        packet.pop(0)
    position += 1

print (position)