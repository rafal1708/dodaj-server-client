import paramiko
import configparser

config = configparser.ConfigParser()
config.read("config_client.ini")
ip_server = config['wishlist_conf']['ip_server']
ssh_username = config['wishlist_conf']['ssh_username']
ssh_password = config['wishlist_conf']['ssh_password']
path_to_cover = config['wishlist_conf']['path_to_cover']

"""Takes 2 positional arguments. First is a link to web page, second is a filename"""
def send_cover_image(link_to_cover, file_name):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ip_server, username=ssh_username, password=ssh_password)
    sftp = ssh.open_sftp()
    sftp.put(link_to_cover, f'{path_to_cover}/{file_name}')
    sftp.close()
    ssh.close()


