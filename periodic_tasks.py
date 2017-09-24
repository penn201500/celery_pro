# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from .celery import app
from celery.schedules import crontab

@app.on_after_configure.connect
def setup_period_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('helo'), name='add every 10s')
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

@app.task
def test(arg):
    print(arg)
