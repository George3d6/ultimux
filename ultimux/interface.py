import uuid
import os
import sys
import types

from ultimux.translate_func import func_to_file


def fire_and_forget(runnable, args=[], id=None, python_interpreter='python', tmux_executable='tmux', I_dont_like_fun=False):
    id = id.replace(' ', '_')

    if sys.platform in ['win32','cygwin','windows']:
        raise OSError('Only runs on real operating systems.')

    STORAGE_DIR = os.path.join(os.path.expanduser('~'), '.cache', 'ultimux')
    os.makedirs(STORAGE_DIR, exist_ok=True, mode = 0o777)

    if id is None:
        id = str(uuid.uuid1()).replace('-','_')

    py_file_name = os.path.join(STORAGE_DIR,f'{id}.py')

    if type(runnable) == types.FunctionType:
        runnable = func_to_file(runnable, py_file_name)
    elif os.path.isfile(runnable):
        with open(py_file_name, 'w') as wfp:
            with open(runnable, 'r') as rfp:
                wfp.write(rfp.read())
    elif type(runnable) == str and not I_dont_like_fun:
        with open(py_file_name, 'w') as fp:
            fp.write(runnable)
    else:
        raise ValueError('I don\'t what you passed as a `runnable`, try a python file or function')

    arg_str = ' '.join(['"' + str(x) + '"' for x in args])
    os.system(f'chmod +x {py_file_name}')
    if I_dont_like_fun:
        raise Exception('Subprocess usage not yet implemented !')
    else:
        os.system(f'tmux new-session -d -s {id}; tmux send-keys \'{python_interpreter} {py_file_name} {arg_str} && rm {py_file_name} && tmux kill-session -t {id}\' C-m; tmux detach -s {id};')





    ifn = str(uuid.uuid1()).replace('-','') + '.sh'
