import math as m


def main () :
    while True :
        try : 
            num = input("Enter decimal number: ")
            break
        except NameError :
            print("Input was not a number")
        except SyntaxError :
            print("Input was not a number")
    
    integ = m.trunc(num)
    decim = num - integ

    decim_num = 0
    decim_den = 0

    low_num = 0
    low_den = 1
    high_num = 1
    high_den = 1

    for _ in range(1000) :
        mid_num = low_num + high_num
        mid_den = low_den + high_den
        mid = float(mid_num) / float(mid_den)

        if decim == mid :
            break
        elif decim < mid :
            high_num = mid_num
            high_den = mid_den
        elif decim > mid :
            low_num = mid_num
            low_den = mid_den

    decim_num = mid_num + (integ * mid_den)
    decim_den = mid_den

    print("Fraction: %i / %i" % (decim_num, decim_den))


if __name__ == "__main__" :
    main()