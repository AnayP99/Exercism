def rows(letter):
    size = ord(letter) - ord('A') + 1
    top_half = []
    for i in range(size):
        row = ''
        row += ' ' * (size-i-1)
        if i == 0:
            row += 'A'
        else:
            row += chr(ord('A')+i) + ' ' * (2*i-1) + chr(ord('A')+i)
        row += ' ' * (size-i-1)
        top_half.append(row)
    bottom_half = top_half[:-1][::-1]
    return top_half + bottom_half
