#!/usr/bin/python2
import sys
if len(sys.argv) < 4:
    print("invalid arguments, use:")
    print("carve input start end output")
    print("carve input.txt 50.3 70.3 output.txt")
    exit(-1)
curpos=0
curPC=0.0
with open(sys.argv[1],"rb") as src:
    with open(sys.argv[4],"wb") as dest:
        beginPC=float(sys.argv[2])
        beginF=beginPC/100
        endPC=float(sys.argv[3])
        endF=endPC/100

        src.seek(0,2)                 # seek to end of file
        srcSize = src.tell()
        print (str.format("file {1} size:{0}", str(srcSize), sys.argv[1]));

        pos = int(srcSize * (beginF));
        # print( "seek to:" + str(pos))
        src.seek(pos)

        # Now seek forward until beginning of file or we get a \n
        while True:
            src.seek(-2,1)
            ch = src.read(1)
            if ch==b'\n': break
            if src.tell()==1: break

        while True:
            dest.write(src.readline())
            curpos = src.tell();
            curPC = curpos / srcSize * 100
            if ( curPC > endPC): break