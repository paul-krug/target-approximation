import numpy as np

supraglottal_tiers = dict(
    vtl =[
        'HX','HY','JX','JA','LP','LD','VS','VO',
        'TCX','TCY','TTX','TTY','TBX','TBY','TRX','TRY',
        'TS1','TS2','TS3',
        ],
    tt2 = [
        'HX','HY','JX','JA','LP','LD','VS','VO',
        'TCX','TCY','TTX','TTY','TBX','TBY',#'TRX',#'TRY',
        'TS1','TS2','TS3',
        ],
    )

glottal_tiers = dict(
    vtl = [
        'F0','PR','XB','XT','CA','PL','RA','DP','PS','FL','AS',
        ],
    tt2 = [
        'F0','PR','XB',
        ],
    )

tier_sets = dict(
    vtl = dict(
        sg_tiers = supraglottal_tiers['vtl'],
        g_tiers = glottal_tiers['vtl'],
        ),
    tt2 = dict(
        sg_tiers = supraglottal_tiers['tt2'],
        g_tiers = glottal_tiers['tt2'],
        ),
    tt3 = dict(
        sg_tiers = supraglottal_tiers['vtl'],
        g_tiers = glottal_tiers['tt2'],
        ),
    )

#ms_file_extensions = [
#    '.yaml',
#    '.yaml.gz',
#    '.ms',
#    ]

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

def get_tiers_from_set( x, group ):
    if x not in tier_sets.keys():
        raise ValueError( f'Unknown set {x}.' )
    if group in [ 'sg', 'supraglottal', 'tract' ]:
        tiers =  tier_sets[ x ][ 'sg_tiers' ]
    elif group in [ 'g', 'glottal', 'glottis' ]:
        tiers = tier_sets[ x ][ 'g_tiers' ]
    elif group in [ 'm', 'motor' ]:
        tiers = tier_sets[ x ][ 'sg_tiers' ] + tier_sets[ x ][ 'g_tiers' ]
    else:
        raise ValueError( f'Unknown group {group}.' )
    return tiers