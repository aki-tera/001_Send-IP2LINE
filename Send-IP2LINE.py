import urllib.request
import requests


def get_ip_address():
    # グローバルIPアドレスを取得
    get_ip = urllib.request.urlopen('http://ipcheck.ieserver.net').read().decode('utf-8')
    return(get_ip)


def post_line(send_message):
    # LINE_notifyへ送る準備
    line_notify_token = 'LINEから入手したアクセストークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = 'IP:'+send_message
    payload = {'message': message}

    # 発行したトークン
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    # LINE_notifyへメッセージを送信
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)


def main():
    # IPアドレスを取得
    # IPアドレスの余計な改行を削除    
    ip=get_ip_address().rstrip()

    # IPアドレスをLINEへ送信
    post_line(ip)

    # 送信IPアドレスを確認
    print('今のIPアドレス：{}です。'.format(ip))



if __name__ == "__main__":
    main()
