def enlargeViewboxSize(viewbox, margin):
    '''
    Enlarges the viewbox string by a certain margin.
    example usage:
    vb = enlargeViewboxSize('0 0 48 30', 10)
    '''

    sizeStrings = viewbox.split()
    result = ''
    result += str(int(sizeStrings[0]) - margin) + ' '
    result += str(int(sizeStrings[1]) - margin) + ' '
    result += str(int(sizeStrings[2]) + margin) + ' '
    result += str(int(sizeStrings[3]) + margin)
    return result
