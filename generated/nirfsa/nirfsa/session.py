# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import nirfsa._converters as _converters
import nirfsa._library_singleton as _library_singleton
import nirfsa._visatype as _visatype
import nirfsa.enums as enums
import nirfsa.errors as errors

import nirfsa.ni_complex_number as ni_complex_number  # noqa: F401

import nirfsa.spectrum_info_t as spectrum_info_t  # noqa: F401

import nirfsa.waveform_info as waveform_info  # noqa: F401

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(vi=self._session._vi, repeated_capability_list=complete_rep_cap_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-RFSA sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nirfsa', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

    def configure_iq_carrier_frequency(self, carrier_frequency):
        r'''configure_iq_carrier_frequency

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_iq_carrier_frequency`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_iq_carrier_frequency`

        Args:
            carrier_frequency (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        carrier_frequency_ctype = _visatype.ViReal64(carrier_frequency)  # case S150
        error_code = self._library.niRFSA_ConfigureIQCarrierFrequency(vi_ctype, channel_list_ctype, carrier_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_iq_rate(self, iq_rate):
        r'''configure_iq_rate

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_iq_rate`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_iq_rate`

        Args:
            iq_rate (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        iq_rate_ctype = _visatype.ViReal64(iq_rate)  # case S150
        error_code = self._library.niRFSA_ConfigureIQRate(vi_ctype, channel_list_ctype, iq_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_number_of_samples(self, number_of_samples_is_finite, samples_per_record):
        r'''configure_number_of_samples

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_number_of_samples`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_number_of_samples`

        Args:
            number_of_samples_is_finite (bool):

            samples_per_record (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_samples_is_finite_ctype = _visatype.ViBoolean(number_of_samples_is_finite)  # case S150
        samples_per_record_ctype = _visatype.ViInt64(samples_per_record)  # case S150
        error_code = self._library.niRFSA_ConfigureNumberOfSamples(vi_ctype, channel_list_ctype, number_of_samples_is_finite_ctype, samples_per_record_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_reference_level(self, reference_level):
        r'''configure_reference_level

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_reference_level`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_reference_level`

        Args:
            reference_level (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        reference_level_ctype = _visatype.ViReal64(reference_level)  # case S150
        error_code = self._library.niRFSA_ConfigureReferenceLevel(vi_ctype, channel_list_ctype, reference_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_resolution_bandwidth(self, resolution_bandwidth):
        r'''configure_resolution_bandwidth

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_resolution_bandwidth`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_resolution_bandwidth`

        Args:
            resolution_bandwidth (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        resolution_bandwidth_ctype = _visatype.ViReal64(resolution_bandwidth)  # case S150
        error_code = self._library.niRFSA_ConfigureResolutionBandwidth(vi_ctype, channel_list_ctype, resolution_bandwidth_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_spectrum_frequency_start_stop(self, start_frequency, stop_frequency):
        r'''configure_spectrum_frequency_start_stop

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_start_stop`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_spectrum_frequency_start_stop`

        Args:
            start_frequency (float):

            stop_frequency (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        start_frequency_ctype = _visatype.ViReal64(start_frequency)  # case S150
        stop_frequency_ctype = _visatype.ViReal64(stop_frequency)  # case S150
        error_code = self._library.niRFSA_ConfigureSpectrumFrequencyStartStop(vi_ctype, channel_list_ctype, start_frequency_ctype, stop_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_error(self):
        r'''_get_error

        Returns the error information associated with an IVI session or with the
        current execution thread. If you specify a valid IVI session for the
        **vi** parameter, this method retrieves and then clears the error
        information for the session. If you pass VI_NULL for the **vi**
        parameter, this method retrieves and then clears the error information
        for the current execution thread.

        The IVI Engine also maintains this error information separately for each
        thread. This feature is useful if you do not have a session handle to
        pass to the niFgen_GetError or ClearError methods. This
        situation occurs when a call to the init or
        __init__ method fails.

        Returns:
            error_code (int): The error code for the session or execution thread.

                A value of VI_SUCCESS (0) indicates that no error occurred. A positive
                value indicates a warning. A negative value indicates an error.

                You can call _error_message to get a text description of the
                value.

                If you are not interested in this value, you can pass VI_NULL.

            error_description (str): The error description string for the session or execution thread. If the
                error code is nonzero, the description string can further describe the
                error or warning condition.

                If you are not interested in this value, you can pass VI_NULL.
                Otherwise, you must pass a ViChar array of a size specified with the
                **errorDescriptionBufferSize** parameter.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_number_of_spectral_lines(self):
        r'''get_number_of_spectral_lines

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_number_of_spectral_lines`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_number_of_spectral_lines`

        Returns:
            number_of_spectral_lines (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_spectral_lines_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetNumberOfSpectralLines(vi_ctype, channel_list_ctype, None if number_of_spectral_lines_ctype is None else (ctypes.pointer(number_of_spectral_lines_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_spectral_lines_ctype.value)

    def read_iq_single_record_complex_f64(self, timeout, data_array_size):
        r'''read_iq_single_record_complex_f64

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_iq_single_record_complex_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.read_iq_single_record_complex_f64`

        Args:
            timeout (float):

            data_array_size (int):


        Returns:
            data (list of NIComplexNumber):

            wfm_info (WaveformInfo):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_size = data_array_size  # case B600
        data_ctype = get_ctypes_pointer_for_buffer(library_type=ni_complex_number.struct_NIComplexNumber, size=data_size)  # case B600
        data_array_size_ctype = _visatype.ViInt64(data_array_size)  # case S210
        wfm_info_ctype = waveform_info.struct_niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_ReadIQSingleRecordComplexF64(vi_ctype, channel_list_ctype, timeout_ctype, data_ctype, data_array_size_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [ni_complex_number.NIComplexNumber(data_ctype[i]) for i in range(data_array_size_ctype.value)], waveform_info.WaveformInfo(wfm_info_ctype)

    def read_power_spectrum_f64(self, timeout, data_array_size):
        r'''read_power_spectrum_f64

        Todo: add documentation

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.read_power_spectrum_f64`

        Args:
            timeout (float):

            data_array_size (int):


        Returns:
            power_spectrum_data (list of float):

            spectrum_info (SpectrumInfoT):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        power_spectrum_data_size = data_array_size  # case B600
        power_spectrum_data_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=power_spectrum_data_size)  # case B600
        data_array_size_ctype = _visatype.ViInt32(data_array_size)  # case S210
        spectrum_info_ctype = spectrum_info_t.struct_niRFSA_spectrumInfo()  # case S220
        error_code = self._library.niRFSA_ReadPowerSpectrumF64(vi_ctype, channel_list_ctype, timeout_ctype, power_spectrum_data_ctype, data_array_size_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(power_spectrum_data_ctype[i]) for i in range(data_array_size_ctype.value)], spectrum_info_t.SpectrumInfoT(spectrum_info_ctype)

    def _error_message(self, error_code):
        r'''_error_message

        Converts a status code returned by an NI-RFSA method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-RFSA methods.

                **Default Value**: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}):
        r'''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           True
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to True
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver method calls

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must make sure that the name you use matches the name in
                the IVI Configuration Store file exactly, without any variations in the
                case of the characters.

                | Specifies the resource name of the device to initialize

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
                device name, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +---------+--------------------------------------+--------------------------------------------------+
                | Example | Device Type                          | Syntax                                           |
                +=========+======================================+==================================================+
                | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
                +---------+--------------------------------------+--------------------------------------------------+
                | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
                +---------+--------------------------------------+--------------------------------------------------+
                | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
                +---------+--------------------------------------+--------------------------------------------------+
                | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
                +---------+--------------------------------------+--------------------------------------------------+
                | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
                +---------+--------------------------------------+--------------------------------------------------+

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+


        Returns:
            session (nirfsa.Session): A session object representing the device.

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, id_query, reset_device, options)

        self.tclk = nitclk.SessionReference(self._vi)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        Initiates a thingie.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts an acquisition and returns the device to the Idle state. Call
        this method if the device times out waiting for a trigger.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_acquisition_type(self, acquisition_type):
        r'''configure_acquisition_type

        Todo: add documentation

        Args:
            acquisition_type (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        acquisition_type_ctype = _visatype.ViInt32(acquisition_type)  # case S150
        error_code = self._library.niRFSA_ConfigureAcquisitionType(vi_ctype, acquisition_type_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_clock(self, clock_source, ref_clock_rate=10000000):
        r'''configure_ref_clock

        Todo: add documentation

        Args:
            clock_source (str):

            ref_clock_rate (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        clock_source_ctype = ctypes.create_string_buffer(clock_source.encode(self._encoding))  # case C020
        ref_clock_rate_ctype = _visatype.ViReal64(ref_clock_rate)  # case S150
        error_code = self._library.niRFSA_ConfigureRefClock(vi_ctype, clock_source_ctype, ref_clock_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.
        The time returned is 24-hour (military) local time; for example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hour** parameter and 30 for the **minute** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        year, month, day, hour, minute = self.get_ext_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self, self_calibration_step):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        All values are returned as separate parameters. Each parameter is
        returned as an integer, including the year, month, day, hour, minute,
        and second. For example, if the device is calibrated in September 2013,
        this method returns 9 for the **month** parameter and 2013 for the
        **year** parameter.

        The time returned is 24-hour (military) local time. For example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hours** parameter and 30 for the **minutes** parameter.

        Args:
            self_calibration_step (int): Specifies the calibration step.


        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        year, month, day, hour, minute = self.get_self_cal_last_date_and_time(self_calibration_step)
        return hightime.datetime(year, month, day, hour, minute)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           True
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to True
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver method calls

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must make sure that the name you use matches the name in
                the IVI Configuration Store file exactly, without any variations in the
                case of the characters.

                | Specifies the resource name of the device to initialize

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
                device name, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +---------+--------------------------------------+--------------------------------------------------+
                | Example | Device Type                          | Syntax                                           |
                +=========+======================================+==================================================+
                | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
                +---------+--------------------------------------+--------------------------------------------------+
                | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
                +---------+--------------------------------------+--------------------------------------------------+
                | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
                +---------+--------------------------------------+--------------------------------------------------+
                | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
                +---------+--------------------------------------+--------------------------------------------------+
                | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
                +---------+--------------------------------------+--------------------------------------------------+

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            option_string (dict): | Specifies initialization commands. The following table lists the
                  properties and the name you use in the **optionString** to identify
                  the property.

                Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                You can use the option string to simulate a device. The DriverSetup flag
                specifies the model that is to be simulated and the type of the model.
                One example to simulate an NI PXI-5102 would be as follows:

                Option String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI

                Refer to the example niScope EX Simulated Acquisition for more
                information on simulation.

                You can also use the option string to attach an accessory such as the
                NI 5900 to your digitizer session to allow the seamless use of the
                accessory:

                Option String: DriverSetup = Accessory:Dev1

                Refer to the example niScope EX External Amplifier for more information.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-SCOPE method calls.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates a thingie.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def self_test(self):
        '''self_test

        TBD
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None



