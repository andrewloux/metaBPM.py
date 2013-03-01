import argparse
import sys, os
import eyed3
import echonest.remix.audio as audio

#Command line parser. 
parser = argparse.ArgumentParser(description='Add BPM metadata to your music collection')
parser.add_argument('-s','--source path', help='Your music directory eg: "C:/mp3" ', required=True)
args = vars(parser.parse_args())

#Pass in source folder
location = args['source path']
os.chdir(location)

mp3list = os.listdir(location)

for mp3 in mp3list:
    audiofile = audio.LocalAudioFile(mp3)
    bpm = audiofile.analysis.tempo['value']
    metadata = eyed3.load(mp3)
    metadata.tag.bpm = bpm
    metadata.tag.save()
