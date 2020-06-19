def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        # Creates a buffer of 10k bytes. Pretty small for modern systems
        # You don't want this too large however in case the system runs out of memory
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone')


if __name__ == '__main__': main()
