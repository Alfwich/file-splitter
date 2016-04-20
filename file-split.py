import os, sys

def main():
    if len(sys.argv) < 2:
        print("useage: python file-split.py {source-file} '{search-string}'")
        return

    files = [[]]
    FILE = sys.argv[1]
    SEARCH_STRING = sys.argv[2]
    with open(FILE) as f:
        lines = f.readlines()
        for line in lines:
            if SEARCH_STRING in line:
                files.append([])
            files[-1].append(line)

        print("Will split file: %s into %d files" %(FILE, len(files)))
        userDec = raw_input("Do this(y/n)?").lower()

        if not userDec == "y":
            print("Aborting!")
            return

        for idx in xrange(len(files)):
            if not os.path.isdir("out"):
                os.mkdir("out")
            fileName = "out\%s.split.%d.txt" % (FILE, idx)
            sys.stdout.write("Writing file: '%s'..." % fileName)
            with open(fileName, "w") as g:
                for line in files[idx]:
                    g.write(line)
            print("Done.")

if __name__ == "__main__":
    main()
