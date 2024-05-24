# Disseminate
*Can it run display an image without exploding? Great, make it a billboard.*

### Structure
- Server
  - Runs Django and has a collection of "displays" stored in its database
    - IP Address/Hostname
    - Username
    - SSH Public Key or Password
    - Remote Directory
  - Syncs files to host nodes and configure SSH commands to play files using VLC
- Display
  - Starts FBI at login and receives commands to play slideshow of local rsync'd folder
  - Runs in terminal mode

### Procedure for Auto Operation

1. **Make sure you are not using a window server or graphical environment.** The underlying display software is [framebuffer imageviewer](https://linux.die.net/man/1/fbi) (fbi), which directly writes pixels to the GPU's frame buffer. The program needs to be run in terminal mode.
2. **Enable autologin to the user running fbi.** This will open up the tty for the user that will receive the SSH and rsync commands.
3. **Add the slideshow command to .profile.** Using the same user, this will start the slideshow on boot, making the slideshow starting automatic from boot.

### Future
- Add photo displays to file list
- Add autosetup routine for client
- Add UI for customizable playlist time
