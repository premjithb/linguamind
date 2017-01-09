# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_linalg')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_linalg')
    _linalg = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_linalg', [dirname(__file__)])
        except ImportError:
            import _linalg
            return _linalg
        try:
            _mod = imp.load_module('_linalg', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _linalg = swig_import_helper()
    del swig_import_helper
else:
    import _linalg
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _linalg.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _linalg.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _linalg.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _linalg.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _linalg.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _linalg.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _linalg.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _linalg.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _linalg.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _linalg.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _linalg.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _linalg.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _linalg.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _linalg.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _linalg.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _linalg.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _linalg.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _linalg.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectori(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectori, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectori, name)
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _linalg.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _linalg.vectori___nonzero__(self)

    def __bool__(self) -> "bool":
        return _linalg.vectori___bool__(self)

    def __len__(self) -> "std::vector< int >::size_type":
        return _linalg.vectori___len__(self)

    def __getslice__(self, i: 'std::vector< int >::difference_type', j: 'std::vector< int >::difference_type') -> "std::vector< int,std::allocator< int > > *":
        return _linalg.vectori___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _linalg.vectori___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< int >::difference_type', j: 'std::vector< int >::difference_type') -> "void":
        return _linalg.vectori___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _linalg.vectori___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< int >::value_type const &":
        return _linalg.vectori___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _linalg.vectori___setitem__(self, *args)

    def pop(self) -> "std::vector< int >::value_type":
        return _linalg.vectori_pop(self)

    def append(self, x: 'std::vector< int >::value_type const &') -> "void":
        return _linalg.vectori_append(self, x)

    def empty(self) -> "bool":
        return _linalg.vectori_empty(self)

    def size(self) -> "std::vector< int >::size_type":
        return _linalg.vectori_size(self)

    def swap(self, v: 'vectori') -> "void":
        return _linalg.vectori_swap(self, v)

    def begin(self) -> "std::vector< int >::iterator":
        return _linalg.vectori_begin(self)

    def end(self) -> "std::vector< int >::iterator":
        return _linalg.vectori_end(self)

    def rbegin(self) -> "std::vector< int >::reverse_iterator":
        return _linalg.vectori_rbegin(self)

    def rend(self) -> "std::vector< int >::reverse_iterator":
        return _linalg.vectori_rend(self)

    def clear(self) -> "void":
        return _linalg.vectori_clear(self)

    def get_allocator(self) -> "std::vector< int >::allocator_type":
        return _linalg.vectori_get_allocator(self)

    def pop_back(self) -> "void":
        return _linalg.vectori_pop_back(self)

    def erase(self, *args) -> "std::vector< int >::iterator":
        return _linalg.vectori_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectori(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x: 'std::vector< int >::value_type const &') -> "void":
        return _linalg.vectori_push_back(self, x)

    def front(self) -> "std::vector< int >::value_type const &":
        return _linalg.vectori_front(self)

    def back(self) -> "std::vector< int >::value_type const &":
        return _linalg.vectori_back(self)

    def assign(self, n: 'std::vector< int >::size_type', x: 'std::vector< int >::value_type const &') -> "void":
        return _linalg.vectori_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _linalg.vectori_resize(self, *args)

    def insert(self, *args) -> "void":
        return _linalg.vectori_insert(self, *args)

    def reserve(self, n: 'std::vector< int >::size_type') -> "void":
        return _linalg.vectori_reserve(self, n)

    def capacity(self) -> "std::vector< int >::size_type":
        return _linalg.vectori_capacity(self)
    __swig_destroy__ = _linalg.delete_vectori
    __del__ = lambda self: None
vectori_swigregister = _linalg.vectori_swigregister
vectori_swigregister(vectori)

class vectorf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorf, name)
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _linalg.vectorf_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _linalg.vectorf___nonzero__(self)

    def __bool__(self) -> "bool":
        return _linalg.vectorf___bool__(self)

    def __len__(self) -> "std::vector< float >::size_type":
        return _linalg.vectorf___len__(self)

    def __getslice__(self, i: 'std::vector< float >::difference_type', j: 'std::vector< float >::difference_type') -> "std::vector< float,std::allocator< float > > *":
        return _linalg.vectorf___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _linalg.vectorf___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< float >::difference_type', j: 'std::vector< float >::difference_type') -> "void":
        return _linalg.vectorf___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _linalg.vectorf___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< float >::value_type const &":
        return _linalg.vectorf___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _linalg.vectorf___setitem__(self, *args)

    def pop(self) -> "std::vector< float >::value_type":
        return _linalg.vectorf_pop(self)

    def append(self, x: 'std::vector< float >::value_type const &') -> "void":
        return _linalg.vectorf_append(self, x)

    def empty(self) -> "bool":
        return _linalg.vectorf_empty(self)

    def size(self) -> "std::vector< float >::size_type":
        return _linalg.vectorf_size(self)

    def swap(self, v: 'vectorf') -> "void":
        return _linalg.vectorf_swap(self, v)

    def begin(self) -> "std::vector< float >::iterator":
        return _linalg.vectorf_begin(self)

    def end(self) -> "std::vector< float >::iterator":
        return _linalg.vectorf_end(self)

    def rbegin(self) -> "std::vector< float >::reverse_iterator":
        return _linalg.vectorf_rbegin(self)

    def rend(self) -> "std::vector< float >::reverse_iterator":
        return _linalg.vectorf_rend(self)

    def clear(self) -> "void":
        return _linalg.vectorf_clear(self)

    def get_allocator(self) -> "std::vector< float >::allocator_type":
        return _linalg.vectorf_get_allocator(self)

    def pop_back(self) -> "void":
        return _linalg.vectorf_pop_back(self)

    def erase(self, *args) -> "std::vector< float >::iterator":
        return _linalg.vectorf_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectorf(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x: 'std::vector< float >::value_type const &') -> "void":
        return _linalg.vectorf_push_back(self, x)

    def front(self) -> "std::vector< float >::value_type const &":
        return _linalg.vectorf_front(self)

    def back(self) -> "std::vector< float >::value_type const &":
        return _linalg.vectorf_back(self)

    def assign(self, n: 'std::vector< float >::size_type', x: 'std::vector< float >::value_type const &') -> "void":
        return _linalg.vectorf_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _linalg.vectorf_resize(self, *args)

    def insert(self, *args) -> "void":
        return _linalg.vectorf_insert(self, *args)

    def reserve(self, n: 'std::vector< float >::size_type') -> "void":
        return _linalg.vectorf_reserve(self, n)

    def capacity(self) -> "std::vector< float >::size_type":
        return _linalg.vectorf_capacity(self)
    __swig_destroy__ = _linalg.delete_vectorf
    __del__ = lambda self: None
