'''
Copyright (c) 2017 VMware, Inc. All Rights Reserved.
SPDX-License-Identifier: BSD-2-Clause
'''

import unittest

from classes.package import Package
from classes.notice import Notice


class TestClassPackage(unittest.TestCase):

    def setUp(self):
        self.package = Package('x')

    def tearDown(self):
        del self.package

    def testInstance(self):
        self.assertEqual(self.package.name, 'x')
        self.assertEqual(self.package.version, '')
        self.assertFalse(self.package.src_url)
        self.assertFalse(self.package.license)
        self.assertFalse(self.package.notices)

    def testSetters(self):
        self.assertRaises(AttributeError, setattr, self.package, 'name', 'y')
        self.package.version = '1.0'
        self.assertEqual(self.package.version, '1.0')
        self.package.license = 'Apache 2.0'
        self.assertEqual(self.package.license, 'Apache 2.0')
        self.package.src_url = 'github.com'
        self.assertEqual(self.package.src_url, 'github.com')

    def testGetters(self):
        self.package.version = '1.0'
        self.package.license = 'Apache 2.0'
        self.package.src_url = 'github.com'
        self.assertEqual(self.package.name, 'x')
        self.assertEqual(self.package.version, '1.0')
        self.assertEqual(self.package.license, 'Apache 2.0')
        self.assertEqual(self.package.src_url, 'github.com')

    def testAddNotice(self):
        n = Notice()
        n.origin = 'FROM'
        n.message = 'no image'
        n.level = 'error'
        self.package.add_notice(n)
        self.assertEqual(len(self.package.notices), 1)
        self.assertEqual(self.package.notices[0].origin, 'FROM')

    def testToDict(self):
        self.package.version = '1.0'
        self.package.license = 'Apache 2.0'
        self.package.src_url = 'github.com'
        a_dict = self.package.to_dict()
        self.assertEqual(a_dict['name'], 'x')
        self.assertEqual(a_dict['version'], '1.0')
        self.assertEqual(a_dict['license'], 'Apache 2.0')
        self.assertEqual(a_dict['src_url'], 'github.com')


if __name__ == '__main__':
    unittest.main()
