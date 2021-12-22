def is_real(n):
    try:
        result = n == float(n)
        return result
    except ValueError:
        return False

def biquad_roots(a, b = 0, c = 0):
    assert is_real(a)
    assert is_real(b)
    assert is_real(c)
    D = b**2 - 4 * a * c
    qroots = []
    if D < 0 or a == 0:
        return []
    else:
        qroots.append((-b + D**0.5) / (2 * a))
        qroots.append((-b - D**0.5) / (2 * a))
        biqroots = []
        for qroot in qroots:
            if qroot < 0:
                continue
            biqroot = qroot**0.5
            if biqroot not in biqroots:
                biqroots.append(biqroot)
            if -biqroot not in biqroots:
                biqroots.append(-biqroot)
        return sorted(biqroots)

if __name__ == '__main__':
    print(biquad_roots(1))
    