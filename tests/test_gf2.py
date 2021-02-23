"""
A pytest module to test classes/functions in galois/gf2.py.
"""
import pytest
import numpy as np

import galois

from .data import gf2_lut as LUT


class TestInstantiation:
    def test_list_int(self):
        v = [0,1,0,1]
        a = galois.GF2(v)
        check_array(a)

    def test_list_int_out_of_range(self):
        v = [0,1,0,2]
        with pytest.raises(AssertionError):
            a = galois.GF2(v)
        v = [0,1,0,-1]
        with pytest.raises(AssertionError):
            a = galois.GF2(v)

    def test_list_float(self):
        v = [0.1, 1.2, 0.1, 1.2]
        with pytest.raises(AssertionError):
            a = galois.GF2(v)

    def test_array_int(self):
        v = np.array([0,1,0,1])
        a = galois.GF2(v)
        check_array(a)

    def test_array_int_out_of_range(self):
        v = np.array([0,1,0,2])
        with pytest.raises(AssertionError):
            a = galois.GF2(v)
        v = np.array([0,1,0,-1])
        with pytest.raises(AssertionError):
            a = galois.GF2(v)

    def test_array_float(self):
        v = np.array([0.1, 1.2, 0.1, 1.2])
        with pytest.raises(AssertionError):
            a = galois.GF2(v)

    def test_zeros(self):
        a = galois.GF2.Zeros(10)
        assert np.all(a == 0)
        check_array(a)

    def test_ones(self):
        a = galois.GF2.Ones(10)
        assert np.all(a == 1)
        check_array(a)

    def test_random(self):
        a = galois.GF2.Random(10)
        assert np.all(a >= 0) and np.all(a < galois.GF2.order)
        check_array(a)

    def test_random_element(self):
        a = galois.GF2.Random()
        assert 0 <= a < galois.GF2.order
        assert a.ndim == 0
        check_array(a)


class TestArithmetic:
    def test_lut_add(self):
        a = LUT.X1 + LUT.Y1
        assert np.all(a == LUT.ADD)
        check_array(a)

    def test_lut_sub(self):
        a = LUT.X1 - LUT.Y1
        assert np.all(a == LUT.SUB)
        check_array(a)

    def test_lut_mul(self):
        a = LUT.X1 * LUT.Y1
        assert np.all(a == LUT.MUL)
        check_array(a)

    def test_lut_div(self):
        a = LUT.X2 / LUT.Y2
        assert np.all(a == LUT.DIV)
        check_array(a)

    def test_lut_neg(self):
        a = -LUT.X
        assert np.all(a == LUT.NEG)
        check_array(a)

    def test_lut_sqr(self):
        a = LUT.X ** 2
        assert np.all(a == LUT.SQR)
        check_array(a)

    def test_lut_pwr_3(self):
        a = LUT.X ** 3
        assert np.all(a == LUT.PWR_3)
        check_array(a)

    def test_lut_pwr_8(self):
        a = LUT.X ** 8
        assert np.all(a == LUT.PWR_8)
        check_array(a)

    def test_lut_log(self):
        a = np.log(LUT.X)
        assert np.all(a == LUT.LOG)

    def test_scalar_int_return_type(self):
        shape = ()
        ndim = 0
        a = galois.GF2.Random(shape)
        b = 1
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape
        c = b + a
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_vector_int_return_type(self):
        shape = (10,)
        ndim = 1
        a = galois.GF2.Random(shape)
        b = 1
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape
        c = b + a
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_matrix_int_return_type(self):
        shape = (10,10)
        ndim = 2
        a = galois.GF2.Random(shape)
        b = 1
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape
        c = b + a
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_scalar_scalar_return_type(self):
        shape = ()
        ndim = 0
        a = galois.GF2.Random(shape)
        b = galois.GF2.Random(shape)
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_vector_vector_return_type(self):
        shape = (10,)
        ndim = 1
        a = galois.GF2.Random(shape)
        b = galois.GF2.Random(shape)
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_matrix_matrix_return_type(self):
        shape = (10,10)
        ndim = 2
        a = galois.GF2.Random(shape)
        b = galois.GF2.Random(shape)
        c = a + b
        assert type(c) is galois.GF2
        assert c.ndim == ndim
        assert c.shape == shape

    def test_scalar_int_out_of_range(self):
        shape = ()
        a = galois.GF2.Random(shape)
        b = 2
        with pytest.raises(AssertionError):
            c = a + b
        with pytest.raises(AssertionError):
            c = b + a

    def test_vector_int_out_of_range(self):
        shape = (10,)
        a = galois.GF2.Random(shape)
        b = 2
        with pytest.raises(AssertionError):
            c = a + b
        with pytest.raises(AssertionError):
            c = b + a

    def test_matrix_int_out_of_range(self):
        shape = (10,10)
        a = galois.GF2.Random(shape)
        b = 2
        with pytest.raises(AssertionError):
            c = a + b
        with pytest.raises(AssertionError):
            c = b + a

    def test_scalar_scalar_out_of_range(self):
        shape = ()
        a = galois.GF2.Random(shape)
        b = 2*np.ones(shape, dtype=int)
        with pytest.raises(AssertionError):
            c = a + b
        # TODO: Can't figure out how to make this fail
        # with pytest.raises(AssertionError):
        #     c = b + a

    def test_vector_vector_out_of_range(self):
        shape = (10,)
        a = galois.GF2.Random(shape)
        b = 2*np.ones(shape, dtype=int)
        with pytest.raises(AssertionError):
            c = a + b
        with pytest.raises(AssertionError):
            c = b + a

    def test_matrix_matrix_out_of_range(self):
        shape = (10,10)
        a = galois.GF2.Random(shape)
        b = 2*np.ones(shape, dtype=int)
        with pytest.raises(AssertionError):
            c = a + b
        with pytest.raises(AssertionError):
            c = b + a


def check_array(array):
    assert type(array) is galois.GF2
    assert array.characteristic == 2
    assert array.power == 1
    assert array.order == 2
    # assert array.prim_poly == ?
    assert array.dtype == np.uint8