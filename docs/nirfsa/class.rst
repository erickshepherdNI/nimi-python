.. py:module:: nirfsa

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={})

    

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

    



    :param resource_name:
        

        .. caution:: Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
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


    :type resource_name: str

    :param id_query:
        

        Specify whether to perform an ID query.

        When you set this parameter to True, NI-SCOPE verifies that the
        device you initialize is a type that it supports.

        When you set this parameter to False, the method initializes the
        device without performing an ID query.

        **Defined Values**

        | True—Perform ID query
        | False—Skip ID query

        **Default Value**: True

        


    :type id_query: bool

    :param reset_device:
        

        Specify whether to reset the device during the initialization process.

        Default Value: True

        **Defined Values**

        True (1)—Reset device

        False (0)—Do not reset device

        

        .. note:: For the NI 5112, repeatedly resetting the device may cause excessive
            wear on the electromechanical relays. Refer to `NI 5112
            Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
            for recommended programming practices.


    :type reset_device: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
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


    :type options: dict


Methods
=======

_close
------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: _close()

            When you are finished using an instrument driver session, you must call
            this method to perform the following actions:

            -  Closes the instrument I/O session.
            -  Destroys the IVI session and all of its properties.
            -  Deallocates any memory resources used by the IVI session.

            



abort
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: abort()

            Aborts an acquisition and returns the device to the Idle state. Call
            this method if the device times out waiting for a trigger.

            



close
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close()

            When you are finished using an instrument driver session, you must call
            this method to perform the following actions:

            -  Closes the instrument I/O session.
            -  Destroys the IVI session and all of its properties.
            -  Deallocates any memory resources used by the IVI session.

            

            .. note:: This method is not needed when using the session context manager



configure_acquisition_type
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_acquisition_type(acquisition_type)

            Todo: add documentation

            



            :param acquisition_type:


                


            :type acquisition_type: int

configure_iq_carrier_frequency
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_carrier_frequency(carrier_frequency)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_iq_carrier_frequency`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_iq_carrier_frequency`


            :param carrier_frequency:


                


            :type carrier_frequency: float

configure_iq_rate
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_rate(iq_rate)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_iq_rate`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_iq_rate`


            :param iq_rate:


                


            :type iq_rate: float

configure_number_of_samples
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_number_of_samples(number_of_samples_is_finite, samples_per_record)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_number_of_samples`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_number_of_samples`


            :param number_of_samples_is_finite:


                


            :type number_of_samples_is_finite: bool
            :param samples_per_record:


                


            :type samples_per_record: int

configure_ref_clock
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_ref_clock(clock_source, ref_clock_rate=10000000)

            Todo: add documentation

            



            :param clock_source:


                


            :type clock_source: str
            :param ref_clock_rate:


                


            :type ref_clock_rate: float

configure_reference_level
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_reference_level(reference_level)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_reference_level`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_reference_level`


            :param reference_level:


                


            :type reference_level: float

configure_resolution_bandwidth
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_resolution_bandwidth(resolution_bandwidth)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_resolution_bandwidth`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_resolution_bandwidth`


            :param resolution_bandwidth:


                


            :type resolution_bandwidth: float

configure_spectrum_frequency_start_stop
---------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_spectrum_frequency_start_stop(start_frequency, stop_frequency)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_start_stop`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_spectrum_frequency_start_stop`


            :param start_frequency:


                


            :type start_frequency: float
            :param stop_frequency:


                


            :type stop_frequency: float

get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful external calibration.
            The time returned is 24-hour (military) local time; for example, if the
            device was calibrated at 2:30 PM, this method returns 14 for the
            **hour** parameter and 30 for the **minute** parameter.

            



            :rtype: tuple (year, month, day, hour, minute)

                WHERE

                year (int): 


                    Specifies the year of the last successful calibration.

                    


                month (int): 


                    Specifies the month of the last successful calibration.

                    


                day (int): 


                    Specifies the day of the last successful calibration.

                    


                hour (int): 


                    Specifies the hour of the last successful calibration.

                    


                minute (int): 


                    Specifies the minute of the last successful calibration.

                    



get_number_of_spectral_lines
----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_number_of_spectral_lines()

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_number_of_spectral_lines`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_number_of_spectral_lines`


            :rtype: int
            :return:


                    



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_self_cal_last_date_and_time(self_calibration_step)

            Returns the date and time of the last successful self-calibration.

            All values are returned as separate parameters. Each parameter is
            returned as an integer, including the year, month, day, hour, minute,
            and second. For example, if the device is calibrated in September 2013,
            this method returns 9 for the **month** parameter and 2013 for the
            **year** parameter.

            The time returned is 24-hour (military) local time. For example, if the
            device was calibrated at 2:30 PM, this method returns 14 for the
            **hours** parameter and 30 for the **minutes** parameter.

            



            :param self_calibration_step:


                Specifies the calibration step.

                


            :type self_calibration_step: int

            :rtype: tuple (year, month, day, hour, minute)

                WHERE

                year (int): 


                    Specifies the year of the last successful calibration.

                    


                month (int): 


                    Specifies the month of the last successful calibration.

                    


                day (int): 


                    Specifies the day of the last successful calibration.

                    


                hour (int): 


                    Specifies the hour of the last successful calibration.

                    


                minute (int): 


                    Specifies the minute of the last successful calibration.

                    



initiate
--------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initiate()

            Initiates a thingie.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



read_iq_single_record_complex_f64
---------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_iq_single_record_complex_f64(timeout, data_array_size)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_iq_single_record_complex_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_iq_single_record_complex_f64`


            :param timeout:


                


            :type timeout: float
            :param data_array_size:


                


            :type data_array_size: int

            :rtype: tuple (data, wfm_info)

                WHERE

                data (list of NIComplexNumber): 


                    


                wfm_info (WaveformInfo): 


                    



read_power_spectrum_f64
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_power_spectrum_f64(timeout, data_array_size)

            Todo: add documentation

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_power_spectrum_f64`


            :param timeout:


                


            :type timeout: float
            :param data_array_size:


                


            :type data_array_size: int

            :rtype: tuple (power_spectrum_data, spectrum_info)

                WHERE

                power_spectrum_data (list of float): 


                    


                spectrum_info (SpectrumInfoT): 


                    



self_test
---------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_test()

            TBD

            





NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:attr:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session


