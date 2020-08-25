scmos_noise_properties = {
        'VSC-00954': {
            '12-bit (low noise)': {
                'ReadNoise' : 1.1,
                'ElectronsPerCount' : 0.28,
                'ADOffset' : 100, # check mean (or median) offset
                'SaturationThreshold' : 2**11-1#(2**16 -1) # check this is really 11 bit
            },
            '12-bit (high well capacity)': {
                'ReadNoise' : 5.96,
                'ElectronsPerCount' : 6.97,
                'ADOffset' : 100,
                'SaturationThreshold' : 2**11-1#(2**16 -1)         
            },
            '16-bit (low noise & high well capacity)': {
                'ReadNoise' : 1.33,
                'ElectronsPerCount' : 0.5,
                'ADOffset' : 100,
                'SaturationThreshold' : (2**16 -1)
            }},
        'CSC-00425': { # this is info for a Sona
            u'12-bit (low noise)': {
                'ReadNoise' : 1.21,
                'ElectronsPerCount' : 0.45,
                'ADOffset' : 100, # check mean (or median) offset
                'SaturationThreshold' : 1776  #(2**16 -1) # check this is really 11 bit
            },
            u'16-bit (high dynamic range)': {
                'ReadNoise' : 1.84,
                'ElectronsPerCount' : 1.08,
                'ADOffset' : 100,
                'SaturationThreshold' : 44185
            }},
        'VSC-02858': {
             '12-bit (low noise)': {
                'ReadNoise' : 1.19,
                'ElectronsPerCount' : 0.3,
                'ADOffset' : 100, # check mean (or median) offset
                'SaturationThreshold' : 2**11-1#(2**16 -1) # check this is really 11 bit
            },
            '12-bit (high well capacity)': {
                'ReadNoise' : 6.18,
                'ElectronsPerCount' : 7.2,
                'ADOffset' : 100,
                'SaturationThreshold' : 2**11-1#(2**16 -1)         
            },
            '16-bit (low noise & high well capacity)': {
                'ReadNoise' : 1.42,
                'ElectronsPerCount' : 0.5,
                'ADOffset' : 100,
                'SaturationThreshold' : (2**16 -1)
            }},
        'VSC-02698': {
             '12-bit (low noise)': {
                'ReadNoise' : 1.16,
                'ElectronsPerCount' : 0.26,
                'ADOffset' : 100, # check mean (or median) offset
                'SaturationThreshold' : 2**11-1#(2**16 -1) # check this is really 11 bit
            },
            '12-bit (high well capacity)': {
                'ReadNoise' : 6.64,
                'ElectronsPerCount' : 7.38,
                'ADOffset' : 100,
                'SaturationThreshold' : 2**11-1#(2**16 -1)         
            },
            '16-bit (low noise & high well capacity)': {
                'ReadNoise' : 1.36,
                'ElectronsPerCount' : 0.49,
                'ADOffset' : 100,
                'SaturationThreshold' : (2**16 -1)
            }}}

emCCDnoiseProperties = {
1823 : {
        'ReadNoise' : 109.8,
        'ElectronsPerCount' : 27.32,
        'NGainStages' : 536,
        'ADOffset' : 971,
        'DefaultEMGain' : 150,
        'SaturationThreshold' : (2**14 -1)
        },
5414 : {
        'ReadNoise' : 61.33,
        'ElectronsPerCount' : 25.24,
        'NGainStages' : 536,
        'ADOffset' : 413,
        'DefaultEMGain' : 90,
        'SaturationThreshold' : (2**14 -1)
        },
7863 : { #Gain setting of 3
        'ReadNoise' : 88.1,
        'ElectronsPerCount' : 4.99,
        'NGainStages' : 536,
        'ADOffset' : 203,
        'DefaultEMGain' : 90,
        'SaturationThreshold' : 5.4e4#(2**16 -1)
        },
7546 : {
        #  preamp: currently using most sensitive setting (default according to docs)
        # if I understand the code correctly the fastest Horizontal Shift Speed will be selected
        # which should be 17 MHz for this camera; therefore using 17 MHz data
        'ReadNoise' : 85.23,
        'ElectronsPerCount' : 4.82,
        'NGainStages' : 536, # relevant?
        'ADOffset' : 150, # from test measurement at EMGain 85 (realgain ~30)
        'DefaultEMGain' : 85, # we start carefully and can bumb this later to be in the vicinity of 30
        'SaturationThreshold' : (2**16 -1) # this cam has 16 bit data
    },
}

preamp_gains = {
    1823 : 0,
    5414 : 0,
    7863 : 2,
}

emCCD_properties = {
    'noiseProperties' : emCCDnoiseProperties,
    'preampGain' : preamp_gains
    }
