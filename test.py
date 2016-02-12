from dont_argue import supply_args

@supply_args('foo', 'bar', my_key=42, another_key='default value')
def main(foo, bar, my_key, another_key):
    print 'Foo:', foo
    print 'Bar:', bar
    print 'my_key', my_key
    print 'another_key', another_key

main()
