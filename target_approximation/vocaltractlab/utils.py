import numpy as np

supraglottal_tiers = dict(
    default =[
        'HX',
        'HY',
        'JX',
        'JA',
        'LP',
        'LD',
        'VS',
        'VO',
        'TCX',
        'TCY',
        'TTX',
        'TTY',
        'TBX',
        'TBY',
        'TRX',
        'TRY',
        'TS1',
        'TS2',
        'TS3',
        ]
    )

glottal_tiers = dict(
    default = [
        'F0',
        'PR',
        'XB',
        'XT',
        'CA',
        'PL',
        'RA',
        'DP',
        'PS',
        'FL',
        'AS',
        ]
    )

ms_file_extensions = [
    '.yaml',
    '.yaml.gz',
    '.ms',
    ]

def _glottis_params_from_vtl_tractseq( index ):
    if (index > 7) and (index % 2 == 0):
        return False
    else:
        return True

def _tract_params_from_vtl_tractseq( index ):
    if (index > 7) and ((index-1) % 2 == 0):
        return False
    else:
        return True
    
def hz_to_st(
        frequency_hz,
        reference = 1.0,
    ):
    return 12.0*np.log( frequency_hz / reference ) / np.log(2.0)

def st_to_hz(
        frequency_st,
        reference = 1.0,
    ):
    return reference*pow( 2, frequency_st / 12.0 )