#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery
from .celery import app

@app.task
def hello(x,y):
    print x,y
    return x+y

@app.task
def mul(x,y):
    print "x*y is:", x*y
    return x*y