vectorf_swigregister = _linalg.vectorf_swigregister
vectorf_swigregister(vectorf)

class vectord(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectord, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectord, name)
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _linalg.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _linalg.vectord___nonzero__(self)

    def __bool__(self) -> "bool":
        return _linalg.vectord___bool__(self)

    def __len__(self) -> "std::vector< double >::size_type":
        return _linalg.vectord___len__(self)

    def __getslice__(self, i: 'std::vector< double >::difference_type', j: 'std::vector< double >::difference_type') -> "std::vector< double,std::allocator< double > > *":
        return _linalg.vectord___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _linalg.vectord___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< double >::difference_type', j: 'std::vector< double >::difference_type') -> "void":
        return _linalg.vectord___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _linalg.vectord___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< double >::value_type const &":
        return _linalg.vectord___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _linalg.vectord___setitem__(self, *args)

    def pop(self) -> "std::vector< double >::value_type":
        return _linalg.vectord_pop(self)

    def append(self, x: 'std::vector< double >::value_type const &') -> "void":
        return _linalg.vectord_append(self, x)

    def empty(self) -> "bool":
        return _linalg.vectord_empty(self)

    def size(self) -> "std::vector< double >::size_type":
        return _linalg.vectord_size(self)

    def swap(self, v: 'vectord') -> "void":
        return _linalg.vectord_swap(self, v)

    def begin(self) -> "std::vector< double >::iterator":
        return _linalg.vectord_begin(self)

    def end(self) -> "std::vector< double >::iterator":
        return _linalg.vectord_end(self)

    def rbegin(self) -> "std::vector< double >::reverse_iterator":
        return _linalg.vectord_rbegin(self)

    def rend(self) -> "std::vector< double >::reverse_iterator":
        return _linalg.vectord_rend(self)

    def clear(self) -> "void":
        return _linalg.vectord_clear(self)

    def get_allocator(self) -> "std::vector< double >::allocator_type":
        return _linalg.vectord_get_allocator(self)

    def pop_back(self) -> "void":
        return _linalg.vectord_pop_back(self)

    def erase(self, *args) -> "std::vector< double >::iterator":
        return _linalg.vectord_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectord(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x: 'std::vector< double >::value_type const &') -> "void":
        return _linalg.vectord_push_back(self, x)

    def front(self) -> "std::vector< double >::value_type const &":
        return _linalg.vectord_front(self)

    def back(self) -> "std::vector< double >::value_type const &":
        return _linalg.vectord_back(self)

    def assign(self, n: 'std::vector< double >::size_type', x: 'std::vector< double >::value_type const &') -> "void":
        return _linalg.vectord_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _linalg.vectord_resize(self, *args)

    def insert(self, *args) -> "void":
        return _linalg.vectord_insert(self, *args)

    def reserve(self, n: 'std::vector< double >::size_type') -> "void":
        return _linalg.vectord_reserve(self, n)

    def capacity(self) -> "std::vector< double >::size_type":
        return _linalg.vectord_capacity(self)
    __swig_destroy__ = _linalg.delete_vectord
    __del__ = lambda self: None
