#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parmetrize('a', [1, 2, 3])
@pytest.mark.parmetrize('b', [4, 5, 6])
@pytest.mark.parmetrize('c', [7, 8, 9])
def test_parm(a, b, c):
    print(a, b, c)
