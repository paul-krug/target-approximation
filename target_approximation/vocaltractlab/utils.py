

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