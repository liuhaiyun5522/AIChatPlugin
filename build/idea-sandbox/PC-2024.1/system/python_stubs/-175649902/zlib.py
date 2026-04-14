# encoding: utf-8
# module zlib
# from /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload/zlib.cpython-312-darwin.so
# by generator 1.147
"""
The functions in this module allow compression and decompression using the
zlib library, which is based on GNU zip.

adler32(string[, start]) -- Compute an Adler-32 checksum.
compress(data[, level]) -- Compress data, with compression level 0-9 or -1.
compressobj([level[, ...]]) -- Return a compressor object.
crc32(string[, start]) -- Compute a CRC-32 checksum.
decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
decompressobj([wbits[, zdict]]) -- Return a decompressor object.

'wbits' is window buffer size and container format.
Compressor objects support compress() and flush() methods; decompressor
objects support decompress() and flush().
"""
# no imports

# Variables with simple values

DEFLATED = 8

DEF_BUF_SIZE = 16384

DEF_MEM_LEVEL = 8

MAX_WBITS = 15

ZLIB_RUNTIME_VERSION = '1.2.12'

ZLIB_VERSION = '1.2.11'

Z_BEST_COMPRESSION = 9
Z_BEST_SPEED = 1

Z_BLOCK = 5

Z_DEFAULT_COMPRESSION = -1
Z_DEFAULT_STRATEGY = 0

Z_FILTERED = 1
Z_FINISH = 4
Z_FIXED = 4

Z_FULL_FLUSH = 3

Z_HUFFMAN_ONLY = 2

Z_NO_COMPRESSION = 0
Z_NO_FLUSH = 0

Z_PARTIAL_FLUSH = 1

Z_RLE = 3

Z_SYNC_FLUSH = 2

Z_TREES = 6

__version__ = '1.0'

# functions

def adler32(*args, **kwargs): # real signature unknown
    """
    Compute an Adler-32 checksum of data.
    
      value
        Starting value of the checksum.
    
    The returned checksum is an integer.
    """
    pass

def compress(*args, **kwargs): # real signature unknown
    """
    Returns a bytes object containing compressed data.
    
      data
        Binary data to be compressed.
      level
        Compression level, in 0-9 or -1.
      wbits
        The window buffer size and container format.
    """
    pass

def compressobj(*args, **kwargs): # real signature unknown
    """
    Return a compressor object.
    
      level
        The compression level (an integer in the range 0-9 or -1; default is
        currently equivalent to 6).  Higher compression levels are slower,
        but produce smaller results.
      method
        The compression algorithm.  If given, this must be DEFLATED.
      wbits
        +9 to +15: The base-two logarithm of the window size.  Include a zlib
            container.
        -9 to -15: Generate a raw stream.
        +25 to +31: Include a gzip container.
      memLevel
        Controls the amount of memory used for internal compression state.
        Valid values range from 1 to 9.  Higher values result in higher memory
        usage, faster compression, and smaller output.
      strategy
        Used to tune the compression algorithm.  Possible values are
        Z_DEFAULT_STRATEGY, Z_FILTERED, and Z_HUFFMAN_ONLY.
      zdict
        The predefined compression dictionary - a sequence of bytes
        containing subsequences that are likely to occur in the input data.
    """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """
    Compute a CRC-32 checksum of data.
    
      value
        Starting value of the checksum.
    
    The returned checksum is an integer.
    """
    pass

def decompress(*args, **kwargs): # real signature unknown
    """
    Returns a bytes object containing the uncompressed data.
    
      data
        Compressed data.
      wbits
        The window buffer size and container format.
      bufsize
        The initial output buffer size.
    """
    pass

def decompressobj(*args, **kwargs): # real signature unknown
    """
    Return a decompressor object.
    
      wbits
        The window buffer size and container format.
      zdict
        The predefined compression dictionary.  This must be the same
        dictionary as used by the compressor that produced the input data.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class _ZlibDecompressor(object):
    """
    Create a decompressor object for decompressing data incrementally.
    
      wbits = 15
      zdict
         The predefined compression dictionary. This is a sequence of bytes
         (such as a bytes object) containing subsequences that are expected
         to occur frequently in the data that is to be compressed. Those
         subsequences that are expected to be most common should come at the
         end of the dictionary. This must be the same dictionary as used by the
         compressor that produced the input data.
    """
    def decompress(self): # real signature unknown; restored from __doc__
        """
        Decompress *data*, returning uncompressed data as bytes.
        
        If *max_length* is nonnegative, returns at most *max_length* bytes of
        decompressed data. If this limit is reached and further output can be
        produced, *self.needs_input* will be set to ``False``. In this case, the next
        call to *decompress()* may provide *data* as b'' to obtain more of the output.
        
        If all of the input data was decompressed and returned (either because this
        was less than *max_length* bytes, or because *max_length* was negative),
        *self.needs_input* will be set to True.
        
        Attempting to decompress data after the end of stream is reached raises an
        EOFError.  Any data found after the end of the stream is ignored and saved in
        the unused_data attribute.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the end-of-stream marker has been reached."""

    needs_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if more input is needed before more decompressed data can be produced."""

    unused_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data found after the end of the compressed stream."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x102ba4e00>'

__spec__ = None # (!) real value is "ModuleSpec(name='zlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x102ba4e00>, origin='/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload/zlib.cpython-312-darwin.so')"

