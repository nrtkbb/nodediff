# -*- coding: utf-8 -*-
import os
import sys
from itertools import ifilter
from difflib import Differ
from pprint import pprint


ROOT='___root___'


class Node(object):
    def __init__(self, name, parent=None, nodetype=None):
        self.name = name
        self.parent = parent
        self.nodetype = nodetype
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def compareStr(self, indent=''):
        res = '{0}{1}({2})\n'.format(indent, self.name, self.nodetype)
        for child in sorted(self.children, key=lambda n:n.name):
            res += child.compareStr(indent + '    ')
        return res

    def __str__(self):
        return self.dumps()

    def dumps(self, indent='', end='}'):
        indent2 = indent + '    '
        res = '\n' + indent + '{\n' + indent2 + '"class": "%s",\n' % self.__class__.__name__
        res += indent2 + '"id": "@0x%X",\n' % id(self)
        res += indent2 + '"name": "%s",\n' % self.name
        if self.parent is None:
            res += indent2 + '"parent": "%s",\n' % None
        else:
            res += indent2 + '"parent": "%s",\n' % self.parent.name
        res += indent2 + '"nodetype": "%s",\n' % self.nodetype
        if 0 < len(self.children):
            res += indent2 + '"children": ['
            for child in self.children:
                if child is self.children[-1]:
                    res += child.dumps(indent=indent2, end='}]')
                else:
                    res += child.dumps(indent=indent2, end='},')
            res += '\n' + indent + end
        else:
            res += indent2 + '"children": []\n' + indent + end
        return res


    @staticmethod
    def jointree(name, parentname, nodetype, roottree):
        if '|' == parentname[0]:
            Node.__jointreeFullPath(name, parentname, nodetype, roottree)
        else:
            Node.__jointreeUnique(name, parentname, nodetype, roottree)

    @classmethod
    def __jointreeUnique(cls, name, parentname, nodetype, tree):
        if tree.name == parentname:
            node = Node(name, tree, nodetype)
            tree.addChild(node)
            return
        for child in tree.children:
            Node.__jointreeUnique(name, parentname, nodetype, child)

    @classmethod
    def __jointreeFullPath(cls, name, parentname, nodetype, tree):
        # parentname == '|root|parent|child' みたいな時の処理
        parents = parentname[1:].split('|')
        tmptree = tree
        for parent in parents:
            tmptree = next(ifilter(lambda x:x.name == parent, tmptree.children), None)
        node = Node(name, tmptree, nodetype)
        tmptree.addChild(node)


def createNodeParser(line):
    # line = 'createNode transform -n "hoge" -s -p "aa";\n'
    tokens = line[:-2].split()
    nameflag = False
    parentflag = False
    name = ''
    parent = ROOT
    nodetype = tokens[1]
    for token in tokens[2:]:
        if '-n' == token:
            nameflag = True
            continue
        if '-p' == token:
            parentflag = True
            continue
        if nameflag:
            name = token.strip('"')
            nameflag = False
            continue
        if parentflag:
            parent = token.strip('"')
            parentflag = False
            continue
    return (name, parent, nodetype)


def buildNodeTreeFils(path, fils):
    roottree = Node(ROOT)
    try:
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                if 'createNode' == line[:10]:
                    (name, parentname, nodetype) = createNodeParser(line)
                    if nodetype in fils:
                        Node.jointree(name, parentname, nodetype, roottree)
                line = f.readline()
    except IOError:
        raise u'Not allowed to write files to this path "%s".' % path
    return roottree


def nodediff(patha, pathb, diffonly=False, whitelist=['transform', 'mesh', 'nurbsSurface', 'nurbsCurve']):
    if not os.path.exists(patha):
        raise Exception(u'%s is not exists. exit.' % patha)
    if not os.path.exists(pathb):
        raise Exception(u'%s is not exists. exit.' % pathb)

    treea = buildNodeTreeFils(patha, whitelist)
    treeb = buildNodeTreeFils(pathb, whitelist)

    d = Differ()
    result = list(d.compare(treea.compareStr().split('\n'), treeb.compareStr().split('\n')))
    if diffonly:
        pprint(filter(lambda x:x[0]!=' ', result))
    else:
        pprint(result)


if __name__ == '__main__':
    patha = sys.argv[1]
    pathb = sys.argv[2]
    whitelist = sys.argv[3].split(',')
    if len(sys.argv) is 5 and 'diffonly' == sys.argv[4]:
        nodediff(patha, pathb, diffonly=True, whitelist=whitelist)
    else:
        nodediff(patha, pathb, diffonly=False, whitelist=whitelist)
