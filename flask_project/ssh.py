from fabric import Connection

def connect(input_host, input_user):
    conn = Connection(input_host, input_user)
    input_cmd = input("Enter your command: ")
    conn.run(input_cmd, hide=True)