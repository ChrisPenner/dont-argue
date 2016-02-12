from dont_argue import supply_args

@supply_args('other', 'blah', 'kwarg')
def main(blah, other, kwarg):
    print 'blah: {}, other: {}, kwarg: {}'.format(blah, other, kwarg)

main()
