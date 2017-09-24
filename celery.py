#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['celery_pro.test_cpu', 'celery_pro.periodic_tasks']) #include files


if __name__ == '__main__':
    app.start()
