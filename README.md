# Disseminate
*Can it run VLC without exploding? Great, make it a billboard.*

This is just a concept for now, but the proposed architecture is as follows:

### Structure
- Server
  - Runs Django and has a collection of "displays" stored in its database
    - IP Address/Hostname
    - Username
    - SSH Public Key or Password
    - Remote Directory
  - Syncs files to host nodes and configure SSH commands to play files using VLC
- Display
  - Uses CVLC as a daemon and receives commands to play from local folder
  - Runs in terminal mode

### Future
- MQTT?
