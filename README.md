
# Tor Simultaneous IP
Python3 script that creates multiple threads with different rotating IP.

## Details

The script is written to get several IP simultaneously, don't use it to hide malicious network traffic.
It causes Tor exit-node IP to get blocked and keeps other people from accessing websites.
Respect the volunteer network of relays that makes it possible to work.

The script is based on Threading, particularly optimized for tasks that spend much of their time waiting for external events like http requests. 

On average the total number of Tor "Exit" nodes is around 1000 at a given time, (see number of exit relays on [tor metrics](http://torstatus.blutmagie.de/#Stats)). The script will gets different Tor circuits at the same time but it may be possible that you end up having the same exit node for different ports (Same IP but on circuits with different middle relays).

## Requirements

### 1. Configure Tor
A thread connects to a Tor circuit with a particular port. Edit the configuration file "**torrc**" to add Tor circuits and restart Tor.
To run and configure Tor on :
+ [Linux](https://www.torproject.org/docs/tor-doc-unix.html.en)
+ [MacOSX](https://www.torproject.org/docs/tor-doc-osx.html.en)
+ [Windows](https://miloserdov.org/?p=1839) (to Install Tor as a service)

By default, in the python script 8 threads are created which requires 8 "SOCKSPort" lines in the configuration file.

```
SOCKSPort 9050
SOCKSPort 9060
SOCKSPort 9070
SOCKSPort 9080
SOCKSPort 9090
...

ControlPort 9051
ControlPort 9061
ControlPort 9071
ControlPort 9081
ControlPort 9091
...
```

If a password is needed by Tor, update the following variable:

```python
password = None # Replace with Tor Password
```

### 2. Python modules

Stem a Python module to interact with Tor

```
$ pip install stem
```

HTTP library 

```
$ pip install requests
```

## Usage

```
$ python3 process.py
13:57:43 - THREAD: 7 - PORT: 9120 - IP: 128.14.136.158
13:57:43 - THREAD: 6 - PORT: 9110 - IP: 87.118.110.27
13:57:43 - THREAD: 2 - PORT: 9070 - IP: 77.247.181.162
13:57:43 - THREAD: 1 - PORT: 9060 - IP: 85.248.227.165
13:57:44 - THREAD: 3 - PORT: 9080 - IP: 185.220.101.61
13:57:44 - THREAD: 0 - PORT: 9050 - IP: 23.129.64.185
13:57:44 - THREAD: 4 - PORT: 9090 - IP: 23.129.64.100
13:57:44 - THREAD: 5 - PORT: 9100 - IP: 185.220.101.33
13:57:54 - THREAD: 7 - PORT: 9120 - IP: 128.14.136.158
13:57:54 - THREAD: 2 - PORT: 9070 - IP: 77.247.181.162
13:57:54 - THREAD: 6 - PORT: 9110 - IP: 192.42.116.18
13:57:55 - THREAD: 1 - PORT: 9060 - IP: 185.220.101.30
13:57:55 - THREAD: 0 - PORT: 9050 - IP: 23.129.64.162
13:57:55 - THREAD: 4 - PORT: 9090 - IP: 199.249.230.70
13:57:55 - THREAD: 3 - PORT: 9080 - IP: 199.249.230.114
13:57:55 - THREAD: 5 - PORT: 9100 - IP: 185.220.100.254
...
```

### IP Rotation


```python
self.ipchange()         # Within threads

thread.ipchange()       # Outside threads
```