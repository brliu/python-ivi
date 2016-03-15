"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2012-2014 Alex Forencich
Copyright (c) 2016 Faraday Technology Corporation

Author: Bing-Rong Liu <brliu@faraday-tech.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from .tektronixBaseScope import *


ScreenshotImageFormatMapping = {
        'bmp': 'bmp',
        'bmpcolor': 'bmp',
        'png': 'png'}


class tektronixTDS3000(tektronixBaseScope):
    "Tektronix eScope TDS3000 series IVI oscilloscope driver"
    
    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault('_instrument_id', '')
        
        super(tektronixTDS3000, self).__init__(*args, **kwargs)
        
        self._analog_channel_name = list()
        self._analog_channel_count = 4
        self._digital_channel_name = list()
        self._digital_channel_count = 0
        self._channel_count = self._analog_channel_count + self._digital_channel_count
        self._bandwidth = 500e6
        
        self._horizontal_divisions = 10
        self._vertical_divisions = 8

        self._display_screenshot_image_format_mapping = ScreenshotImageFormatMapping

        # wavegen option
        #self._output_mode_list = OutputMode
        #self._operation_mode_list = OperationMode
        #self._output_count = 1
        #self._output_standard_waveform_mapping = StandardWaveformMapping
        
        self._identity_description = "Tektronix eScope TDS3000 series IVI oscilloscope driver"
        self._identity_supported_instrument_models = [
                'TDS3102','TDS3014',
                'TDS3032','TDS3034',
                'TDS3052','TDS3054'
                ]

        #self._init_outputs()
        self._init_channels()
       

class tektronixTDS3052B(tektronixTDS3000):
    "Tektronix eScope TDS3052B IVI oscilloscope driver"
    
    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault('_instrument_id', 'TDS3052B')
        
        super(tektronixTDS3052B, self).__init__(*args, **kwargs)
        
        self._analog_channel_count = 2
        self._digital_channel_count = 0
        self._channel_count = self._analog_channel_count + self._digital_channel_count
        self._bandwidth = 500e6
        
        self._init_channels()
    
