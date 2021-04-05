from ultimux import fire_and_forget
import time

def pure_func(arg1, arg2):
    import time
    print(f'I am a self contained funcion: {arg1} and {arg2} ')
    with open('/tmp/1', 'w') as fp:
        fp.write(arg1)
    # Increase for debugging purposes
    time.sleep(2)
    eixt(22)

python_file = 'tests/integration/ressources/test.py'


for i, runnable in enumerate([pure_func, python_file]):
    fire_and_forget(runnable=runnable, args=['STRING NUMBER 1', '2'], id=f'tmux_nr_{i + 1}', python_interpreter='/usr/bin/python3', tmux_executable='/usr/bin/tmux')
    time.sleep(1)
    with open(f'/tmp/{i + 1}', 'r') as fp:
        content = fp.read()
        assert content == 'STRING NUMBER 1'
