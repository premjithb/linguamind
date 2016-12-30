# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_linalg', [dirname(__file__)])
        except ImportError:
            import _linalg
            return _linalg
        if fp is not None:
            try:
                _mod = imp.load_module('_linalg', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _linalg = swig_import_helper()
    del swig_import_helper
else:
    import _linalg
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


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


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
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

    def value(self):
        return _linalg.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _linalg.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _linalg.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _linalg.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _linalg.SwigPyIterator_equal(self, x)

    def copy(self):
        return _linalg.SwigPyIterator_copy(self)

    def next(self):
        return _linalg.SwigPyIterator_next(self)

    def __next__(self):
        return _linalg.SwigPyIterator___next__(self)

    def previous(self):
        return _linalg.SwigPyIterator_previous(self)

    def advance(self, n):
        return _linalg.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _linalg.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _linalg.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _linalg.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _linalg.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _linalg.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
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

    def iterator(self):
        return _linalg.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _linalg.vectori___nonzero__(self)

    def __bool__(self):
        return _linalg.vectori___bool__(self)

    def __len__(self):
        return _linalg.vectori___len__(self)

    def pop(self):
        return _linalg.vectori_pop(self)

    def __getslice__(self, i, j):
        return _linalg.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _linalg.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _linalg.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _linalg.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _linalg.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _linalg.vectori___setitem__(self, *args)

    def append(self, x):
        return _linalg.vectori_append(self, x)

    def empty(self):
        return _linalg.vectori_empty(self)

    def size(self):
        return _linalg.vectori_size(self)

    def clear(self):
        return _linalg.vectori_clear(self)

    def swap(self, v):
        return _linalg.vectori_swap(self, v)

    def get_allocator(self):
        return _linalg.vectori_get_allocator(self)

    def begin(self):
        return _linalg.vectori_begin(self)

    def end(self):
        return _linalg.vectori_end(self)

    def rbegin(self):
        return _linalg.vectori_rbegin(self)

    def rend(self):
        return _linalg.vectori_rend(self)

    def pop_back(self):
        return _linalg.vectori_pop_back(self)

    def erase(self, *args):
        return _linalg.vectori_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectori(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _linalg.vectori_push_back(self, x)

    def front(self):
        return _linalg.vectori_front(self)

    def back(self):
        return _linalg.vectori_back(self)

    def assign(self, n, x):
        return _linalg.vectori_assign(self, n, x)

    def resize(self, *args):
        return _linalg.vectori_resize(self, *args)

    def insert(self, *args):
        return _linalg.vectori_insert(self, *args)

    def reserve(self, n):
        return _linalg.vectori_reserve(self, n)

    def capacity(self):
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

    def iterator(self):
        return _linalg.vectorf_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _linalg.vectorf___nonzero__(self)

    def __bool__(self):
        return _linalg.vectorf___bool__(self)

    def __len__(self):
        return _linalg.vectorf___len__(self)

    def pop(self):
        return _linalg.vectorf_pop(self)

    def __getslice__(self, i, j):
        return _linalg.vectorf___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _linalg.vectorf___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _linalg.vectorf___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _linalg.vectorf___delitem__(self, *args)

    def __getitem__(self, *args):
        return _linalg.vectorf___getitem__(self, *args)

    def __setitem__(self, *args):
        return _linalg.vectorf___setitem__(self, *args)

    def append(self, x):
        return _linalg.vectorf_append(self, x)

    def empty(self):
        return _linalg.vectorf_empty(self)

    def size(self):
        return _linalg.vectorf_size(self)

    def clear(self):
        return _linalg.vectorf_clear(self)

    def swap(self, v):
        return _linalg.vectorf_swap(self, v)

    def get_allocator(self):
        return _linalg.vectorf_get_allocator(self)

    def begin(self):
        return _linalg.vectorf_begin(self)

    def end(self):
        return _linalg.vectorf_end(self)

    def rbegin(self):
        return _linalg.vectorf_rbegin(self)

    def rend(self):
        return _linalg.vectorf_rend(self)

    def pop_back(self):
        return _linalg.vectorf_pop_back(self)

    def erase(self, *args):
        return _linalg.vectorf_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectorf(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _linalg.vectorf_push_back(self, x)

    def front(self):
        return _linalg.vectorf_front(self)

    def back(self):
        return _linalg.vectorf_back(self)

    def assign(self, n, x):
        return _linalg.vectorf_assign(self, n, x)

    def resize(self, *args):
        return _linalg.vectorf_resize(self, *args)

    def insert(self, *args):
        return _linalg.vectorf_insert(self, *args)

    def reserve(self, n):
        return _linalg.vectorf_reserve(self, n)

    def capacity(self):
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

    def iterator(self):
        return _linalg.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _linalg.vectord___nonzero__(self)

    def __bool__(self):
        return _linalg.vectord___bool__(self)

    def __len__(self):
        return _linalg.vectord___len__(self)

    def pop(self):
        return _linalg.vectord_pop(self)

    def __getslice__(self, i, j):
        return _linalg.vectord___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _linalg.vectord___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _linalg.vectord___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _linalg.vectord___delitem__(self, *args)

    def __getitem__(self, *args):
        return _linalg.vectord___getitem__(self, *args)

    def __setitem__(self, *args):
        return _linalg.vectord___setitem__(self, *args)

    def append(self, x):
        return _linalg.vectord_append(self, x)

    def empty(self):
        return _linalg.vectord_empty(self)

    def size(self):
        return _linalg.vectord_size(self)

    def clear(self):
        return _linalg.vectord_clear(self)

    def swap(self, v):
        return _linalg.vectord_swap(self, v)

    def get_allocator(self):
        return _linalg.vectord_get_allocator(self)

    def begin(self):
        return _linalg.vectord_begin(self)

    def end(self):
        return _linalg.vectord_end(self)

    def rbegin(self):
        return _linalg.vectord_rbegin(self)

    def rend(self):
        return _linalg.vectord_rend(self)

    def pop_back(self):
        return _linalg.vectord_pop_back(self)

    def erase(self, *args):
        return _linalg.vectord_erase(self, *args)

    def __init__(self, *args):
        this = _linalg.new_vectord(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _linalg.vectord_push_back(self, x)

    def front(self):
        return _linalg.vectord_front(self)

    def back(self):
        return _linalg.vectord_back(self)

    def assign(self, n, x):
        return _linalg.vectord_assign(self, n, x)

    def resize(self, *args):
        return _linalg.vectord_resize(self, *args)

    def insert(self, *args):
        return _linalg.vectord_insert(self, *args)

    def reserve(self, n):
        return _linalg.vectord_reserve(self, n)

    def capacity(self):
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
        except:
            self.this = this
    __swig_destroy__ = _linalg.delete_charp
    __del__ = lambda self: None

    def assign(self, value):
        return _linalg.charp_assign(self, value)

    def value(self):
        return _linalg.charp_value(self)

    def cast(self):
        return _linalg.charp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _linalg.charp_frompointer
    if _newclass:
        frompointer = staticmethod(_linalg.charp_frompointer)
charp_swigregister = _linalg.charp_swigregister
charp_swigregister(charp)

def charp_frompointer(t):
    return _linalg.charp_frompointer(t)
charp_frompointer = _linalg.charp_frompointer

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
        except:
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

    def uniform(self):
        return _linalg.Tensor_uniform(self)

    def zero(self):
        return _linalg.Tensor_zero(self)

    def get(self, x):
        return _linalg.Tensor_get(self, x)

    def __imul__(self, x):
        return _linalg.Tensor___imul__(self, x)

    def __idiv__(self, x):
        return _linalg.Tensor___idiv__(self, x)

    def __iadd__(self, x):
        return _linalg.Tensor___iadd__(self, x)

    def __isub__(self, x):
        return _linalg.Tensor___isub__(self, x)
    __swig_destroy__ = _linalg.delete_Tensor
    __del__ = lambda self: None
Tensor_swigregister = _linalg.Tensor_swigregister
Tensor_swigregister(Tensor)

# This file is compatible with both classic and new-style classes.

