#!/bin/bash
STATE_FILE="/tmp/polybar_sysinfo_state"
CACHE_FILE="/tmp/polybar_cpu_prev"

# Inicializar estado
if [ ! -f "$STATE_FILE" ]; then
    echo "cpu" > "$STATE_FILE"
fi

# Alternar estado al hacer clic
if [[ "$1" == "--toggle" ]]; then
    STATE=$(cat "$STATE_FILE")
    if [[ "$STATE" == "cpu" ]]; then
        echo "mem" > "$STATE_FILE"
    else
        echo "cpu" > "$STATE_FILE"
    fi
    exit 0
fi

STATE=$(cat "$STATE_FILE")

if [[ "$STATE" == "cpu" ]]; then
    # Leer valores actuales de /proc/stat
    read cpu user nice system idle iowait irq softirq steal guest < /proc/stat
    TOTAL=$((user + nice + system + idle + iowait + irq + softirq + steal))
    IDLE=$((idle + iowait))

    # Si no hay valores previos, inicializarlos y mostrar algo provisional
    if [ ! -f "$CACHE_FILE" ]; then
        echo "$TOTAL $IDLE" > "$CACHE_FILE"
        echo "CPU ..."
        exit 0
    fi

    # Leer valores previos
    read PREV_TOTAL PREV_IDLE < "$CACHE_FILE"

    # Guardar valores nuevos
    echo "$TOTAL $IDLE" > "$CACHE_FILE"

    # Calcular diferencia
    DIFF_TOTAL=$((TOTAL - PREV_TOTAL))
    DIFF_IDLE=$((IDLE - PREV_IDLE))

    if [ "$DIFF_TOTAL" -gt 0 ]; then
        CPU=$(( (100 * (DIFF_TOTAL - DIFF_IDLE)) / DIFF_TOTAL ))
    else
        CPU=0
    fi

    echo "CPU ${CPU}%"
else
    # Memoria usada
    MEM=$(free -m | awk '/Mem:/ {printf "%d/%dMB", $3, $2}')
    echo "RAM $MEM"
fi

