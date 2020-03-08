import wget
import click
import subprocess

@click.command()
@click.argument("filing")
@click.argument("state")
def actblue(filing, state):
    receipts_url = "https://pp-projects-static.s3.amazonaws.com/itemizer/sa_%s_%s.csv" % (filing, state.lower())
    receipts = wget.download(receipts_url, bar=wget.bar_thermometer)
    spending_url = "https://pp-projects-static.s3.amazonaws.com/itemizer/sb_%s_%s.csv" % (filing, state.lower())
    spending = wget.download(spending_url, bar=wget.bar_thermometer)
    subprocess.call(["csvs-to-sqlite", receipts, "actblue.db"])

if __name__ == '__main__':
    actblue()
