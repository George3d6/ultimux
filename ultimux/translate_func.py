from dill.source import getsource
from collections import Counter


def func_to_file(fup, fin):
    source = getsource(fup)
    executable = 'import sys\n\n' + source

    call = source.split('(')[0]
    nr_args = Counter(source.split(')')[0])[',']

    for char in ['d','e','f',' ']:
        call = call.rstrip(char)

    sys_args = []
    for i in range(1, nr_args + 1):
        sys_args.append(f'sys.argv[{i}]')

    call = call + '(' + ','.join(sys_args) + ')'
    
    executable += f'\n{call}'

    with open(fin, 'w') as fip:
        fip.write(source)
