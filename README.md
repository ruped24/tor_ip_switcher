

# tor_ip_switcher


Setup:
```bash
Edit: /etc/tor/torrc
Remove the comment "#" from the line with  #ControlPort 9051 
Remove the comment "#" from the line with #HashedControlPassword 16:01234556789ABCDEF 
```

Reset the password:

```bash
tor --hash-password "Your_new_password"
```

Edit and replace the old HashedControlPassword 16:01234556789ABCDEF

with the newly generated hash in /etc/tor/torrc file from <Your_new_password> hash.
```bash
sudo kill -HUP $(pidof tor)
```
Usage:

```python
tor_ip_switcher.py
```

[Forked From](https://github.com/Anonymous-Dev/Pyloris/blob/master/tor_switcher.py)


### [Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZQzRkVDhQR3hRSlE)
