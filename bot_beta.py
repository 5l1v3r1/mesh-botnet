import socket, getpass, random, platform, uuid, signal, time, os, sys, urllib2, unicodedata, json
from subprocess import Popen, PIPE, STDOUT
from time import strftime, sleep

version = "BETA1.0"

server = 'irc.freenode.net'
port = 6667
channel = '##medusa'
admin = 'thesquash'
nick = "TESTBOT"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

recv = irc.recv(4096)
log("[+] Recieved:    ", recv+'\n')

irc.send('NICK %s\r\n' % nick )
irc.send('USER %s %s %s :%s\r\n' % (nick, nick, nick, nick))
irc.send('JOIN %s\r\n' % channel)

data = ""

while True:
    data = irc.recv(4096)
    print data