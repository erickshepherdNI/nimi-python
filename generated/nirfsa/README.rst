Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |Docs| |MITLicense| |CoverageStatus|                                                                                 |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         Python bindings for NI Modular Instrument drivers. See `GitHub <https://github.com/ni/nimi-python/>`_ for the latest source.
Author       National Instruments
===========  ============================================================================================================================

.. |BuildStatus| image:: https://img.shields.io/travis/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |Docs| image:: https://readthedocs.org/projects/nimi-python/badge/?version=latest
    :alt: Documentation Status - master branch
    :target: https://nimi-python.readthedocs.io/en/latest/?badge=latest

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://coveralls.io/repos/github/ni/nimi-python/badge.svg?branch=master&dummy=no_cache_please_1
    :alt: Test Coverage - master branch
    :target: https://coveralls.io/github/ni/nimi-python?branch=master

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls


.. _about-section:

About
=====

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. The
following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-Digital Pattern Driver (Python module: nidigital)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-ModInst (Python module: nimodinst)
* NI-SCOPE (Python module: niscope)
* NI Switch Executive (Python module: nise)
* NI-SWITCH (Python module: niswitch)
* NI-TClk (Python module: nitclk)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is
called through its public C API using the `ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions. At
this time this includes Python 3.6 and above using CPython.


NI-RFSA Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-RFSA (nirfsa)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 21.5.0                |
+-------------------------------+-----------------------+
| PyPI Version                  | |nirfsaLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nirfsaPythonVersion| |
+-------------------------------+-----------------------+
| Open Issues                   | |nirfsaOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nirfsaOpenPRs|       |
+-------------------------------+-----------------------+


.. |nirfsaLatestVersion| image:: http://img.shields.io/pypi/v/nirfsa.svg
    :alt: Latest NI-RFSA Version
    :target: http://pypi.python.org/pypi/nirfsa


.. |nirfsaPythonVersion| image:: http://img.shields.io/pypi/pyversions/nirfsa.svg
    :alt: NI-RFSA supported Python versions
    :target: http://pypi.python.org/pypi/nirfsa


.. |nirfsaOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nirfsa.svg
    :alt: Open Issues + Pull Requests for NI-RFSA
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anirfsa


.. |nirfsaOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nirfsa.svg
    :alt: Pull Requests for NI-RFSA
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anirfsa



.. _nirfsa_installation-section:

Installation
------------

As a prerequisite to using the nirfsa module, you must install the NI-RFSA runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-RFSA**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nirfsa

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install nirfsa


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

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

.. _support-section:

Support / Feedback
==================

The packages included in **nimi-python** package are supported by NI. For support, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to NI Modular Instruments Python bindings (nimi-python), please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.

For hardware support or any other questions not specific to this GitHub project, please visit `NI Community Forums <https://forums.ni.com/>`_.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nimi-python.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


