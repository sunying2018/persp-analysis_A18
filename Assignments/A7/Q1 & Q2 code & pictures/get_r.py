import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    assert alpha > 0 and alpha < 1, "alpha should between 0 and 1"
    assert delta >= 0 and delta < 1, "delta should between 0 and 1"
    assert Z > 0, "Z should lager than 0"

    r = alpha * Z * ( (L / K) ** (1 - alpha) ) - delta

    if (type(K) == float) and (type(L)== float):
        assert type(r)==float, "If K and L are both scalars,  the interest rate should be a scalar"

    if not np.isscalar(K) and not np.isscalar(L):
        assert not np.isscalar(r), "If K and L are both vectors, the interest rate should be a vector"
    
    return r