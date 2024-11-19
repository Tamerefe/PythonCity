import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print(f"Battery: {battery.percent}%")
    print(f"Plugged: {battery.power_plugged}")
    
    def convertime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    
    if battery.secsleft == psutil.POWER_TIME_UNLIMITED:
        print("Left: Charging")
    elif battery.secsleft == psutil.POWER_TIME_UNKNOWN:
        print("Left: Unknown")
    else:
        print(f"Left: {convertime(battery.secsleft)}")
else:
    print("Battery not found")
