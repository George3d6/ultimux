from dill.source import getsource
from collections import Counter


def func_to_file(fup, fin):
    source = getsource(fup)
    executable = 'import sys\n\n' + source

    call = source.split('(')[0]

    for char in ['d','e','f',' ']:
        call = call.lstrip(char)

    call = call + '(*sys.argv[1:])'
    executable += f'\n{call}\n'

    with open(fin, 'w') as fip:
        fip.write(executable)
