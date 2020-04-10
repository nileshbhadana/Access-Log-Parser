import sys,math
from datetime import datetime


bytes=[]

def apache_output(line):
    split_line = line.split()
    time1=split_line[3][-8:]
    time2='10:40:00'
    t1=datetime.strptime(time1,"%H:%M:%S")
    t2=datetime.strptime(time2,"%H:%M:%S")
    if t1>t2 and "/phpMyAdmin" in split_line[6]:
        print(line)
        bytes.append(int(split_line[-1]))


def final_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
    total_bytes=int(math.fsum(bytes))
    print("Total Bytes = "+str(total_bytes))


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print ("You must specify a valid file to parse")
        print (__doc__)
        sys.exit(1)
    log_report = final_report(infile)
    #print (log_report)
    infile.close()
