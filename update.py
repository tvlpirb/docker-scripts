#!/usr/bin/python
# Authored by Talhah Peerbhai <talhah@cmu.edu>
import os

##### CONFIG #####
# set directory where docker dirs are
dock_path = "/home/talhah/docker-configs"
# set directories to exclude
dir_excl = ["scripts","gitea"]
##### END CONFIG #####


os.chdir(dock_path)
# output current path
print(f"Working in {os.getcwd()}")

sub_dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
# Remove excluded dirs
sub_dirs = [i for i in sub_dirs if i not in dir_excl]

def update_docker():
    cmd = "docker-compose pull"
    os.system(cmd)
    cmd = "docker-compose up -d --remove-orphans"
    os.system(cmd)


for dirs in sub_dirs:
    os.chdir(dirs)
    update_docker()
    os.chdir('..')

