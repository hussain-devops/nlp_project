text = """This is a test of the column formatting system.""".splitlines()


def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw


size = terminal_size()/2

maxlen = max(size for s in text)
colwidth = maxlen +2

print '+' + '-'*colwidth + '+'
for s in text:
    print '| '+ " "*size +" |"
    print '| %-*.*s |' % (maxlen, maxlen, s)
    print '| '+ " "*size +" |"
print '+' + '-'*colwidth + '+'



