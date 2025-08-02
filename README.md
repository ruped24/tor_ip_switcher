

# tor_ip_switcher

![](https://img.shields.io/badge/tor__ip__switcher-python_2.7-blue.svg?style=flat-square) ![](https://img.shields.io/badge/dependencies-toriptables2_python--tk_tor-orange.svg?style=flat-square) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/ruped24/tor_ip_switcher/graphs/commit-activity)

---

### [tor_ip_switcher ELF 64-bit LSB executable, x86-64 - AppImage](https://github.com/ruped24/tor_ip_switcher/releases/tag/v2.7)

![](https://img.shields.io/badge/tor__ip__switcher-AppImage-red.svg?style=flat-square)  ![Architecture](https://img.shields.io/badge/architecture-x86__64-blue.svg?style=flat-square)  ![](https://img.shields.io/badge/dependencies-toriptables2_tor-orange.svg?style=flat-square) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/ruped24/tor_ip_switcher/graphs/commit-activity)


---

### [Setup ControlPort](https://drive.google.com/open?id=16YmyR4qVzEFOUSDhbPIeX-nzOPoKMszH):

Running the automated tips_setup script
<details><summary>Expand for tips_setup script commands</summary>
<br>
  
```bash
tips_setup.py <your_new_password>
```

```python
sudo python3 tips_setup.py "password"
```

</details>

***

### [Reset HashedControlPassword](https://drive.google.com/open?id=0B79r4wTVj-CZbFNIM0lGTVRjbU0):
<details><summary>Expand for manually resetting password</summary>
<br>

Edit with sed editor: `/etc/tor/torrc`

1. Remove the comment "#" from the line with  [#ControlPort 9051](https://github.com/torproject/tor/blob/ac44e70ffc047941d196596dd651019c054b7faf/src/config/torrc.sample.in#L57)

 ```bash
sudo sed -i '/ControlPort /s/^#//' /etc/tor/torrc
```
2. Remove the comment "#" from the line with [#HashedControlPassword](https://github.com/torproject/tor/blob/ac44e70ffc047941d196596dd651019c054b7faf/src/config/torrc.sample.in#L60)

```bash
sudo sed -i '/HashedControlPassword /s/^#//' /etc/tor/torrc
```

3. Reset HashedControlPassword.

```bash
tor --hash-password "Your_new_password"
```

4. Replace the old hashed password below `16:01234556789ABCDEF` with <16:your_new_password_hash>.

```bash
sudo sed -i 's/^HashedControlPassword 16:.*[A-Z0-9]*$/HashedControlPassword 16:01234556789ABCDEF/' /etc/tor/torrc
```

5. Finally, reload the configuration file. 
```bash
sudo kill -HUP $(pidof tor)
```

</details>

***

### [Usage](https://drive.google.com/file/d/0B79r4wTVj-CZOGJadlBtWWxPWFk/view?resourcekey=0-6GxU28nWepXCim7xtkUONA):

<details><summary>Expand for usage</summary>
<br>
Method One: Run-as a background job and disown

```python
tor_ip_switcher.py &
```
```bash
disown
```
Method Two: Run-as a screen session detached
  
<details><summary>Expand for run-as a screen session detached</summary>
<br>

```bash
screen -dmS "torswitcher" tor_ip_switcher.py
```
</details>

</details>

---

### [Tor IP Switcher](https://github.com/ruped24/tor_ip_switcher#tor_ip_switcher)
<details><summary>Expand for screenie</summary>
  <br>

[▹ Tor IP Switcher Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZVm56M3pMdEx3X28)

</details>

### [Tor Manager](https://bitbucket.org/ruped24/tor_manager/src)
<details><summary>Expand for screenie</summary>
  <br>

[▹ Tor Manager Screenshot](https://drive.google.com/file/d/0B79r4wTVj-CZdUtGU3p6WldHX2s/view)

</details>

---

### [Installation and Setup](https://github.com/ruped24/tor_ip_switcher/wiki/Tor-IP-Switcher-installation)

### [Troubleshooting and FAQ.](https://github.com/ruped24/tor_ip_switcher/wiki/Troubleshooting)

***
Credits:

Anonymous-Dev

[Forked from](https://github.com/Anonymous-Dev/Pyloris)

###### Disclaimer: ######
###### Pen-testing Only. ######


