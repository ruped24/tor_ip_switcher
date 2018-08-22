

# tor_ip_switcher


### Setup ControlPort:

[Running the automated setup script:](https://drive.google.com/open?id=16YmyR4qVzEFOUSDhbPIeX-nzOPoKMszH)

* `sudo python tips_setup.py "password"`

* `sudo kill -HUP $(pidof tor)`

***

For CLI Ninjas:

Manual edit: `/etc/tor/torrc`

1. Remove the comment "#" from the line with  #ControlPort 9051

* `sudo sed -i '/ControlPort /s/^#//' /etc/tor/torrc`

2. Remove the comment "#" from the line with #HashedControlPassword 16:01234556789ABCDEF

* `sudo sed -i '/HashedControlPassword /s/^#//' /etc/tor/torrc`

3. Reset HashedControlPassword. See below. 

### [Reset HashedControlPassword](https://drive.google.com/open?id=0B79r4wTVj-CZbFNIM0lGTVRjbU0):

* `tor --hash-password "Your_new_password"`

* Replace the old hashed password below `16:01234556789ABCDEF` with <16:your_new_password_hash>.

* `sudo sed -i 's/^HashedControlPassword 16:.*[A-Z0-9]*$/HashedControlPassword 16:01234556789ABCDEF/' /etc/tor/torrc`

* Send tor's daemon process SIGHUP to reload the configuraton.
```bash
sudo kill -HUP $(pidof tor)
```
***

### [Usage:](https://github.com/ruped24/tor_ip_switcher/wiki/Tor-IP-Switcher-installation)
* Method One: Run-as a background job and disown

```python
tor_ip_switcher.py &
```
```bash
disown -a
```
* Method Two: Run-as a screen session detached
```bash
screen -dmS "torswitcher" tor_ip_switcher.py
```
***

### Tor IP Switcher
* ### [Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZVm56M3pMdEx3X28)

### [Tor Manager](https://bitbucket.org/ruped24/tor_manager/src)

* ### [Screenshot](https://drive.google.com/file/d/0B79r4wTVj-CZdUtGU3p6WldHX2s/view)

### [Troubleshooting and FAQ](https://github.com/ruped24/tor_ip_switcher/wiki/Troubleshooting)
***
Credits:

Anonymous-Dev

[Forked from](https://github.com/Anonymous-Dev/Pyloris)

###### Disclaimer: ######
###### Pen-testing Only. ######
