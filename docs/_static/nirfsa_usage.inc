Usage
------

The following is a basic example of using the **nirfsa** module to open a session to a VST and acquire IQ and Spectrum data.

.. code-block:: python

    import nirfsa.session
    from matplotlib import pyplot as plt

    def plotIQ():
        with nirfsa.session.Session("PXI1Slot17", True) as session:
            session.configure_ref_clock("OnboardClock")
            session.configure_acquisition_type(100)  # 100 = IQ
            session.configure_reference_level(0)
            session.configure_iq_carrier_frequency(1000000000)
            session.configure_iq_rate(1000000)
            session.configure_number_of_samples(True, 1000)
            data, wfmInfo = session.read_iq_single_record_complex_f64(10.0, 1000)
            real = []
            imaginary = []
            for x in range(len(data)):
                real.append(data[x].real)
                imaginary.append(data[x].imaginary)
            plt.plot(real, label='I Data')
            plt.plot(imaginary, label='Q Data')
            plt.title('IQ Data')
            plt.legend(loc='best')
            plt.show()

    def plotSpectrum():
        with nirfsa.session.Session("PXI1Slot17", True) as session:
            session.configure_ref_clock("OnboardClock")
            session.configure_acquisition_type(101)  # 101 = Spectrum
            session.configure_reference_level(0)
            session.configure_spectrum_frequency_start_stop(990000000, 1010000000)
            session.configure_resolution_bandwidth(10000)
            numberOfSpectralLines = session.get_number_of_spectral_lines()
            data, spectrumInfo = session.read_power_spectrum_f64(10.0, numberOfSpectralLines)
            plt.plot(data, label='Spectrum from 990MHz to 1.01GHz')
            plt.title('Spectrum Data')
            plt.legend(loc='best')
            plt.show()

