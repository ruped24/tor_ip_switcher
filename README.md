

# tor_ip_switcher


### Setup ControlPort:

Edit: `/etc/tor/torrc`

1. `Remove the comment "#" from the line with  #ControlPort 9051` 
2. `Remove the comment "#" from the line with #HashedControlPassword 16:01234556789ABCDEF`
3. `Reset HashedControlPassword 16: See Reset HashedControlPassword below.`


### Reset HashedControlPassword:

```bash
tor --hash-password "Your_new_password"
```

* Edit: Replace the old `HashedControlPassword 16:01234556789ABCDEF` 

* With the newly [generated hash](https://drive.google.com/open?id=0B79r4wTVj-CZbFNIM0lGTVRjbU0), replace the old hash in `/etc/tor/torrc` with <Your_new_password> hash.

* Send tor's daemon process SIGHUP to reload the configuraton.
```bash
sudo kill -HUP $(pidof tor)
```
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


### [Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZVm56M3pMdEx3X28)

***
Credits:

Anonymous-Dev

[Forked from](https://github.com/Anonymous-Dev/Pyloris)

###### Disclaimer: ######
###### Please don't test this tool against my site or anyone else for that matter. Pen-testing Only. ######
