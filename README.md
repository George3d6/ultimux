# Ultimux

Because multiprocessing is boring.

Did you ever lament python multiprocessing's difficulty of usage?

`join`,`close`,`start`, individual processes, polls, fork vs spawn, asyncio wrappers... please stop. There must be a  better way forward.

Of course there is, the revelation came to me in late November 2019 as the result of a (two) [3 year old 11.5% ABV porter](https://www.ratebeer.com/Ratings/Beer/Beer-Ratings.asp?BeerID=501180). Just launch your file or function in a tmux and leave it running!

In all honesty, I should say, this joke is inspired by a coding pattern I did use for ease of debugging, where I would leave long-running tasks running in a tmux and then connect to them accordingly in order to stop and fiddle with the process. It's strange what happens when gdb and desperation come together late at night.

## Interface & Usage

The library exposes a single function: `fire_and_forget`.
Installation can be done via pip: `pip install ultimux`.

### Running a file

Write a self-contained python script, on my computer this will be `/home/moron/my_task.py`.

The execute the code:
```
from ultimux import fire_and_forget

fire_and_forget(runnable='/home/moron/my_task.py', args=['a list of', 'whatever args your script', 'needs'], python_interpreter='python3', id='my_tmux_session')
```

And now, while your file is running, you can connect to the session via tmux `tmux a -t my_tmux_session`. The session will be closed once the script is done running.

### Running a function

Define a function that is self-contained, i.e doesn't use any variables (including imports) from the external scope, then pass it as the runnable. For example:

```
def a_task(arg1):
  import time
  time.sleep(5)
  print(f'I am doing something with {arg1}')
  time.sleep(5)

fire_and_forget(runnable=a_task, args=[2898], id='tmux_running_a_task')
```

Again, you can now connect to the tmux as `tmux a -t tmux_running_a_task`

### The interface

The only function exposed is `fire_and_forget`, it has the following args & default values:
* `runnable` - Mandatory - path to the file or pointer to the function that you want to execute
* `args` - Default: `[]` - array of arguments for your script or function
* `id` - Default: randomly generate uuid - id of the tmux session
* `python_interpreter` - Default: `python`
* `tmux_executable` - Default: `tmux`
* `I_dont_like_fun` - Default: `False` - Optional argument for boring people that disables some of the more stupid functionality of this library (e.g. the reckless function -> file conversion and using `os.system` instead of `subprocess`), I don't recommend turning this on, it spoils the spirit of the whole afair.

## Contributing

Contributions are allowed, but certain code quality guidelines should be observed and will be strictly enforced at PR time:
* Minimal testing, preferably none, unit testing prohibited
* Inconsistent variable naming schema, preference for overly long names or 2-3 char variables. Prefer puns, inside jokes and funny sounds to expressive naming.
* Proof of added complexity and lines of code with little to no benefit in terms of functionality.

Current critical contributions I'd appreciate:
* Documentation, strictly in the form of a "multiprocessing vs tmux" picture using the "virgin vs chad" meme format.
* Support for capturing outside context of a function.
* Support for names arguments.
* Better support for `i_dont_like_fun` mode.
* Humorous spelling errors and puns for exception messages.
* Support for screen (note: with condescending message about tmux being better, ideally print half of it as stdout and half of it as stderr).

## Questions

* I have used this library in production, am I a bad person?
[Complicated](https://en.wikipedia.org/wiki/Moral_relativism)

* Have you ever used this?
No, but I actually do use a similar coding pattern in places and you'd be surprised how convenient it is. I'm not even kidding.
