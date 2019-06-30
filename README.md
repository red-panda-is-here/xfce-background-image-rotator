# Xface desktop image rotator
Works for Python2.x and Python3.x
## How to use
Create directory and copy images there. If you want to specify your own directory you can do that in `config.py`.
```
$ mkdir ~/Pictures/Wallpapers/
$ cp -r ~/Old/Directory/. ~/Pictures/Wallpapers/
```
Clone repository.
```
$ git clone ssh://git@github.com/<user>/<repository name>.git
```
In `config.py` specify how many monitors and workspaces you use.
You can check it by running:
```
$ xfconf-query --channel xfce4-desktop --list
```
Add execute permissions to the file which will be called from crontab.
```
$ chmod +x rotate_desktop_images.sh
```
Open crontab.
```
$ sudo vim /etc/crontab
```
Add to crontab next line(if you want to change images every 30 mins).
```
30 * * * * username /path/to/project/xface-background-image-rotator/rotate_desktop_images.sh

```
Run `crontab -l` to check if crontab works.

