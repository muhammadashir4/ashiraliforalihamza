import sys



def main():

    f = open(sys.argv[1])
    T = int(f.readline())

    tribe = {}
    p = {}

    for i in range(0, T):
        N = int(f.readline())
        for l in range(0, N):
            line = f.readline()
            line = line.split()
            tb = line.pop(0)
            name = ' '.join(line)

            if name in p:
                pass
            else:
                p[name] = 1
                if tb in tribe:
                    tribe[tb] += 1
                else:
                    tribe[tb] = 1

        for key in tribe.keys():
            print(key + ": " + str(tribe[key]))

main()
            
                
            
            
