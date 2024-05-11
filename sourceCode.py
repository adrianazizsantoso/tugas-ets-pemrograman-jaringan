import os
import sys
import time
import subprocess

# Model konkurensi
MODELS = {
    "thread": "python server_thread_http.py",
    "process": "python server_process_http.py",
    "thread_secure": "python server_thread_https.py",
    "process_secure": "python server_process_https.py",
}

# Jumlah konkurensi
CONCURRENCY = [10, 50, 100, 150, 200]

def main():
    # Dapatkan argumen dari command line
    concurrency = int(sys.argv[1])
    model = sys.argv[2]

    # Pastikan model valid
    if model not in MODELS:
        print("Model tidak valid:", model)
        sys.exit(1)

    # Pastikan jumlah konkurensi valid
    if concurrency not in CONCURRENCY:
        print("Jumlah konkurensi tidak valid:", concurrency)
        sys.exit(1)

    # Jalankan server
    server_process = subprocess.Popen(MODELS[model].split())

    # Tunggu server untuk memulai
    time.sleep(1)

    # Jalankan benchmark
    result = subprocess.run(["ab", "-n", "1000", "-c", str(concurrency), "http://localhost:8000/"], capture_output=True)

    # Hentikan server
    server_process.terminate()

    # Cetak hasil benchmark
    print(result.stdout.decode())

if __name__ == "__main__":
    main()
