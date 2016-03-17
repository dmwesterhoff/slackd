![Alt text](https://raw.githubusercontent.com/dmwesterhoff/slackd/master/logo.png?raw=true "slackd")
-------------------------------------------------------------------------------

IN DEVELOPMENT COME BACK SOON

slackd is an awesome command line slack daemon. Never switch from your console
window again. Easily send messages and files straight from your terminal and
get real-time messages from channels and DM's sent straight to your console's
text output. slackd sits dormant as a background process waiting for incoming
messages or to send outgoing ones.

### Table of Contents
---------------------

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Reference](#reference)
* [Contributing](#contributing)
* [History](#history)
* [Roadmap](#roadmap)
* [Author](#author)
* [License](#license)

### Features
------------

- Never change from your terminal to check or respond to slack messages
- Easy command line interface to interact with slack
- Daemonized slack websocket client receives messages in real time

### Installation
----------------

###### homebrew

```
brew install slackd
```

###### pip

```
pip install slackd
```

###### source

```
git clone https://github.com/dmwesterhoff/slackd.git
cd slackd
pip install -e slackd
```

### Usage
---------

##### Getting Started

After installation getting started is easy, first start slackd in a shell:

```
slackd start
```

If this is your first time running the daemon it will ask for a slack API 
token, which is necessary to go any further. After supplying the token
the daemon will begin running in the background and you'll be listening in
for incoming real time messages.

##### Sending Messages

Well you're probably gonna want to respond to incoming messages, its as easy
as possible.

### Reference
-------------

Here's a list of all the available cli commands, with a short description.

| Command             | Description                                           | 
| ------------------- | ----------------------------------------------------- |
| slackd users        | Shows a list of all users in the team, with a status  |
| slackd channels     | Shows a list of all available channels for the team   |
| slackd status       | Displays basic info on the authenticated user         |
| slackd logs         | Displays access logs for the team                     |
| slackd open         | Opens the teams slack homepage in a web browser       |
| slackd start        | Starts the slack websocket daemon                     |
| slackd stop         | Halts the slack websocket daemon                      |
| slackd restart      | Restarts the slack websocket daemon                   |

### Contributing
----------------

Got a great idea and want to contribute? Here's how you can help...

1. Fork it
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

### History
-----------

### Roadmap
-----------

### Author
----------

David Westerhoff - dmwesterhoff@gmail.com

### License
-----------

The MIT License (MIT)

Copyright (c) 2016 David M. Westerhoff

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
