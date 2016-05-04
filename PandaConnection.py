import paramiko
from scp import SCPClient

class PandaConnection:
    def __init__(self, hostname):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh.connect(hostname, username='dummy', password='123')
        except paramiko.SSHException:
            print "fail"

    def executeCommand(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)

        #Normal output
        for line in stdout.readlines():
            print line.strip()
        #Error output
        for line in stderr.readlines():
            print line.strip()

    # src and dst can be abs or relative path
    # dst is relative to home directory of the user
    def uploadFile(self, src, dst):
        scp = SCPClient(self.ssh.get_transport())
        scp.put(src, dst)

    def downloadFile(self, src):
        scp = SCPClient(self.ssh.get_transport())
        scp.get(src)

if __name__ == "__main__":
    panda = PandaConnection("192.168.56.101")
    panda.executeCommand("uptime")
    panda.uploadFile("README.md", "/home/dummy/abc.md")
    panda.downloadFile("abc.md")