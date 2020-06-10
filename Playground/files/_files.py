def main():
    # 'rt' and 'wt' are read/write modes, but not sure about the 't'
    # The use of with ... as f: pattern is known was a context manager. Useful here as we don't need to remember
    # to close the file after we're done using it. This is now done automatically.
    with open('lines.txt', 'rt') as infile:
        with open('lines-copy.txt', 'wt') as outfile:
            for line in infile:
                # Note: This is a little confusing still... What is rstrip() doing?
                # It would appear that by using file=outfile in the print function we are effectively 'writing'
                # to the file
                print(line.rstrip(), file=outfile)
                print('.', end='', flush=True)
    print('\ndone')


if __name__ == '__main__': main()
