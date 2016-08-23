import argparse
import os
import subprocess

import sys
from jinja2 import Environment, FileSystemLoader


def layzee_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--provider",
                        default="libvirt",
                        help="vagrant provider to deploy on")
    parser.add_argument("-m", "--memory",
                        default="4096",
                        type=int,
                        help="memory to allocate to the virtual machine")
    parser.add_argument("-c", "--cpu",
                        default=2,
                        type=int,
                        help="CPUs to allocate to the virtual machine")
    parser.add_argument("-b", "--box",
                        default="fedora/24-cloud-base",
                        help="vagrant box to use")
    parser.add_argument("-v", "--volumes",
                        action="append",
                        help="host path:guest path")
    parser.add_argument("-t", "--type",
                        default="nfs",
                        help="which mount type to use")
    parser.add_argument("-s", "--shell",
                        help="path to the shell script to provision the VM")
    parser.add_argument("-d", "--directory",
                        help="directory to place your Vagrantfile in")
    parser.add_argument("--stdout",
                        action="store_true",
                        help="print Vagrantfile on screen")

    return parser


def render_from_jinja(args):
    j2_template_path = os.path.normpath(os.path.join(os.path.dirname(__file__)))
    j2_env = Environment(loader=FileSystemLoader(j2_template_path))
    j2_template = j2_env.get_template("Vagrantfile.j2")
    return j2_template.render(**vars(args))


def vagrant_bootstrap(args, rendered):
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)

    with open("{}/Vagrantfile".format(args.directory), "w") as f:
        f.write(rendered)

    return True


def vagrant_up(directory):
    output = subprocess.Popen("VAGRANT_CWD={} vagrant up".format(directory),
                              stdout=subprocess.PIPE, shell=True, bufsize=1)

    for line in iter(output.stdout.readline, ""):
        print line,


def main():
    parsed = layzee_parser()
    args = parsed.parse_args()
    if len(sys.argv) < 2:
        parsed.print_help()
        sys.exit(0)
    rendered = render_from_jinja(args)
    if args.stdout:
        print rendered
        sys.exit(0)
    if vagrant_bootstrap(args, rendered):
        vagrant_up(args.directory)
