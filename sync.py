#!/usr/bin/python
import sys, os, subprocess, shutil, errno, json, datetime

##
 # @param {tuple} Backup / Sync configuration
 # @return stdout
 ##
def sync(backup_config):

  output  = []
  if not backup_config['volumes']:
    output.append('Error: volumes does not exist')
    return

  # "volumes" = {
  #   "m": master",
  #   "s": [
  #     "slave1",
  #     "slave2",
  #     "slave3"
  #   ]
  # }
  #
  volumes = backup_config['volumes']
  for volume in volumes:

    master = volume["m"]
    if not os.path.exists(master):
      output.append('Error: master > ' + master + ' does not exist')
      continue

    slaves = volume["s"]
    for slave in slaves:

      if not os.path.exists(slave):
        output.append('Error: slave > ' + slave  + ' does not exist\n\n')
        continue

      cmd = ' '.join([
        'rsync',
        ' -apoguvrEC',
        ' --delete ',
        ' --size-only',
        # ' --exclude-from=' + cfg['rsync.exclude.file'],
        master + '/',
        slave + '/'
      ])

      p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
      p_out = p.communicate()[0]+'\n';
      output.append('Success: master > ' + master + ' => slave > ' + slave + ' sync')

  return "\n".join(output)

def log(str):
  print "sync: " + str

def execute():
  if len(sys.argv) <= 1:
    log("What's going on? Config file is required.")
    exit()

  filename = sys.argv[1]
  if not os.path.isfile(filename):
    log(filename + " is not a real file. Try again.")
    exit()

  try:
    with open(filename) as data:
      config = json.load(data)
  except Exception:
    log(filename + " is not a valid JSON file.")
    exit()

  print(sync(config['storage']['sync']))

if __name__ == "__main__":
  execute()
