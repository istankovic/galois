"""
A pytest module to test BCH encoding.

Test vectors generated from Octave with bchpoly().

References
----------
* https://octave.sourceforge.io/communications/function/bchpoly.html
"""
import pytest
import numpy as np

import galois


def test_15_7():
    """
    g = bchpoly(15, 7)
    bchenco(M, 15, 7, g, 'end')
    """
    n, k = 15, 7
    bch = galois.BCH(n, k)
    M = galois.GF2([
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0],
    ])
    C_truth = galois.GF2([
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    ])

    C = bch.encode(M)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth)

    C = bch.encode(M, parity_only=True)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth[:, k:])

    C = bch.encode(M.view(np.ndarray))
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth)

    C = bch.encode(M.view(np.ndarray), parity_only=True)
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth[:, k:])


def test_15_7_diff_primitive_poly():
    """
    g = bchpoly(15, 7, 25)
    bchenco(M, 15, 7, g, 'end')
    """
    n, k = 15, 7
    p = galois.Poly.Degrees([4, 3, 0])  # galois.primitive_poly(2, 4, method="largest")
    bch = galois.BCH(n, k, primitive_poly=p)
    M = galois.GF2([
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0],
    ])
    C_truth = galois.GF2([
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    ])

    C = bch.encode(M)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth)

    C = bch.encode(M, parity_only=True)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth[:, k:])

    C = bch.encode(M.view(np.ndarray))
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth)

    C = bch.encode(M.view(np.ndarray), parity_only=True)
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth[:, k:])


def test_15_7_systematic():
    n, k = 15, 7
    bch = galois.BCH(n, k, systematic=True)
    m = galois.GF2.Random(k)
    c_truth = galois.GF2.Zeros(n)
    c_truth[0:k] = m
    r_poly = (galois.Poly(m) * galois.Poly.Degrees([n-k])) % bch.generator_poly
    c_truth[-r_poly.coeffs.size:] = -r_poly.coeffs

    c = bch.encode(m)
    assert type(c) is galois.GF2
    assert np.array_equal(c, c_truth)

    c = bch.encode(m, parity_only=True)
    assert type(c) is galois.GF2
    assert np.array_equal(c, c_truth[k:])

    c = bch.encode(m.view(np.ndarray))
    assert type(c) is np.ndarray
    assert np.array_equal(c, c_truth)

    c = bch.encode(m.view(np.ndarray), parity_only=True)
    assert type(c) is np.ndarray
    assert np.array_equal(c, c_truth[k:])


def test_15_7_non_systematic():
    n, k = 15, 7
    bch = galois.BCH(n, k, systematic=False)
    m = galois.GF2.Random(k)
    c_poly = galois.Poly(m) * bch.generator_poly
    c_truth = galois.GF2.Zeros(n)
    c_truth[-c_poly.coeffs.size:] = c_poly.coeffs

    c = bch.encode(m)
    assert type(c) is galois.GF2
    assert np.array_equal(c, c_truth)

    with pytest.raises(ValueError):
        c = bch.encode(m, parity_only=True)

    c = bch.encode(m.view(np.ndarray))
    assert type(c) is np.ndarray
    assert np.array_equal(c, c_truth)

    with pytest.raises(ValueError):
        c = bch.encode(m.view(np.ndarray), parity_only=True)


def test_31_21():
    """
    g = bchpoly(31, 21)
    bchenco(M, 31, 21, g, 'end')
    """
    n, k = 31, 21
    bch = galois.BCH(n, k)
    M = galois.GF2([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    ])
    C_truth = galois.GF2([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    ])

    C = bch.encode(M)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth)

    C = bch.encode(M, parity_only=True)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth[:, k:])

    C = bch.encode(M.view(np.ndarray))
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth)

    C = bch.encode(M.view(np.ndarray), parity_only=True)
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth[:, k:])


def test_31_21_diff_primitive_poly():
    """
    g = bchpoly(31, 21, 61)
    bchenco(M, 31, 21, g, 'end')
    """
    n, k = 31, 21
    p = galois.Poly.Degrees([5, 4, 3, 2, 0])  # galois.primitive_poly(2, 5, method="largest")
    bch = galois.BCH(n, k, primitive_poly=p)
    M = galois.GF2([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    ])
    C_truth = galois.GF2([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    ])

    C = bch.encode(M)
    assert type(C) is galois.GF2
    assert np.array_equal(C, C_truth)

    C = bch.encode(M.view(np.ndarray))
    assert type(C) is np.ndarray
    assert np.array_equal(C, C_truth)


def test_31_21_non_systematic():
    n, k = 31, 21
    bch = galois.BCH(n, k, systematic=False)
    m = galois.GF2.Random(k)
    c_poly = galois.Poly(m) * bch.generator_poly
    c_truth = galois.GF2.Zeros(n)
    c_truth[-c_poly.coeffs.size:] = c_poly.coeffs

    c = bch.encode(m)
    assert type(c) is galois.GF2
    assert np.array_equal(c, c_truth)

    with pytest.raises(ValueError):
        c = bch.encode(m, parity_only=True)

    c = bch.encode(m.view(np.ndarray))
    assert type(c) is np.ndarray
    assert np.array_equal(c, c_truth)

    with pytest.raises(ValueError):
        c = bch.encode(m.view(np.ndarray), parity_only=True)