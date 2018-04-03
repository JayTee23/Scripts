#!/usr/bin/python
########################################################
# Pre-requisite steps:
#   sudo pip install websocket-client
# Info:
#   Connect to a websocket API URL and check for required response
# Example:
#   websocket_api_monitor.py -w ws://api.jason.co.uk -s Welcome
########################################################

from websocket import create_connection
import sys, getopt

def main(argv):

  global websocketURL
  websocketURL = ''
  global searchString
  searchString = ''

  try:
    opts, args = getopt.getopt(argv, "hw:s:",["help", "wsurl=", "string="])
  except getopt.GetoptError:
    print 'websocket_api_monitor.py --wsurl <websocketURL> --string <searchString>\nor\nwebsocket_api_monitor.py -w <websocketURL> -s <searchString>\nExample\n\twebsocket_api_monitor.py -w ws://api.jason.co.uk -s Welcome'
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('-h', '--help'):
      print 'websocket_api_monitor.py --wsurl <websocketURL> --string <searchString>\nor\nwebsocket_api_monitor.py -w <websocketURL> -s <searchString>\nExample\n\twebsocket_api_monitor.py -w ws://api.jason.co.uk -s Welcome'
      sys.exit()
    elif opt in ("-w", "--wsurl"):
      websocketURL = arg
    elif opt in ("-s", "--string"):
      searchString = arg

  print 'Websocket URL is :', websocketURL
  print 'Search String is :', searchString

if __name__ == "__main__":
  main(sys.argv[1:])

  ws = create_connection(websocketURL)

  #print "Sending 'Hello, World'..."
  #ws.send("Hello, World")
  #print "Sent"
  #print "Receiving..."
  result =  ws.recv()

  print "Received '%s'" % result
  ws.close()