vectord_swigregister = _linalg.vectord_swigregister
vectord_swigregister(vectord)

class charp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, charp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, charp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _linalg.new_charp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _linalg.delete_charp
    __del__ = lambda self: None

    def assign(self, value: 'char') -> "void":
        return _linalg.charp_assign(self, value)

    def value(self) -> "char":
        return _linalg.charp_value(self)

    def cast(self) -> "char *":
        return _linalg.charp_cast(self)
    if _newclass:
        frompointer = staticmethod(_linalg.charp_frompointer)
    else:
        frompointer = _linalg.charp_frompointer
charp_swigregister = _linalg.charp_swigregister
charp_swigregister(charp)

def charp_frompointer(t: 'char *') -> "charp *":
    return _linalg.charp_frompointer(t)
charp_frompointer = _linalg.charp_frompointer

class Seed(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Seed, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Seed, name)
    __repr__ = _swig_repr

    def __init__(self, seed: 'unsigned long long'):
        this = _linalg.new_Seed(seed)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["seed"] = _linalg.Seed_seed_set
    __swig_getmethods__["seed"] = _linalg.Seed_seed_get
    if _newclass:
        seed = _swig_property(_linalg.Seed_seed_get, _linalg.Seed_seed_set)

    def eat(self) -> "void":
        return _linalg.Seed_eat(self)
    __swig_destroy__ = _linalg.delete_Seed
    __del__ = lambda self: None
Seed_swigregister = _linalg.Seed_swigregister
Seed_swigregister(Seed)

