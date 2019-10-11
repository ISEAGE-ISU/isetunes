# isetunes
Web frontend for any music player, using Python3.6/Flask with authentication, allowing users to request and vote on 
songs. Supports whatever backend and music service you're willing to write the API calls for.

To run, you will need to install `mopidy` and the `mopidy-spotify` extension. 
(This can run on a separate host).
Once those are installed, add the following to `~/.config/mopidy/mopidy.conf`.
Consult the internet for ways of finding these values (Spotify changes this semi regularly
for.... reasons)

```config
[spotify]
username = 
password = 
client_id = 
client_secret = 
```

