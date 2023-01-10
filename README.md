# flet-mvp-counter

A simple showcase of how one could use the MVP pattern with Flet.
Heavily inspired by [this project](https://github.com/ArjanCodes/2022-gui/tree/main/mvp)
and the accompanying video.

Also showcases the client storage functionality (that's why the port is fixed,
otherwise no local storage would be found).
This enables you to continue counting right where you left off!

To try it yourself:

1. ```git clone https://github.com/iron3oxide/flet-mvp-counter.git```
2. ```cd flet-mvp-counter```
3. install poetry if you haven't yet and run ```poetry install```
4. create a new file called ".env" at the root of the project
5. add the keys (no values yet) found in settings.py to them, e.g. `GITHUB_CLIENT_ID=`
6. go to [your Github dev settings](https://github.com/settings/developers)
7. create a new OAuth app (call it whatever you want)
8. copy the client secret and client id
   and paste them to the corresponding keys in the .env file
9. choose a random string for `APP_SECRET_KEY`
10. run main.py to see the app in action

Feedback and PRs are welcome.
