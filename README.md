

# tor_ip_switcher


Setup:
```
Edit /etc/torrc
Remove the comment "#" from the line with  #ControlPort 9051 
Remove the comment "#" from the line with #HashedControlPassword 
```

Reset the password:

``
tor –hash-password "Your_new_password"
``



Usage:

```
sudo ./tor_ip_switcher.py
```

[Forked From](https://github.com/Anonymous-Dev/Pyloris/blob/master/tor_switcher.py)


### [Screenshot](https://drive.google.com/open?id=0B79r4wTVj-CZQzRkVDhQR3hRSlE)
