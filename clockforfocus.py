import time
import winsound

def pomodoro_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    
    while seconds > 0:
        secs_remaining = int(seconds % 60)
        mins_remaining = int((seconds - secs_remaining) / 60)
        print(f'{mins_remaining:02d}:{secs_remaining:02d}', end='\r')
        time.sleep(1)
        
        seconds -= 1
    
    print('Time is up!')
    winsound.Beep(440, 1000)

pomodoro_timer(25)  # 将专注时钟设置为25分钟
