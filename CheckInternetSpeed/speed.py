import speedtest

def check_speed():
    # Initialize Speedtest instance
    speed = speedtest.Speedtest()
    
    # Set a smaller server pool for faster server selection
    speed.get_servers([])  # Empty list uses nearby servers; can also specify particular server IDs for quicker results.
    speed.get_best_server()  # Finds the best server based on ping and distance
    
    # Get download and upload speeds in Mbps
    download_speed = round(speed.download() / 1_000_000, 2)
    upload_speed = round(speed.upload() / 1_000_000, 2)
    
    # Get ping in milliseconds
    ping = speed.results.ping
    
    print(f"Download Speed: {download_speed} Mbps")
    print(f"Upload Speed: {upload_speed} Mbps")
    print(f"Ping: {ping} ms")

check_speed()
