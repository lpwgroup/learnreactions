"""
setup.py: Install nanoreactor learning script.  
"""
VERSION=0.1
__author__ = "Lee-Ping Wang, Alexey Titov, Leah Bendavid, Robert McGibbon, Todd J. Martinez"
__version__ = "%.1f"%VERSION

import os, sys
from distutils.core import setup,Extension
import numpy
import glob

requirements = ['numpy', 'networkx']

def buildKeywordDictionary():
    from distutils.core import Extension
    setupKeywords = {}
    setupKeywords["name"]              = "learnreactions"
    setupKeywords["version"]           = "%.1f" %VERSION
    setupKeywords["author"]            = __author__
    setupKeywords["author_email"]      = "leeping@ucdavis.edu"
    setupKeywords["license"]           = "BSD 3-Clause"
    setupKeywords["packages"]          = ["learnreactions"]
    setupKeywords["package_dir"]       = {"learnreactions": "src"}
    setupKeywords["scripts"]           = glob.glob("bin/*.py") + glob.glob("bin/*.sh") + glob.glob("bin/*.exe")
    setupKeywords["platforms"]         = ["Linux"]
    setupKeywords["description"]       = "Identify reaction events in reactive MD simulations."
    outputString=""
    firstTab     = 40
    secondTab    = 60
    for key in sorted( setupKeywords.iterkeys() ):
         value         = setupKeywords[key]
         outputString += key.rjust(firstTab) + str( value ).rjust(secondTab) + "\n"
    print "%s" % outputString
    return setupKeywords
    

def main():
    setup_keywords = buildKeywordDictionary()
    setup(**setup_keywords)
    for requirement in requirements:
      try:
          exec('import %s' % requirement)
      except ImportError as e:
          print >> sys.stderr, '\nWarning: Could not import %s' % e
          print >> sys.stderr, 'Warning: Some package functionality may not work'

if __name__ == '__main__':
    main()

