def drawHorizontalLine(screen, width, x1, x2, y):
    lineOffset = y * width / 8
    modX1 = x1 % 8
    modX2 = x2 % 8
    startAddress = lineOffset + x1 / 8
    endAddress = lineOffset + x2 / 8
    startRange = startAddress
    if modX1 > 0:
        startRange += 1
    for address in range(startRange, endAddress + 1):
        setByte(screen, address)

    if modX1 > 0:
        mask = (1 << 8-modX1) - 1
        screen[startAddress] |= mask
    if modX2 > 0:
        mask = ~((1 << 8-modX2) - 1)
        screen[endAddress] |= mask
    return screen


def setByte(screen, address):
    screen[address] |= 0xFF

width = 400
screen = drawHorizontalLine([0] * 50*50, width, 9, 397, 0)
for row in range(50):
    print str(row)+':',' '.join([(bin(screen[row*width/8+i] & 0xFF)[2:]).zfill(8) for i in range(50)])
