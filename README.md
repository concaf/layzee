# layzee

`layzee` lets you specify Vagrantfile configuration via command line, so you don't have to write Ruby to spin up a VM.

## Using layzee

##### Installation

Just clone this repository,
`git clone https://github.com/containscafeine/layzee` and run `python setup.py develop`

##### Usage
```bash
$ layzee -h
usage: layzee [-h] [-p PROVIDER] [-m MEMORY] [-c CPU] [-b BOX] [-v VOLUMES]
              [-t TYPE] [-s SHELL] [-d DIRECTORY] [--stdout]

optional arguments:
  -h, --help            show this help message and exit
  -p PROVIDER, --provider PROVIDER
                        vagrant provider to deploy on
  -m MEMORY, --memory MEMORY
                        memory to allocate to the virtual machine
  -c CPU, --cpu CPU     CPUs to allocate to the virtual machine
  -b BOX, --box BOX     vagrant box to use
  -v VOLUMES, --volumes VOLUMES
                        host path:guest path
  -t TYPE, --type TYPE  which mount type to use
  -s SHELL, --shell SHELL
                        path to the shell script to provision the VM
  -d DIRECTORY, --directory DIRECTORY
                        directory to place your Vagrantfile in
  --stdout              print Vagrantfile on screen

```