# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nirfsa.errors as errors
import threading

from nirfsa._visatype import *  # noqa: F403,H303

import nirfsa.ni_complex_number as ni_complex_number  # noqa: F401

import nirfsa.spectrum_info_t as spectrum_info_t  # noqa: F401

import nirfsa.waveform_info as waveform_info  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niRFSA_Abort_cfunc = None
        self.niRFSA_ConfigureAcquisitionType_cfunc = None
        self.niRFSA_ConfigureIQCarrierFrequency_cfunc = None
        self.niRFSA_ConfigureIQRate_cfunc = None
        self.niRFSA_ConfigureNumberOfSamples_cfunc = None
        self.niRFSA_ConfigureRefClock_cfunc = None
        self.niRFSA_ConfigureReferenceLevel_cfunc = None
        self.niRFSA_ConfigureResolutionBandwidth_cfunc = None
        self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = None
        self.niRFSA_GetError_cfunc = None
        self.niRFSA_GetExtCalLastDateAndTime_cfunc = None
        self.niRFSA_GetNumberOfSpectralLines_cfunc = None
        self.niRFSA_GetSelfCalLastDateAndTime_cfunc = None
        self.niRFSA_InitWithOptions_cfunc = None
        self.niRFSA_Initiate_cfunc = None
        self.niRFSA_ReadIQSingleRecordComplexF64_cfunc = None
        self.niRFSA_ReadPowerSpectrumF64_cfunc = None
        self.niRFSA_close_cfunc = None
        self.niRFSA_error_message_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niRFSA_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Abort_cfunc is None:
                self.niRFSA_Abort_cfunc = self._get_library_function('niRFSA_Abort')
                self.niRFSA_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Abort_cfunc(vi)

    def niRFSA_ConfigureAcquisitionType(self, vi, acquisition_type):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureAcquisitionType_cfunc is None:
                self.niRFSA_ConfigureAcquisitionType_cfunc = self._get_library_function('niRFSA_ConfigureAcquisitionType')
                self.niRFSA_ConfigureAcquisitionType_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSA_ConfigureAcquisitionType_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureAcquisitionType_cfunc(vi, acquisition_type)

    def niRFSA_ConfigureIQCarrierFrequency(self, vi, channel_list, carrier_frequency):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIQCarrierFrequency_cfunc is None:
                self.niRFSA_ConfigureIQCarrierFrequency_cfunc = self._get_library_function('niRFSA_ConfigureIQCarrierFrequency')
                self.niRFSA_ConfigureIQCarrierFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureIQCarrierFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIQCarrierFrequency_cfunc(vi, channel_list, carrier_frequency)

    def niRFSA_ConfigureIQRate(self, vi, channel_list, iq_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIQRate_cfunc is None:
                self.niRFSA_ConfigureIQRate_cfunc = self._get_library_function('niRFSA_ConfigureIQRate')
                self.niRFSA_ConfigureIQRate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureIQRate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIQRate_cfunc(vi, channel_list, iq_rate)

    def niRFSA_ConfigureNumberOfSamples(self, vi, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureNumberOfSamples_cfunc is None:
                self.niRFSA_ConfigureNumberOfSamples_cfunc = self._get_library_function('niRFSA_ConfigureNumberOfSamples')
                self.niRFSA_ConfigureNumberOfSamples_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureNumberOfSamples_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureNumberOfSamples_cfunc(vi, channel_list, number_of_samples_is_finite, samples_per_record)

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureRefClock_cfunc is None:
                self.niRFSA_ConfigureRefClock_cfunc = self._get_library_function('niRFSA_ConfigureRefClock')
                self.niRFSA_ConfigureRefClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureRefClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureRefClock_cfunc(vi, clock_source, ref_clock_rate)

    def niRFSA_ConfigureReferenceLevel(self, vi, channel_list, reference_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureReferenceLevel_cfunc is None:
                self.niRFSA_ConfigureReferenceLevel_cfunc = self._get_library_function('niRFSA_ConfigureReferenceLevel')
                self.niRFSA_ConfigureReferenceLevel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureReferenceLevel_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureReferenceLevel_cfunc(vi, channel_list, reference_level)

    def niRFSA_ConfigureResolutionBandwidth(self, vi, channel_list, resolution_bandwidth):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureResolutionBandwidth_cfunc is None:
                self.niRFSA_ConfigureResolutionBandwidth_cfunc = self._get_library_function('niRFSA_ConfigureResolutionBandwidth')
                self.niRFSA_ConfigureResolutionBandwidth_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureResolutionBandwidth_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureResolutionBandwidth_cfunc(vi, channel_list, resolution_bandwidth)

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc is None:
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = self._get_library_function('niRFSA_ConfigureSpectrumFrequencyStartStop')
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc(vi, channel_list, start_frequency, stop_frequency)

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetError_cfunc is None:
                self.niRFSA_GetError_cfunc = self._get_library_function('niRFSA_GetError')
                self.niRFSA_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetExtCalLastDateAndTime')
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niRFSA_GetNumberOfSpectralLines(self, vi, channel_list, number_of_spectral_lines):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetNumberOfSpectralLines_cfunc is None:
                self.niRFSA_GetNumberOfSpectralLines_cfunc = self._get_library_function('niRFSA_GetNumberOfSpectralLines')
                self.niRFSA_GetNumberOfSpectralLines_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetNumberOfSpectralLines_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetNumberOfSpectralLines_cfunc(vi, channel_list, number_of_spectral_lines)

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSelfCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetSelfCalLastDateAndTime')
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSelfCalLastDateAndTime_cfunc(vi, self_calibration_step, year, month, day, hour, minute)

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitWithOptions_cfunc is None:
                self.niRFSA_InitWithOptions_cfunc = self._get_library_function('niRFSA_InitWithOptions')
                self.niRFSA_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niRFSA_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Initiate_cfunc is None:
                self.niRFSA_Initiate_cfunc = self._get_library_function('niRFSA_Initiate')
                self.niRFSA_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Initiate_cfunc(vi)

    def niRFSA_ReadIQSingleRecordComplexF64(self, vi, channel_list, timeout, data, data_array_size, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadIQSingleRecordComplexF64_cfunc is None:
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc = self._get_library_function('niRFSA_ReadIQSingleRecordComplexF64')
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ni_complex_number.struct_NIComplexNumber), ViInt64, ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadIQSingleRecordComplexF64_cfunc(vi, channel_list, timeout, data, data_array_size, wfm_info)

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadPowerSpectrumF64_cfunc is None:
                self.niRFSA_ReadPowerSpectrumF64_cfunc = self._get_library_function('niRFSA_ReadPowerSpectrumF64')
                self.niRFSA_ReadPowerSpectrumF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(spectrum_info_t.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_ReadPowerSpectrumF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadPowerSpectrumF64_cfunc(vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info)

    def niRFSA_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_close_cfunc is None:
                self.niRFSA_close_cfunc = self._get_library_function('niRFSA_close')
                self.niRFSA_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_close_cfunc(vi)

    def niRFSA_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_error_message_cfunc is None:
                self.niRFSA_error_message_cfunc = self._get_library_function('niRFSA_error_message')
                self.niRFSA_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_error_message_cfunc(vi, error_code, error_message)
