#!/bin/env python
# -*- coding: utf-8 -*-

import sys

import unittest

from address import Address


class TestAddress(unittest.TestCase):

    def test_init(self):
        index = u'123456'
        country = u'Российская Федерация'
        region = u'Московская область'
        subregion = u'Подольский район'
        settlement = u'Подольск'
        street = u'Малая'
        house = u'234'

        address = Address(
            index=index,
            country=country,
            region=region,
            subregion=subregion,
            settlement=settlement,
            street=street,
            house=house
        )

        expected = ','.join([
            index, country, region, subregion,
            settlement, street, house
        ])
        got = ','.join([
            address.index, address.country,
            address.region, address.subregion,
            address.settlement, address.street,
            address.house
        ])
        self.assertEqual(got, expected)

        address = Address()
        address.raw_address = expected + 'qwerty'
        self.assertEqual(address.raw_address, expected + 'qwerty')

        address = Address()
        address.index = index
        address.country = country
        address.region = region
        address.subregion = subregion
        address.settlement = settlement
        address.street = street
        address.house = house
        got = ','.join([
            address.index, address.country,
            address.region, address.subregion,
            address.settlement, address.street,
            address.house
        ])

        self.assertEqual(got, expected)

    def test___unicode__(self):
        index = u'123456'
        country = u'Российская Федерация'
        region = u'Московская область'
        subregion = u'Подольский район'
        settlement = u'Подольск'
        street = u'Малая'
        house = u'234'

        address = Address(
            index=index,
            country=country,
            region=region,
            subregion=subregion,
            settlement=settlement,
            street=street,
            house=house
        )

        # Index is deleted from the representation
        expected = ', '.join([
            country, region, subregion,
            settlement, street, house
        ])
        self.assertEqual(unicode(address), expected)

    def test_equal(self):
        addr1 = Address()
        addr2 = Address()
        self.assertEqual(addr1, addr2)

        for key, val in addr1.__dict__.iteritems():
            if key == 'strict':
                continue
            addr1.__dict__[key] = 'qwerty' + unicode(val)
            self.assertNotEqual(addr1, addr2)
            addr2.__dict__[key] = 'qwerty' + unicode(val)
            self.assertEqual(addr1, addr2)


if __name__ == '__main__':
    suite = unittest.makeSuite(TestAddress, 'test')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
