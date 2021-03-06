#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_komoot():
    g = geocoder.komoot(location)
    assert g.ok
    assert len(g) == 1


def test_komoot_multi_result():
    g = geocoder.komoot(location, maxRows=3)
    assert g.ok
    assert len(g) == 3


def test_komoot_reverse():
    g = geocoder.komoot(ottawa, method='reverse')
    assert g.ok
