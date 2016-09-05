import argparse
import ipaddress
import requests
import getpass
import json
import time


parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host",
                    help="IP address of the Tweetcool server",
                    default='127.0.0.1')  # Equals 'localhost'
parser.add_argument("-P", "--port",
                    help="Post used by the Tweetcool server",
                    type=int,
                    default=9876)
args = parser.parse_args()

try:
    server = {
        'host': ipaddress.ip_address(args.host),
        'port': args.port
    }
except ValueError as e:
    print('The given host is not a valid IP address')
    exit(0)

if not(1024 < server["port"] < 65535):
    print('The given port number is not in the range between 1024 and 65535!')
    exit(0)

server["address"] = 'http://' + server["host"].compressed + ':' + str(server["port"])

# Logic starts here... somewhere..

print("-----------------------T W E E T C O O L-----------------------\n")

while True:
    try:
        r = requests.get(server['address'] + '/tweet')
        for element in r.json():
            print(('\nID:'), element['id'], ('\nPoster: '), element['poster'], ('\nContent: '), element['content'],
                  ('\nTimestamp: '), element['timestamp'])

        # Choose an option: Tweet, refresh, exit
        print('\n------------------M E N U------------------\n')
        option = input('Tweet\nRefresh\nExit\nChoose an option: ').lower()
        if option == "exit":
            exit()
        elif option == "refresh":
            continue
        else:
            name = input('Your name: ')
            message = input('Your message: ')
            r = requests.post(server['address'] + '/tweet', json={'poster': name, 'content': message})
    except EOFError:
        exit()
