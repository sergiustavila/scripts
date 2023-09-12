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
    click.echo("Date and Time: {}".format(current_datetime))

@cli.command("get_machine_uptime", short_help="Show machine uptime")
def get_machine_uptime():
    try:
        uptime_output = subprocess.check_output(['uptime'], universal_newlines=True)

        click.echo("Machine Uptime: {}".format(uptime_output.strip()))
    except subprocess.CalledProcessError:
         click.echo("Unable to retrieve uptime information.")

@cli.command("get_disk_usage", short_help="Show disk usage")
def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_usage_info = []

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage_info.append(f"{partition.device} - Total: {usage.total / (1024 ** 3):.2f} GB, "
                               f"Used: {usage.used / (1024 ** 3):.2f} GB, "
                               f"Free: {usage.free / (1024 ** 3):.2f} GB")
    click.echo(disk_usage_info)

@cli.command("get_memory_usage", short_help="Show memory usage")
def get_memory_usage():
    virtual_memory = psutil.virtual_memory()
    
    click.echo(f"Total Memory: {virtual_memory.total / (1024 ** 3):.2f} GB, " \
           f"Available Memory: {virtual_memory.available / (1024 ** 3):.2f} GB, " \
           f"Used Memory: {virtual_memory.used / (1024 ** 3):.2f} GB")    

if __name__ == '__main__' :
    click.echo("Health Check Report:")
    cli()