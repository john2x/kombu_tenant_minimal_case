This repo provides a minimal test case replicating https://github.com/bernardopires/django-tenant-schemas/issues/336

```
$ manage.py migrate_schemas
$ manage.py shell

>>> from kombu.transport.django.models import Queue
>>> Queue.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/manager.py", line 122, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/query.py", line 371, in count
    return self.query.get_count(using=self.db)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/sql/query.py", line 483, in get_count
    number = obj.get_aggregation(using, ['__count'])['__count']
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/sql/query.py", line 464, in get_aggregation
    result = compiler.execute_sql(SINGLE)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 848, in execute_sql
    cursor.execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/utils.py", line 95, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
ProgrammingError: relation "djkombu_queue" does not exist
LINE 1: SELECT COUNT(*) AS "__count" FROM "djkombu_queue"
                                          ^
```
