from zope import interface
from zope.interface.interfaces import IObjectEvent

# Events
class ISparcContentAvailableEvent(IObjectEvent):
    """A ISparcFileContent provider is available for processing"""
class ISparcBytesContentAvailableEvent(IObjectEvent):
    """A ISparcBytesFileContent provider is available for processing"""
class ISparcUnicodeContentAvailableEvent(IObjectEvent):
    """A ISparcUnicodeContentAvailableEvent provider is available for processing"""

# File Contents
class ISparcFileContent(interface.Interface):
    """Some content"""
    def contents():
        """Returns either a Bytes, str, or Unicode object"""

class ISparcBytesFileContent(ISparcFileContent):
    """Some content"""
    def contents():
        """Returns Bytes object"""

class ISparcUnicodeFileContent(ISparcFileContent):
    """Some content"""
    def contents():
        """
        Python 3 returns str object.  
        Python 2 returns Unicode object.
        """

# Files
class ISparcFile(interface.Interface):
    def __str__():
        """Informal name of file"""
    def __repr__(other):
        """File identity"""

class ISparcFileReader(ISparcFile):
    """Returns ISparcFileContent provider for read method(s)."""
    def read(self, size):
        """See Python file-like object interface."""
    def seek(self, offset):
        """See Python file-like object interface"""
    def tell(self):
        """See Python file-like object interface"""

class ISparcBytesFile(ISparcFileReader):
    """Returns ISparcBytesFileContent provider for read method(s)."""

class ISparcUnicodeFile(ISparcFileReader):
    """Returns ISparcUnicodeFileContent provider for read method(s)."""
    def readline(size=0):
        """See Python file-like object interface"""
    def next():
        """See Python file-like object interface"""


class ISparcFileContentsLocator(interface.Interface):
    def find(file, contents, end=False):
        """Position ISparcFileReader to first instance of matched contents.
        
        Search starts at current ISparcFileReader provider position and 
        continues to EOF.  ISparcFileReader provider position is unchanged if
        contents can not be located.
        
        Args:
            file: ISparcFileReader provider
            contents: sequence of ISparcFileContent providers to match
            end: True indicates to position ISparcFileReader at end of contents
                 sequence, else position at beginning.
        Rasies:
            ValueError if contents can not be located in ISparcFileReader provider
        """

# Bookmark
class ISparcFileReaderWithBookmark(ISparcFileReader):
    def set_bookmark():
        """Set the book mark position."""
    def goto_bookmark():
        """Go to the last position marked by set() or initial file position
        if set() has not yet been called.
        
        Raises:
            SparcFileBookmarkIndexError if set() position can not be found.
        """

# Tail
class ISparcFileReaderTail(interface.Interface):
    """Tail a file reader"""
    def tail(reader):
        """Tail a ISparcFileReader provider
        
        Emits ISparcContentAvailableEvent event for new content in reader
        
        Args:
            reader: ISparcFileReader provider
        """
        