class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr

    def __init__(self, size: 'int'):
        this = _linalg.new_Vector(size)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["size"] = _linalg.Vector_size_set
    __swig_getmethods__["size"] = _linalg.Vector_size_get
    if _newclass:
        size = _swig_property(_linalg.Vector_size_get, _linalg.Vector_size_set)
    __swig_setmethods__["_data"] = _linalg.Vector__data_set
    __swig_getmethods__["_data"] = _linalg.Vector__data_get
    if _newclass:
        _data = _swig_property(_linalg.Vector__data_get, _linalg.Vector__data_set)

    def resize(self, size: 'int') -> "Vector":
        return _linalg.Vector_resize(self, size)

    def zero(self) -> "Vector":
        return _linalg.Vector_zero(self)

    def uniform(self, seed: 'Seed') -> "Vector":
        return _linalg.Vector_uniform(self, seed)

    def get(self, *args) -> "float":
        return _linalg.Vector_get(self, *args)

    def dot(self, x: 'Vector') -> "float":
        return _linalg.Vector_dot(self, x)

    def doti(self, i: 'int', x: 'Vector', y: 'Vector') -> "void":
        return _linalg.Vector_doti(self, i, x, y)

    def set(self, *args) -> "Vector":
        return _linalg.Vector_set(self, *args)

    def muli(self, *args) -> "Vector":
        return _linalg.Vector_muli(self, *args)

    def __imul__(self, *args) -> "Vector":
        return _linalg.Vector___imul__(self, *args)

    def divi(self, *args) -> "Vector":
        return _linalg.Vector_divi(self, *args)

    def __itruediv__(self, *args):
        return _linalg.Vector___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def addi(self, *args) -> "Vector":
        return _linalg.Vector_addi(self, *args)

    def __iadd__(self, *args) -> "Vector":
        return _linalg.Vector___iadd__(self, *args)

    def subi(self, *args) -> "Vector":
        return _linalg.Vector_subi(self, *args)

    def __isub__(self, *args) -> "Vector":
        return _linalg.Vector___isub__(self, *args)

    def gei(self, *args) -> "Vector":
        return _linalg.Vector_gei(self, *args)

    def __ge__(self, *args) -> "Vector":
        return _linalg.Vector___ge__(self, *args)

    def lei(self, *args) -> "Vector":
        return _linalg.Vector_lei(self, *args)

    def __le__(self, *args) -> "Vector":
        return _linalg.Vector___le__(self, *args)

    def gti(self, *args) -> "Vector":
        return _linalg.Vector_gti(self, *args)

    def __gt__(self, *args) -> "Vector":
        return _linalg.Vector___gt__(self, *args)

    def lti(self, *args) -> "Vector":
        return _linalg.Vector_lti(self, *args)

    def __lt__(self, *args) -> "Vector":
        return _linalg.Vector___lt__(self, *args)

    def __getitem__(self, i: 'int') -> "float":
        return _linalg.Vector___getitem__(self, i)

    def __setitem__(self, key: 'int', item: 'float') -> "void":
        return _linalg.Vector___setitem__(self, key, item)

    def __len__(self) -> "int":
        return _linalg.Vector___len__(self)
    __swig_destroy__ = _linalg.delete_Vector
    __del__ = lambda self: None
Vector_swigregister = _linalg.Vector_swigregister
Vector_swigregister(Vector)

class Matrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matrix, name)
    __repr__ = _swig_repr

    def __init__(self, rows: 'int', cols: 'int'):
        this = _linalg.new_Matrix(rows, cols)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["rows"] = _linalg.Matrix_rows_set
    __swig_getmethods__["rows"] = _linalg.Matrix_rows_get
    if _newclass:
        rows = _swig_property(_linalg.Matrix_rows_get, _linalg.Matrix_rows_set)
    __swig_setmethods__["cols"] = _linalg.Matrix_cols_set
    __swig_getmethods__["cols"] = _linalg.Matrix_cols_get
    if _newclass:
        cols = _swig_property(_linalg.Matrix_cols_get, _linalg.Matrix_cols_set)
    __swig_setmethods__["_data"] = _linalg.Matrix__data_set
    __swig_getmethods__["_data"] = _linalg.Matrix__data_get
    if _newclass:
        _data = _swig_property(_linalg.Matrix__data_get, _linalg.Matrix__data_set)

    def zero(self) -> "Matrix":
        return _linalg.Matrix_zero(self)

    def uniform(self, seed: 'Seed') -> "Matrix":
        return _linalg.Matrix_uniform(self, seed)

    def __imul__(self, *args) -> "Matrix":
        return _linalg.Matrix___imul__(self, *args)

    def __itruediv__(self, *args):
        return _linalg.Matrix___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __iadd__(self, *args) -> "Matrix":
        return _linalg.Matrix___iadd__(self, *args)

    def __isub__(self, *args) -> "Matrix":
        return _linalg.Matrix___isub__(self, *args)

    def __getitem__(self, i: 'int') -> "Vector *":
        return _linalg.Matrix___getitem__(self, i)

    def __setitem__(self, key: 'int', item: 'Vector') -> "void":
        return _linalg.Matrix___setitem__(self, key, item)

    def __len__(self) -> "int":
        return _linalg.Matrix___len__(self)
    __swig_destroy__ = _linalg.delete_Matrix
    __del__ = lambda self: None
