

# tor_ip_switcher


### [Setup:](https://github.com/ruped24/tor_ip_switcher/wiki/Tor-IP-Switcher-installation)
```bash
Edit: */etc/tor/torrc*
Remove the comment "#" from the line with  #ControlPort 9051 
Remove the comment "#" from the line with #HashedControlPassword 16:01234556789ABCDEF
Reset HashedControlPassword: See below.
```

### Reset the password:

```bash
tor --hash-password "Your_new_password"
```

* Edit: Replace the old HashedControlPassword 16:01234556789ABCDEF 

* With the newly generated hash, replace the old hash in */etc/tor/torrc* with <Your_new_password> hash.
```bash
sudo kill -HUP $(pidof tor)
```
### Usage:
* Method one

```python
tor_ip_switcher.py &
```
```bash
disown -a
```
* Method two
```bash
screen -dmS "torswitcher" tor_ip_switcher.py
```


### [Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZUEY0MXV2bVloUWM)

***
Credits:
[Forked From](https://github.com/Anonymous-Dev/Pyloris)

###### Disclaimer: ######
###### Please don't run this tool against my site or anyone else for that matter. ######
