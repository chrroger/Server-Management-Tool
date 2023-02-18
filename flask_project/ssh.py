from fabric import Connection

def connect(input_host, input_user):
    conn = Connection(input_host, input_user)
    return conn

def processes(conn):
    result = conn.run("ps -aux", hide=True)
    ans = []
    processes = result.stdout.split('\n')
    # this specifies the number of splits, so the splitted lines
    # will have (nfields+1) elements
    nfields = len(processes[0].split()) - 1
    for row in processes[1:]:
        res = row.split(None, nfields)
        ans.append(res)
    ans.pop()
    return ans

def show_pids(ans):
    pids = []
    for i in ans:
        pids.append(i[1])
    return pids

def kill(conn, pid):
    conn.run("kill -9 {}".format(pid))