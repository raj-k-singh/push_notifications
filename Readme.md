A simple python script to send push notifications via pushover.
I use this to send notifcations to myself on completion of long running commands.
While it's possible to have terminal alerts when working on the local machine,
the push notification method can be particularly helpful when working on a
remote machine.

Usage:
-   Create an account and an app on [pushover](https://pushover.net).
-   Plug in the user and app tokens into push_notification.py
-   Send a notiification with `python push_notification.py <notification_text>`
