#!/usr/bin/python
import sys, os, subprocess, shutil, errno, datetime, unittest
import sync

def test_sync():

  test_config = {
    "mount": "/tmp/sync",
    "actives": {
      "Devastator" : [
        "Scrapper",
        "Hook",
        "Bonecrusher",
        "Longhaul",
        "Mixmaster",
        "Scavenger"
      ],
      "Voltron": [
        "Black",
        "Blue",
        "Green",
        "Red",
        "Yellow"
      ]
    }
  }

  if os.path.isdir(test_config['mount']):
    shutil.rmtree(test_config['mount'])

  # setup: create tmp filesystem
  for k, v in test_config['actives'].iteritems():
    master = os.sep.join([test_config['mount'], k])
    os.makedirs(master)

    f = open(os.sep.join([master, 'test']), 'w')
    f.write(master)
    f.close()

    for v2 in v:
      slave = os.sep.join([test_config['mount'], v2])
      os.makedirs(slave)

  # execute
  out = sync.sync(test_config)

  # validate
  for k, v in test_config['actives'].iteritems():
    master = os.sep.join([test_config['mount'], k])

    for v2 in v:
      synced_filename = os.sep.join([test_config['mount'], v2, 'test'])
      f = open(synced_filename, 'r')

      assert(os.path.isfile(synced_filename))
      assert(f.read() == master)

      f.close()

  # teardown
  shutil.rmtree(test_config['mount'], True)

if __name__ == "__main__":
  test_sync()
