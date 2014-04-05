
import os
import sys
from fabricate import main, run, shell, autoclean # run caches, shell doesn't

def all():
    base_image()
    namecoindns_image()
    tahoe_images()

def _docker_dir(role):
    return role

def base_image():
    shell('docker', 'build', '-t', 'pjzz/base', '.', cwd=_docker_dir('base'), silent=False)

def namecoindns_image():
    run('docker', 'build', '-t', 'pjzz/namecoin-dns', '.', cwd=_docker_dir('namecoin-dns'), silent=False)

namecoindns_gitdir = '/tmp/n2b'
def namecoindns_update():
    gitdir = namecoindns_gitdir
    env = os.environ
    env['GIT_DIR'] = gitdir + '/.git'
    shell('rm', '-rf', gitdir)
    shell('git', 'clone', 'https://github.com/khalahan/NamecoinToBind.git', gitdir)
    shell(('git log -n 1 > %s/LOG_HEAD' % gitdir).split(), shell=True, env=env, cwd=gitdir, silent=False)
    archive = os.path.join(os.getcwd(), _docker_dir('namecoin-dns'), 'NamecoinToBind.tar.gz')
    shell('git', 'archive', '-o', archive, 'HEAD', cwd=gitdir, silent=False)

def namecoindns_clean():
    shell('rm', '-rf', namecoindns_gitdir)

def namecoindns_run():
    env = os.environ
    env['NAMECOIN_USERNAME'] = 'root'
    env['NAMECOIN_PASSWORD'] = 'root'
    env['NAMECOIN_HOSTNAME'] = 'localhost.localdomain'
    shell('docker', 'run', '-d', '-t', '-p', '53053:53', '-p', '53053:53/udp', 'pjz/namecoin-dns', silent=False, env=env)

def tahoe_images():
    run('docker', 'build', '-t', 'pjzz/tahoe-lafs-introducer', '.', cwd=_docker_dir('tahoe-lafs-introducer'), silent=False)
    run('docker', 'build', '-t', 'pjzz/tahoe-lafs-storage', '.', cwd=_docker_dir('tahoe-lafs-storage'), silent=False)


def clean():
    namecoindns_clean()
    autoclean()


def show_targets():
        print("""Valid targets:
	all - build all images
	base_image - build the base (debian) image
	namecoindns_image - build the namecoin DNS image
	namecoindns_run - run the namecoin DNS image
	tahoe_images - build the tahoe introducer and storage images
        """)
        sys.exit()

main( default='show_targets', runner='always_runner' )

