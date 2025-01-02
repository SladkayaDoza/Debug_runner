#!/usr/bin/env python
import sys
import os
import subprocess
from watchfiles import watch
from watchfiles.filters import PythonFilter  # фильтр, чтобы отслеживать только .py
import signal
from typing import List, Optional, Union

def start_process(script_path: str, script_args: List[str]) -> subprocess.Popen:
    """
    Запускает subprocess с заданным скриптом и аргументами.
    Возвращает объект Popen.
    """
    cmd = [sys.executable, script_path] + script_args
    print(f"[debug_runner] Starting process: {cmd}")
    return subprocess.Popen(cmd)

def stop_process(proc: subprocess.Popen):
    """
    Останавливает subprocess корректно, отправляя SIGTERM (или аналог в Windows).
    Если процесс не завершается в разумные сроки — форсирует kill.
    """
    if proc.poll() is None:
        print("[debug_runner] Stopping current process...")
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print("[debug_runner] Force kill...")
            proc.kill()

def main():
    if len(sys.argv) < 2:
        print("Usage: python debug_runner.py <script.py> [args...]")
        sys.exit(1)

    script_path = sys.argv[1]               # Имя (путь) скрипта, который будем перезапускать
    script_args = sys.argv[2:]             # Остальные аргументы передадим этому скрипту

    # Стартуем первый раз
    proc = start_process(script_path, script_args)

    # Следим за изменениями в текущем каталоге (и подпапках)
    # Можно указать несколько путей, например watch(['.', '../some-other-dir'])
    # Фильтр PythonFilter позволит реагировать только на изменения в .py-файлах.
    print("[debug_runner] Watching for file changes... (Ctrl+C to exit)")
    try:
        for changes in watch('.', watch_filter=PythonFilter(), recursive=True):
            # Это событие — набор изменений (создание, удаление, изменение) в файлах .py
            # Как только мы получаем событие, значит что-то поменялось
            print(f"[debug_runner] Detected changes in .py files: {changes}")
            # Убиваем текущий процесс
            stop_process(proc)
            # Запускаем заново
            proc = start_process(script_path, script_args)
    except KeyboardInterrupt:
        print("[debug_runner] Ctrl+C caught — exiting...")
    finally:
        stop_process(proc)
        print("[debug_runner] Bye!")

if __name__ == "__main__":
    main()