Matrix_swigregister = _linalg.Matrix_swigregister
Matrix_swigregister(Matrix)

class Tensor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tensor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tensor, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _linalg.new_Tensor(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["shape"] = _linalg.Tensor_shape_set
    __swig_getmethods__["shape"] = _linalg.Tensor_shape_get
    if _newclass:
        shape = _swig_property(_linalg.Tensor_shape_get, _linalg.Tensor_shape_set)
    __swig_setmethods__["ndims"] = _linalg.Tensor_ndims_set
    __swig_getmethods__["ndims"] = _linalg.Tensor_ndims_get
    if _newclass:
        ndims = _swig_property(_linalg.Tensor_ndims_get, _linalg.Tensor_ndims_set)
    __swig_setmethods__["_data"] = _linalg.Tensor__data_set
    __swig_getmethods__["_data"] = _linalg.Tensor__data_get
    if _newclass:
        _data = _swig_property(_linalg.Tensor__data_get, _linalg.Tensor__data_set)
    __swig_setmethods__["num_elements"] = _linalg.Tensor_num_elements_set
    __swig_getmethods__["num_elements"] = _linalg.Tensor_num_elements_get
    if _newclass:
        num_elements = _swig_property(_linalg.Tensor_num_elements_get, _linalg.Tensor_num_elements_set)
    __swig_setmethods__["seed"] = _linalg.Tensor_seed_set
    __swig_getmethods__["seed"] = _linalg.Tensor_seed_get
    if _newclass:
        seed = _swig_property(_linalg.Tensor_seed_get, _linalg.Tensor_seed_set)

    def init(self, shape: 'vectori') -> "void":
        return _linalg.Tensor_init(self, shape)

    def dotRow(self, a: 'Tensor', index: 'int') -> "float":
        return _linalg.Tensor_dotRow(self, a, index)

    def addRowi(self, a: 'Tensor', index: 'int') -> "Tensor":
        return _linalg.Tensor_addRowi(self, a, index)

    def sub(self, a: 'Tensor', b: 'Tensor') -> "Tensor":
        return _linalg.Tensor_sub(self, a, b)

    def uniform(self) -> "Tensor":
        return _linalg.Tensor_uniform(self)

    def zero(self) -> "Tensor":
        return _linalg.Tensor_zero(self)

    def get(self, x: 'int') -> "float":
        return _linalg.Tensor_get(self, x)

    def set(self, x: 'int', y: 'float') -> "void":
        return _linalg.Tensor_set(self, x, y)

    def __imul__(self, x: 'float') -> "Tensor":
        return _linalg.Tensor___imul__(self, x)

    def __itruediv__(self, *args):
        return _linalg.Tensor___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __iadd__(self, x: 'float') -> "Tensor":
        return _linalg.Tensor___iadd__(self, x)

    def __isub__(self, x: 'float') -> "Tensor":
        return _linalg.Tensor___isub__(self, x)
    __swig_destroy__ = _linalg.delete_Tensor
    __del__ = lambda self: None
Tensor_swigregister = _linalg.Tensor_swigregister
Tensor_swigregister(Tensor)

# This file is compatible with both classic and new-style classes.


