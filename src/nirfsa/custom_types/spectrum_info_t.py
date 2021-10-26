import ctypes

import nirfsa._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niRFSA_spectrumInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('initial_fequency', nirfsa._visatype.ViReal64),
        ('frequency_increment', nirfsa._visatype.ViReal64),
        ('number_of_spectral_lines', nirfsa._visatype.ViInt32),
        ('reserved1', nirfsa._visatype.ViReal64),
        ('reserved2', nirfsa._visatype.ViReal64),
        ('reserved3', nirfsa._visatype.ViReal64),
        ('reserved4', nirfsa._visatype.ViReal64),
        ('reserved5', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, initial_fequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved1=0.0, reserved2=0.0, reserved3=0.0,
                 reserved4=0.0, reserved5=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.initial_fequency = data.initial_fequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self.reserved3 = data.reserved3
            self.reserved4 = data.reserved4
            self.reserved5 = data.reserved5
        else:
            self.initial_fequency = initial_fequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            self.reserved3 = reserved3
            self.reserved4 = reserved4
            self.reserved5 = reserved5


class SpectrumInfo(object):
    def __init__(self, data=None, initial_fequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved1=0.0, reserved2=0.0, reserved3=0.0,
                 reserved4=0.0, reserved5=0.0):
        if data is not None:
            self.initial_fequency = data.initial_fequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self.reserved3 = data.reserved3
            self.reserved4 = data.reserved4
            self.reserved5 = data.reserved5
        else:
            self.initial_fequency = initial_fequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            self.reserved3 = reserved3
            self.reserved4 = reserved4
            self.reserved5 = reserved5

    def __repr__(self):
        parameter_list = [
            'initial_fequency={}'.format(self.initial_fequency),
            'frequency_increment={}'.format(self.frequency_increment),
            'number_of_spectral_lines={}'.format(self.number_of_spectral_lines),
        ]

        return '{0}({1})'.format(self.__class__.__name__, ', '.join(parameter_list))

    def __str__(self):
        # different format lines
        row_format_g = '{:<20}: {:,.6g}\n'
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'
        string_representation = ''
        string_representation += row_format_g.format('Initial Frequency', self.initial_fequency)
        string_representation += row_format_g.format('Frequency Increment', self.frequency_increment)
        string_representation += row_format_g.format('Number of Spectral Lines', self.number_of_spectral_lines)

        return string_representation

