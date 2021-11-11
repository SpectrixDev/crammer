#!/usr/bin/env python3

import argparse, codecs, random, sys, os, time
from pystyle import Center, Anime, Colors, Colorate, Write, System
from os.path import isfile

def splashScreen():
    System.Clear()
    System.Title("Crammer - By SpectrixDev <3")
    System.Size(140, 40)
    text = """
 ██████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║     ██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝"""[1:]

    banner = r"""
                                                       .                      
                                                       *                        
                                                      .. **                     
                                                ,    * ,**/.                    
                                  .    , ,,,.,    ,    *,                       
                                ., .,,********,   **  ,.//  *                   
                   ,. ...  .,,,  , .  .,,,,..                                   
                       .,.,               ....                                  
                           . .    ..                                            
                                .,    .       *                                 
                                  ..*           ,                               
                                       ,                                        
                                ..        .                                     
                               .,,,     . ,  ..                                 
                                .,,,, ... .. ,. .,                              
                        ,    *   ..     , .      ., ,                           
                   ,      *   *     .,,,...         ., .                        
                       .    *  *       , *                 .                    
                          .    .                              ,                 
                             .       .,                                         
                             .. .   ... *                                       
                                . .....                                         
                                   ..,..                                        
                                     ..  *                                      
                                     . .,   *                                   
                                            .. *                                
                                      *           *                             
                                                    ,                           
                                     ,             ,   


                  ▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · .▄▄ ·     ▄▄▄ . ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄  
                 ▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▀.     ▀▄.▀·•█▌▐█•██  ▀▄.▀·▀▄ █·
                  ██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄ 
                 ▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█    ▐█▄▄▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌
                 .▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀      ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀                          
"""[1:]

    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, enter=True)
    System.Clear()
    print("\n"*2 + Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(text))+ "\n"*5)
    file = Write.Input("Drag & drop the text file we're gonna cram-memorize here, or enter its path:  ", Colors.purple, interval=0.005)

    if not file.strip() or not isfile(file):
        Colorate.Error(Colors.red, "This file does not exist! Make sure you put in the full path, or simply drag and drop it here.")
        return

    print(Colorate.Diagonal(Colors.purple_to_blue, "\n\nAlright, let's start cramming!"))
    time.sleep(1)
    return file

def main():
    parser = argparse.ArgumentParser(description="""A tool to help memorize some
    text! When provided with a file, this program will remove random words from
    each line of text and ask you to provide the words that were removed.""")

    parser.add_argument('--no-color', action='store_true',
                        help='hide colorful underlining. Does not remove colour from splash screen.')

    parser.add_argument('--a', dest='tries', type=int, default=3,
                        help=('number of tries to allow per word '
                              '(0 for unlimited tries, default: 3)'))

    parser.add_argument('--n', dest='num', type=int, default=0,
                        help=('number of words to remove from each line '
                              '(0 for random number of removals, default: 0)'))

    parser.add_argument('--l', dest='lower', type=int, default=1,
                        help=('lower bound on number of words to remove '
                              '(inclusive, default: 1)'))

    parser.add_argument('--u', dest='upper', type=int, default=0,
                        help=('upper bound on number of words to remove '
                              '(inclusive, 0 for no upper bound, default: 0)'))

    args = parser.parse_args()

    try:
        os.system('color')
        file = splashScreen()
        System.Clear()

        with codecs.open(file, 'r', 'utf-8') as f:
            current_line = ''

            # randomize the order of the rows of text fromthe file seperated by newlines
            lines = f.readlines()
            random.shuffle(lines)
            # Assign it to f again so we can use it again
            f = lines

            for line in f:
                missing_words = []
                new_word = u''
                split_line = line.split(' ')

                if args.num:
                    num = args.num
                else:
                    if args.upper:
                        upper = args.upper + 1
                    else:
                        upper = len(split_line) + 1

                    num = random.randrange(start=args.lower, stop=upper)

                words = [False] * num
                diff = len(split_line) - num
                if diff > 0:
                    words.extend([True] * diff)
                    random.shuffle(words)

                for i, word in enumerate(split_line):
                    show_word = words[i]

                    color_started = False

                    for char in word:
                        if (char.isalpha() and show_word) or not char.isalpha():
                            if color_started:
                                current_line += '\033[0m'
                                color_started = False

                            current_line += char
                        else:
                            new_word += char

                            if not color_started and not args.no_color:
                                current_line += '\033[91m'
                                color_started = True

                            current_line += '_'
                    if word[-1] != '\n':
                        if color_started:
                            current_line += '\033[0m'
                            color_started = False
                        current_line += ' '

                    if len(new_word):
                        missing_words.append(new_word)
                        new_word = u''
                tries = 1

                while len(missing_words):

                    next_word = missing_words[0]
                    print("\n\n" + current_line)

                    try:
                        guess = input('\033[1mEnter the next missing word:\033[0m ')
                    except KeyboardInterrupt:
                        sys.exit(0)
                    except EOFError:
                        sys.exit(0)

                    if guess == next_word:
                        System.Clear()
                        print(f'\033[92mCorrect! The word was "{next_word}".\033[0m')
                    elif args.tries and tries == args.tries:
                        System.Clear()
                        print(f'\033[93mToo many tries. The word was "{next_word}".\033[0m')
                    else:
                        System.Clear()
                        print(f'\033[93m"{guess}" is incorrect. Please try again.\033[0m')
                        tries += 1
                        continue

                    if args.no_color:
                        current_line = current_line.replace('_' * len(next_word),next_word,1)
                    else:
                        current_line = current_line.replace('\033[91m' + '_' * len(next_word) + '\033[0m',next_word,1)

                    missing_words.pop(0)
                    tries = 1

    except IOError:
        print("File not found: '{}'".format(args.filename))
        
if __name__ == '__main__':
    main()
