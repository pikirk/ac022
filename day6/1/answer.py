signal = ""
with open('/Users/pikirk/src/aoc22/day6/1/input.txt', 'r') as fp:
    while True:
        char = fp.read(1)
        if not char: break
        signal += char
        
packet = [signal[0], signal[1], signal[2], signal[3]]
position = 4
for c in range(4, len(signal)):
    if len(packet) < 4:
        packet.append(signal[c -1])
    if len(set(packet)) == 4: # uniqueness check
        break;
    else:
        packet.pop(0)
    position += 1

print (position)