from linked_list import *
from array_list import *
from sys import *
# Justin Mo
# a Song is one of
# ~ number, title, artist, or album
class Song:
    def __init__(self, number, title, artist, album):
        self.number = number # an int
        self.title = title # a str
        self.artist = artist # a str
        self.album = album # a str
    
    def __repr__(self):
        return "{:n}--{:s}--{:s}--{:s}".format(int(self.number), str(self.title), str(self.artist), str(self.album))

    def __eq__(self, other):
        return type(other) == Song and self.number == other.number and self.title == other.title and self.artist == other.artist and self.album == other.album

filename = argv[1]
txt_file = open(filename, "r")
lines = txt_file.readlines()
bool = False
for each_line in lines:
    if each_line.strip() != "" and len(each_line.split("--")) != 3:
        bool = True

if bool == True:
    print("Catalog input errors:")
    counter = 0
    for each_line in lines:
        counter += 1
        each_line = each_line.strip()
        if each_line.strip() != "" and len(each_line.split("--")) != 3:    
            print("line {:n}: malformed song information\n".format(counter).strip())
    print("\n".strip())

acc = 0
final_lines = ""
for line in lines:
    line = line.strip()
    if line != "" and len(line.split("--")) == 3 :
        final_lines += (str(acc) + "--" + line + "\n")
        acc += 1
final_lines = final_lines[:-1]

final_lines_split_1 = final_lines.split("\n")
new_song = []
for each_song in final_lines_split_1:
    new_song.append(each_song.split("--"))

def python_list_of_objects(new_song):   
    object_store = []
    acc = 0
    for each_song in new_song:
        object_store.append(Song(new_song[acc][0], new_song[acc][1], new_song[acc][2], new_song[acc][3]))
        acc += 1
    return object_store
list_of_objects = python_list_of_objects(new_song)

def final_list(list_of_objects):
    array_or_linked_list = empty_list()
    for i in range(len(list_of_objects)):
        array_or_linked_list = add(array_or_linked_list, i, list_of_objects[i])
    return array_or_linked_list

hybrid_list = final_list(list_of_objects)

def main(hybrid_list, acc, final_lines, lines, sort_type=None):
    print("Song Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit")
    choice = input("Selection: ")
    if int(choice) == 0:
        exit() 
    while int(choice) != 0:
        if int(choice) == 1:
            foreach(hybrid_list, print)
        elif int(choice) == 2:
            song_number = int(input("Enter song number: "))
            new_acc = 0
            for line in lines:
                line = line.strip()
                if line != "" and len(line.split("--")) == 3:
                    if new_acc == song_number:
                        chosen_one = line
                    new_acc += 1
            if song_number >= new_acc or song_number < 0:
                print("\n...Invalid song number\n")
                main(hybrid_list, acc, final_lines, lines, sort_type)
            song_info_line = chosen_one.split("--")
            print("\nSong information ...\n    Number: {:n}\n    Title: {:s}\n    Artist: {:s}\n    Album: {:s}".format(int(song_number), str(song_info_line[0]), str(song_info_line[1]), str(song_info_line[2])))
        elif int(choice) == 3:
            print("\nSort songs\n    0) By Number\n    1) By Title\n    2) By Artist\n    3) By Album")
            sort_choice = input("Sort by: ")
            if sort_choice.isalpha() == True or int(sort_choice) > 3:
                print("\n... Invalid sort option")
            elif int(sort_choice) == 0:
                sort_type = 0
                hybrid_list = sort(hybrid_list, less_than_number_first)
            elif int(sort_choice) == 1:
                sort_type = 1
                hybrid_list = sort(hybrid_list, less_than_title_first)
            elif int(sort_choice) == 2:
                sort_type = 2
                hybrid_list = sort(hybrid_list, less_than_artist_first)
            elif int(sort_choice) == 3:
                sort_type = 3
                hybrid_list = sort(hybrid_list, less_than_album_first)
        elif int(choice) == 4:
            filename = input("Enter name of file to load: ")
            try:
                txt_file = open(filename, "r")
            except FileNotFoundError:
                print("\nNo such file or directory\n")
                main(hybrid_list, acc, final_lines, lines, sort_type=None)
            new_lines = txt_file.readlines() 
            bool = False
            for each_line in new_lines:
                if each_line.strip() != "" and len(each_line.split("--")) != 3:
                    bool = True
            if bool == True:
                print("Catalog input errors:")
                counter = 0
                for each_line in new_lines:
                    counter += 1
                    if each_line.strip() != "" and len(each_line.split("--")) != 3:
                        print("line {:n}: malformed song information\n".format(counter).strip())
            final_lines += "\n"
            for line in new_lines:
                line = line.strip()
                if line != "" and len(line.split("--")) == 3 :
                    final_lines += (str(acc) + "--" + line + "\n")
                    acc += 1
            final_lines = final_lines[:-1]
            final_lines_split_1 = final_lines.split("\n")
            new_song = []
            for each_song in final_lines_split_1:
                new_song.append(each_song.split("--"))
            python_list_of_objects(new_song)
            list_of_objects = python_list_of_objects(new_song)
            hybrid_list = final_list(list_of_objects)
            lines = lines + new_lines
            if sort_type == 0:
                hybrid_list = sort(hybrid_list, less_than_number_first)
            if sort_type == 1:
                hybrid_list = sort(hybrid_list, less_than_title_first)
            if sort_type == 2:
                hybrid_list = sort(hybrid_list, less_than_artist_first)
            if sort_type == 3:
                hybrid_list = sort(hybrid_list, less_than_album_first)
        else: 
            print("\nInvalid option")
        print("\nSong Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit")
        choice = int(input("Selection: "))
        if choice == 0:
            break

if __name__ == '__main__':
    main(hybrid_list, acc, final_lines, lines, sort_type=None)
