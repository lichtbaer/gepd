#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of gepd.
# https://github.com/lichtbaer/dawum

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, johannes <johannes@kampagnen.eu>

from preggy import expect

from gepd import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    """
    """
    def test_has_proper_version(self):
        """

        """
        expect(__version__).to_equal('0.0.1')
