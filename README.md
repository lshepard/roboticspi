# RoboticsPi

## Twitch.tv Streaming -- Manual

You just need libav-tools installed!

```
sudo apt-get update && sudo apt-get install libav-tools
```

Then, you can add `twstream` to your PATH (like /usr/local/bin -- by default
exists and is on the PATH).

```
sudo cp ./twstream /usr/local/bin
```

Then, copy your Stream key from twitch.tv, on Dashboard > Settings > Channel.

Then, launch the stream:

```
twstream [copy pasted stream key here]
```

To end, just ctrl-c.

