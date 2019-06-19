import os
from io import BytesIO
import gzip
# import bz2

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

def bad_filename(filename):
    return repr(filename)[1:-1]

if __name__ == "__main__":
    print("============file path============")
    abspath = os.path.abspath('file/somefile.bin')
    directname = os.path.dirname('file/somefile.bin')
    base = os.path.basename(abspath)
    print('somefile.path:{}'.format(abspath))
    print('somefile.curpath:{}, current work dir:{}'.format(os.path.dirname(abspath), os.getcwd()))
    print('somefile.pardir:{}'.format(os.path.join(directname, os.path.pardir)))
    print('somefile.parname:{}'.format(os.path.abspath(os.path.join(directname, os.path.pardir))))
    print('base path:{}'.format(base))
    print('join path:{}'.format(os.path.join('tmp', 'data', base)))
    print('expanduser path:{}'.format(os.path.expanduser('~'+abspath)))
    print('splitext path:{}'.format(os.path.splitext(abspath)))

    print('isfile path:{}'.format(os.path.isfile(abspath)))
    print('isdir path:{}'.format(os.path.isdir(os.getcwd())))
    print('realpath path:{}'.format(os.path.realpath(os.getcwd())))
    print('path modify long time path:{}'.format(os.path.getmtime(os.getcwd())))
    import time
    print('path modify ctime path:{}'.format(time.ctime(os.path.getctime(os.getcwd()))))

    print("============write file ============")

    if not os.path.exists('somefile.bin'):
        with open('somefile.bin', 'wb') as f:
            text = 'hello world\nhi'
            f.write(text.encode('utf-8'))

        with open('somefile.bin', 'a') as f:
            f.writelines('writeline\nhihi')
            f.write('write txt\n')
    else:
        print('file already exists!!')


    print("============read file by os============")
    with open('somefile.bin', 'rb') as f:
        data = f.read(30)
        text = data.decode('utf-8')
        print('somefile.bin content is ', text)


    print("============read/write file by StringIO============")
    from io import StringIO
    f = StringIO()
    f.write('this is io write\n')
    f.write('this is io write2')
    # print('this is a test', file= f.getvalue())
    print('write result is ', f.getvalue())

    f = StringIO('hello\n hi\n groovy!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

    print("============read/write file by StringIO============")

    f = BytesIO()
    f.write('中午你'.encode('utf-8'))
    print('result is ', f.getvalue())
    f.write('中午你'.encode('gb2312'))
    print('result is ', f.getvalue())

    print("============read/write file by zip============")
    from datetime import datetime
    gzInfo = 'file/g.gz'
    aa = "时间：(%Y-%m-%d %H:%M:%S %f):", datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
    # print(format('aaa %x', aa))
    print('gzip write test;', aa)
    if os.path.exists(gzInfo):
        with gzip.open(gzInfo, 'rt') as g:
            print(g.read())
    else:
        with gzip.open(gzInfo, 'wt', compresslevel=8) as g:
            g.write('gzip write test;{}'.format(aa))


    xmlfilename = "file/xmldemo.xml"
    if os.path.exists(xmlfilename):
        print("============read all by readlines============")
        with open(xmlfilename,'rb') as f:
            print('all xml info:', f.readlines())
        print("============read all by for============")
        for line in open(xmlfilename, 'rb'):
            print(line)

        print("============read all by while============")
        f = open(xmlfilename)
        line = f.readline()
        while line:
            print(line, end='')
            line = f.readline()
    print("============read/write file by buffer============")
    filename = 'file/somefile.bin'
    newfilename = 'file/newsomefile.bin'
    if os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(b'buffer write line.\n')
            f.write(b'buffer1 write line.')
        buf = read_into_buffer(filename)
        buf[0:5] = b'hell '
        with open(newfilename, 'wb') as f:
            f.write(buf)
        with open(newfilename, 'rb') as f:
            print('all info:', f.readlines())

        bufsize = 32
        bufs = bytearray(bufsize)
        with open(filename, 'rb') as f:
            while True:
                n = f.readinto(bufs)
                if n < bufsize:
                    break
        print('bufs is ', bufs)

    print("============list file============")
    print(os.path.abspath(os.path.join(directname, os.path.pardir)))
    names = os.listdir(os.path.abspath(os.path.join(directname, os.path.pardir)))
    fnames = [name for name in names if name.endswith('.py')]
    for name in fnames:
        print('pyfile result', name)

    from fnmatch import fnmatch
    fnamesp = [name for name in names if not fnmatch(name, '*.py')]
    for name in fnamesp:
        print('not pyfile result:{},size:{},modifytime:{}'.format(name, os.path.getsize(name), time.ctime(os.path.getctime(name))))

    print("============pring bad filename============")
    badname = ' bäd.txt'
    try:
        print('bad filename:', badname)
    except UnicodeEncodeError:
        print(bad_filename(badname))

    print("============write char to buffer============")
    import sys
    sys.stdout.buffer.write(b'hello\n')
    sys.stdout.buffer.write(b'hello5\n')

    # print("============create temp file and folder============")
    # from tempfile import TemporaryFile
    # with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    #     f.write('create temp file\n')
    #     f.write('second line\n')
    #     #read
    #     f.seek(0)
    #     data = f.read()
    #     print('temp info:', data)
    #f = TemporaryFile('w+t')
    #f.write('another way to create temp file')
    #f.close()



