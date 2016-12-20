#! /usr/bin/env python

import socket
import os

KILL_PORT = 6666

NUMBER = 1

container_name = 'client' + str(NUMBER)

kill_command = "docker stop " + container_name

def launch_container():
	launch_command = "docker run -d -P --name " + str(container_name) + " 571106538810.dkr.ecr.us-west-2.amazonaws.com/gopshyam/amazonlinux:test python /home/FTC_Project/replica_socket.py " + str(NUMBER) 
	os.system(launch_command)

def listen_for_signal():
	kill_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	kill_listener.bind(('', KILL_PORT))

	kill_listener.listen(6)
	while(True):
		send_sock, addr = kill_listener.accept()
		message = send_sock.recv(40)
		if 'KILL' in message:
			os.system(kill_container)
			launch_container()

launch_container()

listen_for_signal()
