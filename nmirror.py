#!/usr/bin/env python3

from proxy import Proxy
import threading
import time
import sys
import os
import argparse

# default values
BUFFER_SIZE=1024
MAX_CLIENTS=10000
TIMEOUT=60

VERSION='0.0.1'

def main():
  parser=argparse.ArgumentParser(
    prog='nmirror',
    description='''A simple TCP server that listens
for incoming connections on a specified host and
port. When a client connects, it establishes
a connection to the target host and port, and then
echoes all data received from the client to the
target host and vice versa.''')
  parser.add_argument(
    '-l',
    '--host',
    type=str,
    required=True,
    help='host address to listen on')
  parser.add_argument(
    '-p',
    '--port',
    type=int,
    required=True,
    help='hort number to listen on')
  parser.add_argument(
    '-L',
    '--target-host',
    type=str,
    required=True,
    help='target service host to forward traffic to')
  parser.add_argument(
    '-P',
    '--target-port',
    type=int,
    required=True,
    help='target service port to forward traffic to')
  parser.add_argument(
    '-b',
    '--buffer-size',
    type=int,
    default=BUFFER_SIZE,
    help='''maximum number of bytes for each recv/send
operation (default: %(default)s)''')
  parser.add_argument(
    '-c',
    '--max-clients',
    type=int,
    default=MAX_CLIENTS,
    help='''maximum number of clients that can connect
simultaneously (default: %(default)s)''')
  parser.add_argument(
    '-t',
    '--timeout',
    type=float,
    default=TIMEOUT,
    help='''number of seconds to wait for recv/send
operations before giving up on connections
(default: %(default)s)''')
  parser.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s ' + VERSION)
  args=parser.parse_args()
  proxy=Proxy(host=args.host, port=args.port,
    target_host=args.target_host,
    target_port=args.target_port,
    timeout=args.timeout, max_clients=args.max_clients,
    buffer_size=args.buffer_size)
  proxy.start()
  while True:
    print(f"Thread count: {threading.active_count()}")
    time.sleep(1)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Goodbye!')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)