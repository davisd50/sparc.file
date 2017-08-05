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
class ISparcFileReader(interface.Interface):
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

# Bookmark
class ISparcBookmark(interface.Interface):
    def offset():
        """Returns integer offset of last book mark set() call
        
        If set() has not been called, or can not be located then 0 is returned.
        """
    def set(offset):
        """Set the book mark at integer offset.
        """

# Tail
class ISparcFileTail(interface.Interface):
    """Tail a file reader"""
    def tail(reader):
        """Tail a ISparcFileReader provider
        
        Emits ISparcContentAvailableEvent events for new content in reader
        
        Args:
            reader: ISparcFileReader provider
        """
        