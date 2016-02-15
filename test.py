import unittest

import dont_argue
supply_args = dont_argue.supply_args

class TestBasicUse(unittest.TestCase):
    def test_passes_arguments(self):
        dont_argue.test_args = ['one', 'two']
        @supply_args
        def main(one, two):
            self.assertEqual(one, 'one')
            self.assertEqual(two, 'two')
        main()

    def test_passes_arguments_with_splat(self):
        dont_argue.test_args = ['one', 'two', '3', '4']
        @supply_args
        def main(one, two, *args):
            self.assertEqual(one, 'one')
            self.assertEqual(two, 'two')
            self.assertTupleEqual(args, ('3', '4'))
        main()

    def test_passes_arguments_with_splat_and_named_args(self):
        dont_argue.test_args = ['a', 'b', 'c', 'd']
        @supply_args
        def main(a, b, *args):
            self.assertEqual(a, 'a')
            self.assertEqual(b, 'b')
            self.assertTupleEqual(args, ('c', 'd'))
        main()

    def test_keyword_args(self):
        dont_argue.test_args = ['--first', 'val', '--second=blah', 'a', 'b']
        @supply_args
        def main(a, b, first=None, second=None, third=42):
            self.assertEqual(a, 'a')
            self.assertEqual(b, 'b')
            self.assertEqual(first, 'val')
            self.assertEqual(second, 'blah')
            self.assertEqual(third, 42)
        main()

    def test_splat_args_with_keywords(self):
        dont_argue.test_args = ['1', '--two', '2', '3', '4', '5']
        @supply_args
        def main(one, two=42, *args):
            self.assertEqual(one, '1')
            self.assertEqual(two, '2')
            self.assertTupleEqual(args, ('3', '4', '5'))
        main()
