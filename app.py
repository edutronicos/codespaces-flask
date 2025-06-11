import psutil
import platform
from datetime import datetime, timedelta
from flask import Flask, render_template
import GPUtil

app = Flask(__name__)

def get_system_info():
    # Informações de CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    
    # Informações de Memória
    memory = psutil.virtual_memory()
    memory_total_gb = round(memory.total / (1024**3), 2)
    memory_used_gb = round(memory.used / (1024**3), 2)
    memory_available_gb = round(memory.available / (1024**3), 2)
    
    # Informações de Disco
    disk = psutil.disk_usage('/')
    disk_total_gb = round(disk.total / (1024**3), 2)
    disk_used_gb = round(disk.used / (1024**3), 2)
    disk_free_gb = round(disk.free / (1024**3), 2)
    
    # Informações de Rede
    net_io = psutil.net_io_counters()
    net_sent_gb = round(net_io.bytes_sent / (1024**3), 2)
    net_recv_gb = round(net_io.bytes_recv / (1024**3), 2)
    
    # Tempo de atividade
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    
    # Processos
    processes = len(psutil.pids())
    
    # Temperatura (se disponível)
    try:
        temps = psutil.sensors_temperatures()
        cpu_temp = None
        if temps and 'coretemp' in temps:
            cpu_temp = temps['coretemp'][0].current
        elif temps and 'cpu_thermal' in temps:
            cpu_temp = temps['cpu_thermal'][0].current
    except:
        cpu_temp = None
    
    # Bateria (se disponível)
    try:
        battery = psutil.sensors_battery()
        battery_percent = battery.percent if battery else None
        battery_plugged = battery.power_plugged if battery else None
    except:
        battery_percent = None
        battery_plugged = None
    
    # GPU (se disponível)
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                'name': gpu.name,
                'load': round(gpu.load * 100, 1),
                'memory_total': round(gpu.memoryTotal / 1024, 2),
                'memory_used': round(gpu.memoryUsed / 1024, 2),
                'memory_free': round(gpu.memoryFree / 1024, 2),
                'temperature': gpu.temperature
            })
    except:
        gpu_info = []
    
    return {
        'sistema': platform.system(),
        'versao': platform.version(),
        'arquitetura': platform.architecture()[0],
        'processador': platform.processor(),
        'hostname': platform.node(),
        'cpu': {
            'percentual': cpu_percent,
            'cores_fisicos': cpu_count,
            'cores_logicos': cpu_count_logical,
            'frequencia_atual': round(cpu_freq.current, 2) if cpu_freq else 'N/A',
            'frequencia_max': round(cpu_freq.max, 2) if cpu_freq else 'N/A',
            'temperatura': cpu_temp
        },
        'memoria': {
            'total_gb': memory_total_gb,
            'usado_gb': memory_used_gb,
            'disponivel_gb': memory_available_gb,
            'percentual': memory.percent
        },
        'disco': {
            'total_gb': disk_total_gb,
            'usado_gb': disk_used_gb,
            'livre_gb': disk_free_gb,
            'percentual': round((disk.used / disk.total) * 100, 1)
        },
        'rede': {
            'enviado_gb': net_sent_gb,
            'recebido_gb': net_recv_gb
        },
        'tempo_atividade': str(uptime).split('.')[0],
        'processos_ativos': processes,
        'bateria': {
            'percentual': battery_percent,
            'conectada': battery_plugged
        },
        'gpu': gpu_info
    }

@app.route('/')
def index():
    info = get_system_info()
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
