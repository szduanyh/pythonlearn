#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

__author__ = 'admin-1'

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
r.set('foo', 'bar')
print(r.get('foo'))

r.lpush('list', 1)
r.lpush('list', 2)
r.lpush('list', 3)
r.lpush('list', 4)
r.lpush('list', 5)
r.lpush('list', 6)
r.lpush('list', 7)
r.lpush('list', 8)

print(r.lrange('list', 0, -1))

r.flushdb()
