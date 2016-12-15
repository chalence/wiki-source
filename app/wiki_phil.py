import urllib2
import sys
from bs4 import BeautifulSoup
import re

def strip_brackets(string):
    """
    remove parenthesis from a string
    leave parenthesis between "<a></a>" tags in place
    """
    string = "" + str(string)
    d = 0
    k = 0
    out = ''
    for i in string:
        #check for tag when not in parantheses mode
        if d < 1:
            if i == '>':
                k-=1
            if i =="<":
                k +=  1
        #check for parentheses
        if k < 1:
            if i == '(':
                    d += 1
            if d > 0:
                    out += ' '
            else:
                    out += i
            if i == ')' :
                    d -= 1
        else:
            out +=i
    return out

class PhilosophyGame():
    
    def __init__(self,verbose=True):
        self.iter=0
        self.path=[]
        self.verbose = verbose
        self.ptitle = re.compile(r'"wgPageName":"(.+?)"')

    def trace(self,article):
        
        site = urllib2.urlopen(article)
        data = site.read()

        self.last = article
        self.lastprefix = self.last[:self.last.find("wiki/")+5]
        wiktionary = False
        if 'wiktionary' in self.lastprefix:
            wiktionary = True
        site.close()
        soup = BeautifulSoup(data)
        
        if self.iter ==0:
            self.title = re.search(self.ptitle,str(soup)).group(1)
        
        current_title = re.search(self.ptitle,str(soup)).group(1)
        #self.path.append(current_title)
        if self.verbose:
            print self.iter, ' ', current_title

        
        for s in soup.find_all('table'):
            s.extract()
        
        pnodes = []
        for node in soup.find(id="bodyContent").find_all('p'):
            # the first undecorated <p> should be the first paragraph
            if node.attrs == {}: 
                pnodes.append(node)
    
    
        num = 0
        for node in pnodes:
            try:                  
                remove = ['span','sup']
                if wiktionary: remove=['sup']
                for s in node.find_all(remove):
                    s.extract()
                stnode = strip_brackets(str(node)) 
                trimmed=BeautifulSoup(stnode)
                links = []
                if not trimmed.find('a'):
                    raise TypeError('no links!')
                for l in trimmed.find_all('a'):
                    links.append(l['href'])
                break
            except TypeError:
                continue
                
        #if links==[]:
        #    print "No links found on page!"
        #    print "Error article:", current_title
        #    print "Starting article:", self.title
        #    sys.exit(1)
        
       
        # to remove articles that don't exist (yet)
        next = [s for s in links if 'redlink' not in s][0]
        
        # it's possible we get linked to wikitionary:
        nextarticle = next[next.find('/wiki')+6:]
        
        
        if 'wiktionary' in next:
            nextlink = 'http://en.wiktionary.org/wiki/'
        else:
            nextlink = 'http://en.wikipedia.org/wiki/'
        nextlink = nextlink + nextarticle
        
        
        if nextarticle == 'Philosophy':
            if self.verbose:
                print "Made it to Philosophy! Number of iterations taken = ", self.iter
            self.path.append(nextarticle)
            return 
        else:
            # does the next article match any previously visited article? Then we're in a loop
            for a in self.path:
                if a==nextarticle:
                    print "Infinite loop!", self.title
                    self.path.extend([nextarticle,'-LOOP-'])
                    return
            self.iter = self.iter + 1
            self.path.append(nextarticle)
            self.trace(nextlink)


# input: name of article
# output: list of the path it took to philosophy
# or None if philosophy is not reached or error occurred
def search_article(article):
    game = PhilosophyGame(verbose=False)
    full_article = "http://en.wikipedia.org/wiki/" + article
    try:
        game.trace(full_article)
        return game.path
    except Exception:
        return None


if __name__ == "__main__":
    article = "Vermont"
    game = PhilosophyGame(verbose=False)
    full_article = "http://en.wikipedia.org/wiki/" + article
    print "source article = ", full_article
    try:
        game.trace(full_article)
        print "path to philosophy = ", game.path
    except Exception:
        print "something went wrong with ", article
