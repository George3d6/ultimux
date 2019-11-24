from ultimux import fire_and_forget
import time

def pure_func(arg1, arg2):
    print(f'I am a pure function with arguments: {arg1} and {arg2} ')
    time.sleep(2)
    eixt(22)

python_file = 'tests/integration/ressources/test.py'


for i, runnable in enumerate([pure_func, python_file]):
    fire_and_forget(runnable=runnable, args=['STRING NUMBER 1', '2'], id=f'tmux nr {i + 1}', python_interpreter='/usr/bin/python3', tmux_executable='/usr/bin/tmux')
