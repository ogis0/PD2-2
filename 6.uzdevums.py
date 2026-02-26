# Label; MountPoint; TotalSize (MB); Used (%)
partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mnt/win;100000;90",
"Recovery;/recovery;2000;98"
]

def calculate_used_mb(partitions):
    result = []
    
    for p in partitions:
        label, _, total_mb, used_pct = p.split(";")
        
        total_mb = int(total_mb)
        used_pct = int(used_pct)
        
        used_mb = total_mb * used_pct / 100
        
        result.append({
            "Label": label,
            "used_mb": int(used_mb)
        })
        
    return result
    
    
output = calculate_used_mb(partitions)

for item in output:
    print(item)