import urllib.request
import requests


def get_ip_address():
    """
    get your global IP address(IPv4)

    Parameters
    ----------

    Returns
    ----------
    get_ip:string
        string of IP address
    """
    get_ip = urllib.request.urlopen('http://ipcheck.ieserver.net').read().decode('utf-8')
    return(get_ip)


def post_line(send_message):
    """
    send message to LINE_notify

    Parameters
    ----------
    send_message:string
        string to send to LINE_notify

    Returns
    ---------
    """
    line_notify_token = 'Your access token'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = 'IP:'+send_message
    payload = {'message': message}

    #create headers
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    #send message
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)


def main():
    # get a string of your Ip address
    # and delete <LF> code from this string
    ip=get_ip_address().rstrip()

    #send IP address to LINE_notify
    post_line(ip)

    #display IP address on the screen
    print('Your IP address：{}'.format(ip))



if __name__ == "__main__":
    main()
