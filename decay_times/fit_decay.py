"""
compute an exponential decay fit to two vectors of x and y data
result is in form y = a + b * exp(c*x).
ref. https://gist.github.com/johanvdw/443a820a7f4ffa7e9f8997481d7ca8b3
"""
def exp_est(x,y):
    n = np.size(x)
    # sort the data into ascending x order
    y = y[np.argsort(x)]
    x = x[np.argsort(x)]
    
    Sk = np.zeros(n)
    
    for n in range(1,n):
        Sk[n] = Sk[n-1] + (y[n] + y[n-1])*(x[n]-x[n-1])/2
    dx = x - x[0]
    dy = y - y[0]
    
    m1 = np.matrix([[np.sum(dx**2), np.sum(dx*Sk)],
                    [np.sum(dx*Sk), np.sum(Sk**2)]])
    m2 = np.matrix([np.sum(dx*dy), np.sum(dy*Sk)])
    
    [d, c] = m1.I * m2.T

    m3 = np.matrix([[n,                  np.sum(np.exp(  c*x))],
                    [np.sum(np.exp(c*x)),np.sum(np.exp(2*c*x))]])
    
    m4 = np.matrix([np.sum(y), np.sum(y*np.exp(c*x).T)])

    [a, b] = m3.I * m4.T
    
    return [a.flat[0],b.flat[0],c.flat[0]]