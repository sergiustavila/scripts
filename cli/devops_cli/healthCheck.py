import datetime
import subprocess
import psutil
import click

@click.group()
def cli():
    """Simple cli"""

@cli.command("date_time", short_help="Show current date and time")
def date_time():
    current_datetime = datetime.datetime.now()
    click.echo(f"Date and Time: {current_datetime}")

@cli.command("uptime", short_help="Show machine uptime")
def get_machine_uptime():
    try:
        # For Unix-like systems
        uptime = subprocess.check_output(["uptime -p"], universal_newlines=True).strip()
    except:
        #  For Windows
        uptime = psutil.boot_time()
        uptime = datetime.datetime.fromtimestamp(uptime).strftime("%Y-%m-%d %H:%M:%S")

    click.echo(f"Machine Uptime: {uptime}")

@cli.command("disk", short_help="Show disk usage")
def get_disk_usage():
    disk_info = psutil.disk_usage("/")
    click.echo(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
    click.echo(f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
    click.echo(f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB")
    click.echo(f"Disk Space Percentage: {disk_info.percent} %")

@cli.command("get_memory_usage", short_help="Show memory usage")
def get_memory_usage():
    virtual_memory = psutil.virtual_memory()
    
    click.echo(f"Total Memory: {virtual_memory.total / (1024 ** 3):.2f} GB, " \
           f"Available Memory: {virtual_memory.available / (1024 ** 3):.2f} GB, " \
           f"Used Memory: {virtual_memory.used / (1024 ** 3):.2f} GB")    

if __name__ == '__main__' :
    click.echo("Health Check Report:")
    cli()