# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 21.5.0d9999
config = {
    'api_version': '21.5.0d9999',
    'c_function_prefix': 'niRFSA_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_NIComplexNumber',
            'file_name': 'ni_complex_number',
            'python_name': 'NIComplexNumber'
        },
        {
            'ctypes_type': 'struct_niRFSA_spectrumInfo',
            'file_name': 'spectrum_info_t',
            'python_name': 'SpectrumInfoT'
        },
        {
            'ctypes_type': 'struct_niRFSA_wfmInfo',
            'file_name': 'waveform_info',
            'python_name': 'WaveformInfo'
        }
    ],
    'driver_name': 'NI-RFSA',
    'enum_whitelist_suffix': [
        '_POINT_FIVE'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsa',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSA.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSA_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nirfsa',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
