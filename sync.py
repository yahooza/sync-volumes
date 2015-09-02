#!/usr/bin/python
import sys, os, subprocess, shutil, errno, json, datetime

##
 # @param {tuple} Backup / Sync configuration
 # @return stdout
 ##
def sync(backup_config):

  output = []

  masters = backup_config['actives'].keys()

  for master in masters:

    master_active = os.sep.join([backup_config['mount'], master])
    if not os.path.exists(master_active):
      output.append('Error: master > ' + master_active + ' does not exist')
      continue

    slaves = backup_config['actives'][master]

    for slave in slaves:

      slave_active = os.sep.join([backup_config['mount'], slave])
      if not os.path.exists(slave_active):
        output.append('Error: slave > ' + slave_active  + ' does not exist\n\n')
        continue

      cmd = ' '.join([
        'rsync',
        ' -apoguvrEC',
        ' --delete ',
        ' --size-only',
        # ' --exclude-from=' + cfg['rsync.exclude.file'],
        master_active + '/',
        slave_active + '/'
      ])

      p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
      p_out = p.communicate()[0]+'\n';
      output.append('Success: master > ' + master_active + ' => slave > ' + slave_active + ' sync')

  return "\n".join(output)
