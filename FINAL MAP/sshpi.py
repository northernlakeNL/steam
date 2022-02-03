from fabric import Connection


def ledbalk(voortgang):  # voortgang is % achievements
    try:
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
            PID = c.run('pgrep -f matrix.py', warn=True, hide=True).stdout.strip()
            if PID:
                c.run(f'kill {PID}', warn=True)
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
            c.run(f'python3 /home/pi/matrix.py -p {voortgang}')
    except TimeoutError:
        "lol"


def gamedisplay(game, account, achievements=0):  # game is game naam, account is account naanm
    try:
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
            PID = c.run('pgrep -f friend.py', warn=True, hide=True).stdout.strip()
            if PID:
                c.run(f'kill {PID}', warn=True)
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
            c.run(f'python3 /home/pi/hd44780/game.py -g "{game}" -a {account} -c {achievements}')
    except TimeoutError:
        "lol"



