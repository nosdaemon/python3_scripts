from sshtunnel import SSHTunnelForwarder
from time import sleep

remote_host = [host]
remote_user = [username]
remote_pwrd = [password]

with SSHTunnelForwarder(
    (remote_host, 22),
        ssh_username=remote_user,
        ssh_password=remote_pwrd,
        remote_bind_address=('127.0.0.1', 3306),
        local_bind_address=('0.0.0.0', 10022)) as server:

    print(server.local_bind_port)

    while True:
        # press Ctrl-C for stopping
        sleep(1)

print('FINISH!')
