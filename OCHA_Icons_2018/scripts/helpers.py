def enlargeViewboxSize(viewbox, margin):
    '''
    Enlarges the viewbox string by a certain margin.
    example usage:
    vb = enlargeViewboxSize('0 0 48 30', 10)
    '''

    sizeStrings = viewbox.split()

    result = ''
    result += str(int(float(sizeStrings[0])) - margin) + ' '
    result += str(int(float(sizeStrings[1])) - margin) + ' '
    result += str(int(float(sizeStrings[2])) + margin * 2) + ' '
    result += str(int(float(sizeStrings[3])) + margin * 2)
    return result
