# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['ConfigureAcquisitionType'] = {}
        self._defaults['ConfigureAcquisitionType']['return'] = 0
        self._defaults['ConfigureIQCarrierFrequency'] = {}
        self._defaults['ConfigureIQCarrierFrequency']['return'] = 0
        self._defaults['ConfigureIQRate'] = {}
        self._defaults['ConfigureIQRate']['return'] = 0
        self._defaults['ConfigureNumberOfSamples'] = {}
        self._defaults['ConfigureNumberOfSamples']['return'] = 0
        self._defaults['ConfigureRefClock'] = {}
        self._defaults['ConfigureRefClock']['return'] = 0
        self._defaults['ConfigureReferenceLevel'] = {}
        self._defaults['ConfigureReferenceLevel']['return'] = 0
        self._defaults['ConfigureResolutionBandwidth'] = {}
        self._defaults['ConfigureResolutionBandwidth']['return'] = 0
        self._defaults['ConfigureSpectrumFrequencyStartStop'] = {}
        self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] = 0
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['year'] = None
        self._defaults['GetExtCalLastDateAndTime']['month'] = None
        self._defaults['GetExtCalLastDateAndTime']['day'] = None
        self._defaults['GetExtCalLastDateAndTime']['hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['minute'] = None
        self._defaults['GetNumberOfSpectralLines'] = {}
        self._defaults['GetNumberOfSpectralLines']['return'] = 0
        self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['minute'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['ReadIQSingleRecordComplexF64'] = {}
        self._defaults['ReadIQSingleRecordComplexF64']['return'] = 0
        self._defaults['ReadIQSingleRecordComplexF64']['data'] = None
        self._defaults['ReadIQSingleRecordComplexF64']['wfmInfo'] = None
        self._defaults['ReadPowerSpectrumF64'] = {}
        self._defaults['ReadPowerSpectrumF64']['return'] = 0
        self._defaults['ReadPowerSpectrumF64']['powerSpectrumData'] = None
        self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niRFSA_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niRFSA_ConfigureAcquisitionType(self, vi, acquisition_type):  # noqa: N802
        if self._defaults['ConfigureAcquisitionType']['return'] != 0:
            return self._defaults['ConfigureAcquisitionType']['return']
        return self._defaults['ConfigureAcquisitionType']['return']

    def niRFSA_ConfigureIQCarrierFrequency(self, vi, channel_list, carrier_frequency):  # noqa: N802
        if self._defaults['ConfigureIQCarrierFrequency']['return'] != 0:
            return self._defaults['ConfigureIQCarrierFrequency']['return']
        return self._defaults['ConfigureIQCarrierFrequency']['return']

    def niRFSA_ConfigureIQRate(self, vi, channel_list, iq_rate):  # noqa: N802
        if self._defaults['ConfigureIQRate']['return'] != 0:
            return self._defaults['ConfigureIQRate']['return']
        return self._defaults['ConfigureIQRate']['return']

    def niRFSA_ConfigureNumberOfSamples(self, vi, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        if self._defaults['ConfigureNumberOfSamples']['return'] != 0:
            return self._defaults['ConfigureNumberOfSamples']['return']
        return self._defaults['ConfigureNumberOfSamples']['return']

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        if self._defaults['ConfigureRefClock']['return'] != 0:
            return self._defaults['ConfigureRefClock']['return']
        return self._defaults['ConfigureRefClock']['return']

    def niRFSA_ConfigureReferenceLevel(self, vi, channel_list, reference_level):  # noqa: N802
        if self._defaults['ConfigureReferenceLevel']['return'] != 0:
            return self._defaults['ConfigureReferenceLevel']['return']
        return self._defaults['ConfigureReferenceLevel']['return']

    def niRFSA_ConfigureResolutionBandwidth(self, vi, channel_list, resolution_bandwidth):  # noqa: N802
        if self._defaults['ConfigureResolutionBandwidth']['return'] != 0:
            return self._defaults['ConfigureResolutionBandwidth']['return']
        return self._defaults['ConfigureResolutionBandwidth']['return']

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        if self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] != 0:
            return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']
        return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niRFSA_GetNumberOfSpectralLines(self, vi, channel_list, number_of_spectral_lines):  # noqa: N802
        if self._defaults['GetNumberOfSpectralLines']['return'] != 0:
            return self._defaults['GetNumberOfSpectralLines']['return']
        # number_of_spectral_lines
        if self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines'] is None:
            raise MockFunctionCallError("niRFSA_GetNumberOfSpectralLines", param='numberOfSpectralLines')
        if number_of_spectral_lines is not None:
            number_of_spectral_lines.contents.value = self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines']
        return self._defaults['GetNumberOfSpectralLines']['return']

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niRFSA_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niRFSA_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niRFSA_ReadIQSingleRecordComplexF64(self, vi, channel_list, timeout, data, data_array_size, wfm_info):  # noqa: N802
        if self._defaults['ReadIQSingleRecordComplexF64']['return'] != 0:
            return self._defaults['ReadIQSingleRecordComplexF64']['return']
        # data
        if self._defaults['ReadIQSingleRecordComplexF64']['data'] is None:
            raise MockFunctionCallError("niRFSA_ReadIQSingleRecordComplexF64", param='data')
        test_value = self._defaults['ReadIQSingleRecordComplexF64']['data']
        try:
            data_ref = data.contents
        except AttributeError:
            data_ref = data
        assert len(data_ref) >= len(test_value)
        for i in range(len(test_value)):
            data_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['ReadIQSingleRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadIQSingleRecordComplexF64", param='wfmInfo')
        for field in self._defaults['ReadIQSingleRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(cs.contents, field_name, getattr(self._defaults['ReadIQSingleRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['ReadIQSingleRecordComplexF64']['return']

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        if self._defaults['ReadPowerSpectrumF64']['return'] != 0:
            return self._defaults['ReadPowerSpectrumF64']['return']
        # power_spectrum_data
        if self._defaults['ReadPowerSpectrumF64']['powerSpectrumData'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF64", param='powerSpectrumData')
        test_value = self._defaults['ReadPowerSpectrumF64']['powerSpectrumData']
        try:
            power_spectrum_data_ref = power_spectrum_data.contents
        except AttributeError:
            power_spectrum_data_ref = power_spectrum_data
        assert len(power_spectrum_data_ref) >= len(test_value)
        for i in range(len(test_value)):
            power_spectrum_data_ref[i] = test_value[i]
        # spectrum_info
        if self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF64", param='spectrumInfo')
        for field in self._defaults['ReadPowerSpectrumF64']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(cs.contents, field_name, getattr(self._defaults['ReadPowerSpectrumF64']['spectrum_info'], field_name))
        return self._defaults['ReadPowerSpectrumF64']['return']

    def niRFSA_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niRFSA_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niRFSA_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niRFSA_Abort.side_effect = MockFunctionCallError("niRFSA_Abort")
        mock_library.niRFSA_Abort.return_value = 0
        mock_library.niRFSA_ConfigureAcquisitionType.side_effect = MockFunctionCallError("niRFSA_ConfigureAcquisitionType")
        mock_library.niRFSA_ConfigureAcquisitionType.return_value = 0
        mock_library.niRFSA_ConfigureIQCarrierFrequency.side_effect = MockFunctionCallError("niRFSA_ConfigureIQCarrierFrequency")
        mock_library.niRFSA_ConfigureIQCarrierFrequency.return_value = 0
        mock_library.niRFSA_ConfigureIQRate.side_effect = MockFunctionCallError("niRFSA_ConfigureIQRate")
        mock_library.niRFSA_ConfigureIQRate.return_value = 0
        mock_library.niRFSA_ConfigureNumberOfSamples.side_effect = MockFunctionCallError("niRFSA_ConfigureNumberOfSamples")
        mock_library.niRFSA_ConfigureNumberOfSamples.return_value = 0
        mock_library.niRFSA_ConfigureRefClock.side_effect = MockFunctionCallError("niRFSA_ConfigureRefClock")
        mock_library.niRFSA_ConfigureRefClock.return_value = 0
        mock_library.niRFSA_ConfigureReferenceLevel.side_effect = MockFunctionCallError("niRFSA_ConfigureReferenceLevel")
        mock_library.niRFSA_ConfigureReferenceLevel.return_value = 0
        mock_library.niRFSA_ConfigureResolutionBandwidth.side_effect = MockFunctionCallError("niRFSA_ConfigureResolutionBandwidth")
        mock_library.niRFSA_ConfigureResolutionBandwidth.return_value = 0
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.side_effect = MockFunctionCallError("niRFSA_ConfigureSpectrumFrequencyStartStop")
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.return_value = 0
        mock_library.niRFSA_GetError.side_effect = MockFunctionCallError("niRFSA_GetError")
        mock_library.niRFSA_GetError.return_value = 0
        mock_library.niRFSA_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime")
        mock_library.niRFSA_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_GetNumberOfSpectralLines.side_effect = MockFunctionCallError("niRFSA_GetNumberOfSpectralLines")
        mock_library.niRFSA_GetNumberOfSpectralLines.return_value = 0
        mock_library.niRFSA_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime")
        mock_library.niRFSA_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_InitWithOptions.side_effect = MockFunctionCallError("niRFSA_InitWithOptions")
        mock_library.niRFSA_InitWithOptions.return_value = 0
        mock_library.niRFSA_Initiate.side_effect = MockFunctionCallError("niRFSA_Initiate")
        mock_library.niRFSA_Initiate.return_value = 0
        mock_library.niRFSA_ReadIQSingleRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_ReadIQSingleRecordComplexF64")
        mock_library.niRFSA_ReadIQSingleRecordComplexF64.return_value = 0
        mock_library.niRFSA_ReadPowerSpectrumF64.side_effect = MockFunctionCallError("niRFSA_ReadPowerSpectrumF64")
        mock_library.niRFSA_ReadPowerSpectrumF64.return_value = 0
        mock_library.niRFSA_close.side_effect = MockFunctionCallError("niRFSA_close")
        mock_library.niRFSA_close.return_value = 0
        mock_library.niRFSA_error_message.side_effect = MockFunctionCallError("niRFSA_error_message")
        mock_library.niRFSA_error_message.return_value = 0
