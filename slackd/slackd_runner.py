#!/usr/bin/env python

import time
from daemon import runner


class App():
    def __init__(self):
        self.stdin_path = '/dev/stdin'
        self.stdout_path = '/dev/stdout'
        self.stderr_path = '/dev/stderr'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def run(self):
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
