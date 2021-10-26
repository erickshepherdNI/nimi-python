import ctypes

import nirfsa._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_NIComplexNumber(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('real', nirfsa._visatype.ViReal64),
        ('imaginary', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, real=0.0, imaginary=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.real = data.real
            self.imaginary = data.imaginary
        else:
            self.real = real
            self.imaginary = imaginary

    def __repr__(self):
        return '{0}(data=None, real={1}, imaginary={2})'.format(self.__class__.__name__, self.real, self.imaginary)

    def __str__(self):
        return self.__repr__()


class NIComplexNumber(object):
    def __init__(self, data=None, real=0.0, imaginary=0.0):
        if data is not None:
            self.real = data.real
            self.imaginary = data.imaginary
        else:
            self.real = real
            self.imaginary = imaginary

    def __repr__(self):
        return '{0}(data=None, real={1}, imaginary={2})'.format(self.__class__.__name__, self.real, self.imaginary)

    def __str__(self):
        return self.__repr__()


