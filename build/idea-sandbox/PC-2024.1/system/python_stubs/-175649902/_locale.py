# encoding: utf-8
# module _locale
# from (built-in)
# by generator 1.147
""" Support for POSIX locales. """
# no imports

# Variables with simple values

ABDAY_1 = 14
ABDAY_2 = 15
ABDAY_3 = 16
ABDAY_4 = 17
ABDAY_5 = 18
ABDAY_6 = 19
ABDAY_7 = 20

ABMON_1 = 33
ABMON_10 = 42
ABMON_11 = 43
ABMON_12 = 44
ABMON_2 = 34
ABMON_3 = 35
ABMON_4 = 36
ABMON_5 = 37
ABMON_6 = 38
ABMON_7 = 39
ABMON_8 = 40
ABMON_9 = 41

ALT_DIGITS = 49

AM_STR = 5

CHAR_MAX = 127

CODESET = 0

CRNCYSTR = 56

DAY_1 = 7
DAY_2 = 8
DAY_3 = 9
DAY_4 = 10
DAY_5 = 11
DAY_6 = 12
DAY_7 = 13

D_FMT = 2

D_T_FMT = 1

ERA = 45

ERA_D_FMT = 46

ERA_D_T_FMT = 47

ERA_T_FMT = 48

LC_ALL = 0
LC_COLLATE = 1
LC_CTYPE = 2
LC_MESSAGES = 6
LC_MONETARY = 3
LC_NUMERIC = 4
LC_TIME = 5

MON_1 = 21
MON_10 = 30
MON_11 = 31
MON_12 = 32
MON_2 = 22
MON_3 = 23
MON_4 = 24
MON_5 = 25
MON_6 = 26
MON_7 = 27
MON_8 = 28
MON_9 = 29

NOEXPR = 53

PM_STR = 6

RADIXCHAR = 50

THOUSEP = 51

T_FMT = 3

T_FMT_AMPM = 4

YESEXPR = 52

# functions

def getencoding(*args, **kwargs): # real signature unknown
    """ Get the current locale encoding. """
    pass

def localeconv(*args, **kwargs): # real signature unknown
    """ Returns numeric and monetary locale-specific parameters. """
    pass

def nl_langinfo(*args, **kwargs): # real signature unknown
    """ Return the value for the locale information associated with key. """
    pass

def setlocale(*args, **kwargs): # real signature unknown
    """ Activates/queries locale processing. """
    pass

def strcoll(*args, **kwargs): # real signature unknown
    """ Compares two strings according to the locale. """
    pass

def strxfrm(*args, **kwargs): # real signature unknown
    """ Return a string that can be used as a key for locale-aware comparisons. """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x1043aef20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x1043aefc0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x1043af060>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x1043af1a0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x1043af2e0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x1043af420>)>, 'load_module': <classmethod(<function _load_module_shim at 0x1043ae2a0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_locale', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

