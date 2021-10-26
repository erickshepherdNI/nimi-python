# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 21.5.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nAborts an acquisition and returns the device to the Idle state. Call\nthis function if the device times out waiting for a trigger.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niRFSA_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisitionType': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'acquisitionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureIQCarrierFrequency': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'carrierFrequency',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'configure_iq_carrier_frequency',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureIQRate': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'iqRate',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'configure_iq_rate',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureNumberOfSamples': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamplesIsFinite',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'samplesPerRecord',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureRefClock': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'clockSource',
                'type': 'ViString'
            },
            {
                'default_value': 10000000,
                'direction': 'in',
                'name': 'refClockRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureReferenceLevel': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureResolutionBandwidth': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'resolutionBandwidth',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ConfigureSpectrumFrequencyStartStop': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'startFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with an IVI session or with the\ncurrent execution thread. If you specify a valid IVI session for the\n**vi** parameter, this function retrieves and then clears the error\ninformation for the session. If you pass VI_NULL for the **vi**\nparameter, this function retrieves and then clears the error information\nfor the current execution thread.\n\nThe IVI Engine also maintains this error information separately for each\nthread. This feature is useful if you do not have a session handle to\npass to the niFgen_GetError or nirfsa_ClearError functions. This\nsituation occurs when a call to the nirfsa_init or\nnirfsa_InitWithOptions function fails.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the nirfsa_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fail.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error code for the session or execution thread.\n\nA value of VI_SUCCESS (0) indicates that no error occurred. A positive\nvalue indicates a warning. A negative value indicates an error.\n\nYou can call nirfsa_error_message to get a text description of the\nvalue.\n\nIf you are not interested in this value, you can pass VI_NULL.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the **errorDescription** array.\n\nYou can determine the array size needed to store the entire error\ndescription by setting this parameter to 0. The function then ignores\nthe **errorDescription** buffer, which may be set to VI_NULL, and gives\nas its return value the required buffer size. You can then call the\nfunction a second time using the correct buffer size.\n'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error description string for the session or execution thread. If the\nerror code is nonzero, the description string can further describe the\nerror or warning condition.\n\nIf you are not interested in this value, you can pass VI_NULL.\nOtherwise, you must pass a ViChar array of a size specified with the\n**errorDescriptionBufferSize** parameter.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\nThe time returned is 24-hour (military) local time; for example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hour** parameter and 30 for the **minute** parameter.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnirfsa_init or the nirfsa_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetNumberOfSpectralLines': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'name': 'numberOfSpectralLines',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nAll values are returned as separate parameters. Each parameter is\nreturned as an integer, including the year, month, day, hour, minute,\nand second. For example, if the device is calibrated in September 2013,\nthis function returns 9 for the **month** parameter and 2013 for the\n**year** parameter.\n\nThe time returned is 24-hour (military) local time. For example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hours** parameter and 30 for the **minutes** parameter.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnirfsa_init or the nirfsa_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the calibration step.'
                },
                'name': 'selfCalibrationStep',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument driver and optionally sets the initial\n   state of the following session properties: Range Check, Cache,\n   Simulate, Record Value Coercions\n-  Opens a session to the specified device using the interface and\n   address you specify for the **resourceName**\n-  Resets the digitizer to a known state if **resetDevice** is set to\n   VI_TRUE\n-  Queries the instrument ID and verifies that it is valid for this\n   instrument driver if the **IDQuery** is set to VI_TRUE\n-  Returns an instrument handle that you use to identify the instrument\n   in all subsequent instrument driver function calls\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must make sure that the name you use matches the name in\nthe IVI Configuration Store file exactly, without any variations in the\ncase of the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx\ndevice name, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::1 (1 = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            'myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::2 (2 = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            'myLogicalName (myLogicalName = name)'
                        ]
                    ],
                    'table_header': [
                        'Example',
                        'Device Type',
                        'Syntax'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-SCOPE verifies that the\ndevice you initialize is a type that it supports.\n\nWhen you set this parameter to VI_FALSE, the function initializes the\ndevice without performing an ID query.\n\n**Defined Values**\n\n| VI_TRUE—Perform ID query\n| VI_FALSE—Skip ID query\n\n**Default Value**: VI_TRUE\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to reset the device during the initialization process.\n\nDefault Value: VI_TRUE\n\n**Defined Values**\n\nVI_TRUE (1)—Reset device\n\nVI_FALSE (0)—Do not reset device\n',
                    'note': '\nFor the NI 5112, repeatedly resetting the device may cause excessive\nwear on the electromechanical relays. Refer to `NI 5112\nElectromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__\nfor recommended programming practices.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies initialization commands. The following table lists the\n  attributes and the name you use in the **optionString** to identify\n  the attribute.\n\nDefault Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n\nYou can use the option string to simulate a device. The DriverSetup flag\nspecifies the model that is to be simulated and the type of the model.\nOne example to simulate an NI PXI-5102 would be as follows:\n\nOption String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI\n\nRefer to the example niScope EX Simulated Acquisition for more\ninformation on simulation.\n\nYou can also use the option string to attach an accessory such as the\nNI 5900 to your digitizer session to allow the seamless use of the\naccessory:\n\nOption String: DriverSetup = Accessory:Dev1\n\nRefer to the example niScope EX External Amplifier for more information.\n',
                    'table_body': [
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-SCOPE function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a thingie.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadIQSingleRecordComplexF64': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'struct NIComplexNumber[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo'
            }
        ],
        'python_name': 'read_iq_single_record_complex_f64',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ReadPowerSpectrumF64': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nTodo: add documentation\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'powerSpectrumData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo'
            }
        ],
        'python_name': 'read_power_spectrum_f64',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'close': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nWhen you are finished using an instrument driver session, you must call\nthis function to perform the following actions:\n\n-  Closes the instrument I/O session.\n-  Destroys the IVI session and all of its attributes.\n-  Deallocates any memory resources used by the IVI session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nConverts a status code returned by an NI-RFSA function into a\nuser-readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the niFgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fails.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-RFSA functions.\n\n**Default Value**: 0 (VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error message string read from the instrument error message\nqueue.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'TBD'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    }
}
