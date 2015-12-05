'''
Created on Oct 4, 2015

@author: cptullio
'''


if __name__ == '__main__':
    paths = [set([('1', '2'), ('2', '3'), ('3', '4')]),set([('1', '5'), ('5', '3'), ('3', '4')])]
    for path in paths:
        nodesinPath = set();
    
        for node in path:
            nodesinPath.add(node[0])
            nodesinPath.add(node[1])
        print nodesinPath
    
    