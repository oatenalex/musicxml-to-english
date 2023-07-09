from music21 import converter


def parse_musicxml():
    path = input("Please enter the path to your MusicXML file: ")
    score = converter.parse(path)
    for note in score.recurse().notes:
        print(note)


parse_musicxml()
