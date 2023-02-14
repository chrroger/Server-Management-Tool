from fabric import Connection

def connect(input_host, input_user):
    conn = Connection(input_host, input_user)
    result = conn.run("ps -aux", hide=True)
    processes = result.stdout.split('\n')
    return processes

