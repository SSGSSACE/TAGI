def readfirstcolumncsvfile(csvfile):
    """
    Reads the first column of a csv file and returns a list of strings.
    """
    with open(csvfile, 'r',encoding='utf-8-sig') as f:
        reader = f.readlines()
        return [row.split(',')[0] for row in reader]
a=readfirstcolumncsvfile('TEST1.csv')
print(a)
string="Nguyen Van B"
def checkastringinalist(list1,string):
    if string in a:
        print("yes")
        return True
    else:
        print("no")
        return False
checkastringinalist(a,string)
#check here