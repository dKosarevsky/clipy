
# filename = '/etc/passwd'

def countCli(fname):
    try:
        f = open(fname, 'r')
        text = f.read()
        f.close()
    except IOError:
        print(f'File {fname} not found')
        raise SystemExit

    num_lines = text.count('\n')

    list_words = text.split(None)
    num_words = len(list_words)

    num_chars = len(text)

    num_bytes = len(text.encode('utf-8'))

    print('Lines:', num_lines, 'Words:', num_words, 'Chars:', num_chars, 'Bytes:', num_bytes)


if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) >= 2:
        filename = str(sys.argv[1])
        countCli(filename)
    else:
        filename = None
        print('Not enough arguments!')
        sys.exit(0)
