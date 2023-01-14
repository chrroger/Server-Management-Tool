# Connection by ssh:
#### Actions on local server

    ssh_keygen -t rsa
 (install command: sudo apt-get install openssh-client)
> - Generating public/private rsa key pair.
> - Enter file in which to save the key (/home/roger/.ssh/id_rsa): (*just enter*)
> - Enter passphrase (empty for no passphrase):(passward need to remember).

    cat ~/.ssh/id_rsa.pub
> - copy all the texts(public key).

#### Actions on end client

    mkdir -p /home/user_name/.ssh && touch /home/user_name/.ssh/authorized_keys
> - Create ssh directory in the user’s home directory (as a sysadmin)
> - Keep in mind that you have to create these new directories and files in the end user’s home directory, not your own (root/sysadmin).

    vim /home/user_name/.ssh/authorized_keys
> - Now open this /home/user_name/.ssh/authorized_keys file with a text editor like Vim and add the public key of the user here.
> - Save and close the file.

    chmod 700 /home/user_name/.ssh && chmod 600 /home/user_name/.ssh/authorized_keys
> - make sure to set the correct file permissions.

    chown -R username:username /home/username/.ssh
> - You created those file with either root or your own admin accounts for some other user.
> - You need to change the ownership to the user.

    sudo service ssh start
    ifconfig
> - run above command to check ip address if not works run the below one:
    
    ip a

#### Back to Local server to Connect client

    ssh username@ip_address
> - get log into the client server

Tips:
> When first add to the server -- messages showed below
__The authenticity of host 'host(host)' can't be established.
ECDSA key fingerprint is SHA256:pDvm6T11wXn1OIJRWBq7OWHEqIMJxrWBjpwGGLSuci0.
Are you sure you want to continue connecting (yes/no)?__
>> - Choose 'yes'

> Then shows:
__Warning: Permanently added '192.168.254.128' (ECDSA) to the list of known hosts.
Enter passphrase for key '/home/roger/.ssh/id_rsa':__
- the password entered after asked for the key

[helper reference](https://linuxhandbook.com/add-ssh-public-key-to-server/amp/)
