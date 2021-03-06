#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for pyddq.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""
from __future__ import print_function, absolute_import, division
from mock import Mock
import sys

sys.modules["pyspark"] = Mock()

import pytest
