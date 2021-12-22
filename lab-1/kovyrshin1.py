from sys import argv

def input_float():
    ok = False
    while not ok:
        n = input()
        try:
            n = float(n)
            ok = True
        except:
            print('incorrect input')
            ok = False
    return n
    

def input_args():
    cs = [ 0 ]
    print('input args')
    for i in range(3):
        cs.append(input_float())
    return cs

    
def main():
    cs = argv
    if len(argv) < 4:
        cs.extend([0] * (4 - len(argv)))
    if len(cs) < 2:
        cs = input_args()
    else:
        cs[1] = float(cs[1])
        if len(cs) > 2:
            cs[2] = float(cs[2])
        if len(cs) > 3:
            cs[3] = float(cs[3])
    a, b, c = cs[1], cs[2], cs[3]
    D = b**2 - 4 * a * c
    qroots = []
    if D < 0 or a == 0:
        print('no roots')
    else:
        qroots.append((-b + D**0.5) / (2 * a))
        qroots.append((-b - D**0.5) / (2 * a))
        result = []
        for qroot in qroots:
            if qroot < 0:
                continue
            root = qroot**0.5
            if root not in result:
                result.append(root)
            if -root not in result:
                result.append(-root)
        print(sorted(result))

if __name__ == "__main__":
    main()
