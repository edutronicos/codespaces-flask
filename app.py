from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Uso do CPU
    cpu_percent = psutil.cpu_percent(interval=0.5)
    # Uso da RAM
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    # Uso de disco
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    # Tempo ligado (uptime)
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime_delta = now - boot_time
    uptime = str(uptime_delta).split('.')[0]  # Remove microsegundos
    # Processos ativos
    processes = len(psutil.pids())

    return render_template(
        "index.html",
        title="Monitoramento do Sistema",
        cpu_percent=cpu_percent,
        ram_percent=ram_percent,
        disk_percent=disk_percent,
        uptime=uptime,
        processes=processes
    )
