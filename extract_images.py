
import glob
import ffmpeg

filenames = glob.glob('videos/*.mkv')

for filename in filenames:
    date = filename[7:17]
    ffmpeg.input(filename).filter('fps', fps='1/2').output(f'images/{date}_%04d.jpg').run()

filenames = glob.glob('images/*.jpg')
