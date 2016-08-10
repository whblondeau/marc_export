import sys
'''This script opens the text file, which is passed as an argument, 
and coerces all line endings to Windows CRLF format. It does not
modify the input file; it creates a new file with the CRLF line endings,
whose name is the same as tthe input file, except for "_win" inserted
immediately before the final dot and filetype suffix.

If the file parameter contains binary rather than character data, 
results are not known.
'''

if len(sys.argv) < 2:
    print("Filename required.")
    sys.exit(0)
    
filename = sys.argv[1]
srcfile = open(filename)
srclines = srcfile.readlines()
srcfile.close()

destfilename = filename.split('.')
destfilename = '.'join(filename[:-1]) + '_win.' + filename[-1]
destfile = open(destfilename, 'w')
for line in srclines:
    destfile.write(line.rstrip() + '\r\n')
destfile.close()
