from math import e, factorial
import numpy as np

fac = np.vectorize(factorial)#本质是一个for循环，

def e_x(x, terms=10):
    """Approximates e^x using a given number of terms of
        the Maclaurin series
        """
    n = np.arange(terms)
    return np.sum((x ** n) / fac(n))

if __name__=="__main__":
    print("actual:", e ** 3) #Using e from the standard library

    print("N (terms)\tMaclaurin\tError")

    for n in range(1, 14):
        maclaurin = e_x(3, terms=n)
        print(f"{n}\t\t{maclaurin:.03f}\t\t{e ** 3 - maclaurin:.03f}")


