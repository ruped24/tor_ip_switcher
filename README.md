

# tor_ip_switcher

![](https://img.shields.io/badge/tor__ip__switcher-python_2.7-blue.svg?style=flat-square) ![](https://img.shields.io/badge/dependencies-toriptables2_python--tk_tor-orange.svg?style=flat-square) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/ruped24/tor_ip_switcher/graphs/commit-activity)


### [Setup ControlPort](https://drive.google.com/open?id=16YmyR4qVzEFOUSDhbPIeX-nzOPoKMszH):

Running the automated setup script:
* `tips_setup.py <your_new_password>`

* `sudo python tips_setup.py "password"`

***

### [Reset HashedControlPassword](https://drive.google.com/open?id=0B79r4wTVj-CZbFNIM0lGTVRjbU0):
<details><summary>Expand for manually resetting hash password</summary>
  <br>

Edit with sed editor: `/etc/tor/torrc`

1. Remove the comment "#" from the line with  [#ControlPort 9051](https://github.com/torproject/tor/blob/ac44e70ffc047941d196596dd651019c054b7faf/src/config/torrc.sample.in#L57)

* `sudo sed -i '/ControlPort /s/^#//' /etc/tor/torrc`

2. Remove the comment "#" from the line with [#HashedControlPassword](https://github.com/torproject/tor/blob/ac44e70ffc047941d196596dd651019c054b7faf/src/config/torrc.sample.in#L60)

* `sudo sed -i '/HashedControlPassword /s/^#//' /etc/tor/torrc`

3. Reset HashedControlPassword.

* `tor --hash-password "Your_new_password"`

* Replace the old hashed password below `16:01234556789ABCDEF` with <16:your_new_password_hash>.

* `sudo sed -i 's/^HashedControlPassword 16:.*[A-Z0-9]*$/HashedControlPassword 16:01234556789ABCDEF/' /etc/tor/torrc`

* [Reload](https://github.com/ruped24/toriptables2#to-change-tor-ip-address) the configuraton. `sudo toriptables2.py -r`

</details>

***

### [Usage:](https://drive.google.com/file/d/1WR2mALkhO34PW2YK_CFJsLM7xnaeLK8w/view)
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

### [Tor IP Switcher](https://github.com/ruped24/tor_ip_switcher)
<details><summary>Expand for screenshot</summary>
  <br>

[Tor IP Switcher Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZVm56M3pMdEx3X28)

</details>

### [Tor Manager](https://bitbucket.org/ruped24/tor_manager/src)
<details><summary>Expand for screenshot</summary>
  <br>

[Tor Manager Screenshot](https://drive.google.com/file/d/0B79r4wTVj-CZdUtGU3p6WldHX2s/view)

</details>

### [Installation and Setup](https://github.com/ruped24/tor_ip_switcher/wiki/Tor-IP-Switcher-installation)

### [Troubleshooting and FAQ](https://github.com/ruped24/tor_ip_switcher/wiki/Troubleshooting)
***
Credits:

Anonymous-Dev

[Forked from](https://github.com/Anonymous-Dev/Pyloris)

###### Disclaimer: ######
###### Pen-testing Only. ######
