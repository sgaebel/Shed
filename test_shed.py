#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for shed.

@author: Sebastian Gaebel
@email: sgaebel@star.sr.bham.ac.uk
"""

import shed
import time


def test_Timer_elapsed_time_against_sleep():
    with shed.Timer(verbose=False) as t:
        time.sleep(3.2)
    assert abs(t.dt - 3.2) < 0.1


def test_memory_size_messages():
    assert shed.memory_size(int(3.2e5), SI=False, template='{:.2f} {} ({} B)') == '312.50 kiB (320000 B)'
    assert shed.memory_size(int(3.2e5), SI=True, template='{:.2f} {} ({} B)') == '320.00 kB (320000 B)'
    assert shed.memory_size(int(1002), SI=False, template='{:.2f} {} ({} B)') == '1002 B'
    assert shed.memory_size(int(1002), SI=True, template='{:.2f} {} ({} B)') == '1.00 kB (1002 B)'
    assert shed.memory_size(int(4.9563e30), SI=False, template='{:.2f} {} ({} B)') == '4099755.27 YiB (4956299999999999787158399352832 B)'
    assert shed.memory_size(int(4.9563e30), SI=True, template='{:.2f} {} ({} B)') == '4956300.00 YB (4956299999999999787158399352832 B)'
    assert shed.memory_size(int(12), SI=False, template='{:.2f} {} ({} B)') == '12 B'
    assert shed.memory_size(int(12), SI=True, template='{:.2f} {} ({} B)') == '12 B'


if __name__ == '__main__':
    pass
