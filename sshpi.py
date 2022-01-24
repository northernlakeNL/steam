from fabric import Connection

def ledbalk(voortgang):  # voortgang is % achievements
    try:
        with Connection('swaggerlord.ooguy.com', user='pi', connect_kwargs={"password": "coolcool"}) as c:
            PID = c.run('pgrep -f matrix.py', warn=True, hide=True).stdout.strip()
            if PID:
                c.run(f'kill {PID}', warn=True)
        with Connection('swaggerlord.ooguy.com', user='pi', connect_kwargs={"password": "coolcool"}) as c:
            c.run(f'python3 /home/pi/matrix.py -p {voortgang}')
    except TimeoutError:
        "lol"


def vrienddisplay(naam):
    try:
        with Connection('swaggerlord.ooguy.com', user='pi', connect_kwargs={"password": "coolcool"}) as c:
            PID = c.run('pgrep -f friend.py', warn=True, hide=True).stdout.strip()
            if PID:
                c.run(f'kill {PID}', warn=True)
        with Connection('swaggerlord.ooguy.com', user='pi', connect_kwargs={"password": "coolcool"}) as c:
            c.run(f'python3 /home/pi/hd44780/friend.py -n "{naam}"')
    except TimeoutError:
        "lol"