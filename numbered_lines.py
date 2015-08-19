def insert_num (lines):
    with open("new.txt","a") as fwrite:
        for i in range(len(lines)):
            fwrite.write ( str(i+1) + " " + lines[i])
        
def main():

    with open("small.txt","rb") as f:
        lines = f.read().split('\r\n')
        
        print lines
    insert_num(lines)

main()
