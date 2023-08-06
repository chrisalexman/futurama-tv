from subprocess import run

videos_path = '/home/pi/Documents/futurama-tv/videos/'

run(['vlc', '--x11-display', ':0', videos_path, '-f', '--random'])
