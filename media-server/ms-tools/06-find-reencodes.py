#!/usr/bin/env python


def fileList():
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in fnmatch.filter(filenames, '*.mov'):
            matches.append(os.path.join(root, filename))
    return matches
    
    
    
    def fileList():
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.mov', '.MOV', '.avi', '.mpg')):
                matches.append(os.path.join(root, filename))
    return matches