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


<<<<<<< HEAD
def gamedisplay(game, account, achievements=0):  # game is game naam, account is account naanm
=======
def vrienddisplay(naam):  # naam is naam :)
>>>>>>> f72c575f83dc5f9b9959197ea50c4da490f245f2
    try:
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
            PID = c.run('pgrep -f friend.py', warn=True, hide=True).stdout.strip()
            if PID:
                c.run(f'kill {PID}', warn=True)
        with Connection('dnsmies.ooguy.com', user='pi', connect_kwargs={"password": "Roots"}) as c:
<<<<<<< HEAD
            c.run(f'python3 /home/pi/hd44780/game.py -g "{game}" -a {account} -c {achievements}')
    except TimeoutError:
        "lol"



=======
            c.run(f'python3 /home/pi/hd44780/wave.py')
            c.run(f'python3 /home/pi/hd44780/friend.py -n "{naam}"')
    except TimeoutError:
        "lol"

>>>>>>> f72c575f83dc5f9b9959197ea50c4da490f245f2
