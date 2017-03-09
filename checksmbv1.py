#!/usr/bin/env python2
from impacket.smbconnection import SMBConnection, smb
import click


@click.command()
@click.argument('ip')
def check_smbv1(ip):
    click.echo('Attempting SMBv1 negotation with {}...\t'.format(ip), nl=False)
    try:
        s = SMBConnection('*SMBSERVER', ip, preferredDialect=smb.SMB_DIALECT)
        if isinstance(s, SMBConnection):
            click.secho('Success', fg='green')
    except Exception as e:
        click.secho('Failed\t', fg='red', nl=False)
        click.echo(e)
        return

if __name__ == '__main__':
        check_smbv1()
