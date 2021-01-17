import click
import subprocess
import os


@click.command()
@click.option('--download/--no-download', default=False, help='Download raw data.')
@click.option('--extract/--no-extract', default=False, help='Extract data from zip file.')
@click.option('--pre_process/--no-pre_process', default=False, help='Pre-process data.')
def main(download, extract, pre_process):
    if download:
        path = os.path.join("bike_model", "download_data.py")
        subprocess.run(['python3', path])
    if extract:
        path = os.path.join("bike_model", "extract_data.py")
        subprocess.run(['python3', path])
    if pre_process:
        path = os.path.join("bike_model", "pre_process.py")
        subprocess.run(['python3', path])

if __name__ == '__main__':
    main()
