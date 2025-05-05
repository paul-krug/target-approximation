


import numpy as np
import pandas as pd

from typing import List, Optional, Dict, Any, Union, Tuple, Iterable

#from target_approximation.vocaltractlab.utils import supraglottal_tiers as vtl_sg_tiers
#from target_approximation.vocaltractlab.utils import glottal_tiers as vtl_g_tiers
from target_approximation.vocaltractlab.utils import tier_sets
from target_approximation.vocaltractlab.utils import get_tiers_from_set
#from target_approximation.vocaltractlab.utils import ms_file_extensions
from target_approximation.vocaltractlab.utils import _tract_params_from_vtl_tractseq
from target_approximation.vocaltractlab.utils import _glottis_params_from_vtl_tractseq
from target_approximation.vocaltractlab.utils import st_to_hz, hz_to_st

from target_approximation.core import TargetSequence
from target_approximation.core import TargetSeries
#from target_approximation.tensortract import MotorSequence as TT_MSQ
#from target_approximation.tensortract import MotorSeries as TT_MSRS



class SupraGlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sequence_type: str,
            ):
        tiers = get_tiers_from_set( sequence_type, 'sg' )
        super(SupraGlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        self.sequence_type = sequence_type
        return
    
    def __add__( self, other ):
        if set( self.tiers() ) != set( other.tiers() ):
            raise ValueError(
                f"""
                The tiers of the two target sequences do not match.
                """
                )
        if self.sequence_type != other.sequence_type:
            raise ValueError(
                f"""
                The sequence types of the two target sequences do not match.
                """
                )
        new_tgs = [
            tgs + other.targets[ tier ]
            for tier, tgs in self.targets.items()
        ]
        return SupraGlottalSequence( new_tgs, sequence_type=self.sequence_type )
    
    def _get_data_dict( self ):
        data = super()._get_data_dict()
        data[ 'sequence_type' ] = self.sequence_type
        return data
    
class GlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sequence_type: str,
            ):
        tiers = get_tiers_from_set( sequence_type, 'g' )
        super(GlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        self.sequence_type = sequence_type
        return
    
    def __add__( self, other ):
        if set( self.tiers() ) != set( other.tiers() ):
            raise ValueError(
                f"""
                The tiers of the two target sequences do not match.
                """
                )
        if self.sequence_type != other.sequence_type:
            raise ValueError(
                f"""
                The sequence types of the two target sequences do not match.
                """
                )
        new_tgs = [
            tgs + other.targets[ tier ]
            for tier, tgs in self.targets.items()
        ]
        return GlottalSequence( new_tgs, sequence_type=self.sequence_type )
    
    def _get_data_dict( self ):
        data = super()._get_data_dict()
        data[ 'sequence_type' ] = self.sequence_type
        return data
    
class MotorSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sequence_type: str,
            ):
        tiers = get_tiers_from_set( sequence_type, 'm' )
        super(MotorSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        self.sequence_type = sequence_type
        return
    
    def __add__( self, other ):
        if set( self.tiers() ) != set( other.tiers() ):
            raise ValueError(
                f"""
                The tiers of the two target sequences do not match.
                """
                )
        if self.sequence_type != other.sequence_type:
            raise ValueError(
                f"""
                The sequence types of the two target sequences do not match.
                """
                )
        new_tgs = [
            tgs + other.targets[ tier ]
            for tier, tgs in self.targets.items()
        ]
        return MotorSequence( new_tgs, sequence_type=self.sequence_type )
    
    def _get_data_dict( self ):
        data = super()._get_data_dict()
        data[ 'sequence_type' ] = self.sequence_type
        return data
    
    def to_series(
            self,
            sr: Optional[ float ] = None,
            ):
        x = MotorSeries.from_sequence(
            self,
            sr,
            series_type=self.sequence_type,
            )
        return x

class SupraGlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            series_type: str,
            sr: float = None,
            ):
        tiers = get_tiers_from_set( series_type, 'sg' )
        super(SupraGlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        self.series_type = series_type
        #self.file_type = 'vtl_supraglottal_series'
        return
    
    def _get_data_dict( self ):
        data = dict(
            series = self.series.to_dict( orient = 'list' ),
            series_type = self.series_type,
            sr = self.sr,
            )
        return data
    
    @classmethod
    def from_vtl_tractseq(
            cls,
            file_path: str,
            sr = None,
            ):
        if sr is None:
            sr = 44100/110
        df_vtp = pd.read_csv(
            file_path,
            sep='\s+',
            skiprows= lambda x: _tract_params_from_vtl_tractseq(x),
            header = None,
            )
        x = df_vtp.to_numpy()
        return cls( x, sr = sr )
    
class GlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            series_type: str,
            sr: float = None,
            ):
        tiers = get_tiers_from_set( series_type, 'g' )
        super(GlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        self.series_type = series_type
        #self.file_type = 'glottal_series'
        return
    
    def _get_data_dict( self ):
        data = dict(
            series = self.series.to_dict( orient = 'list' ),
            series_type = self.series_type,
            sr = self.sr,
            )
        return data
    
    @classmethod
    def from_vtl_tractseq(
            cls,
            file_path: str,
            sr = None,
            ):
        if sr is None:
            sr = 44100/110
        df_glp = pd.read_csv(
            file_path,
            sep='\s+',
            skiprows= lambda x: _glottis_params_from_vtl_tractseq(x),
            header = None,
            )
        x = df_glp.to_numpy()
        return cls( x, sr = sr )
    
    def pitch_shift(
            self,
            x: float,
        ):
        # pitch shift is in semitones
        f0_st = hz_to_st(self.series[ 'F0' ])
        f0_shifted = f0_st + x
        self.series[ 'F0' ] = st_to_hz( f0_shifted )
        return
    
class MotorSeries( SupraGlottalSeries, GlottalSeries ):
    def __init__(
            self,
            series: np.ndarray,
            series_type: str,
            sr: float = None,
            ):
        tiers = get_tiers_from_set( series_type, 'm' )
        TargetSeries.__init__(
            self,
            series,
            sr,
            tiers,
            )
        #self.sg_set = sg_set
        #self.g_set = g_set
        self.series_type = series_type

        #self.file_type = 'motor_series'

        return
    
    def _get_data_dict( self ):
        data = dict(
            series = self.series.to_dict( orient = 'list' ),
            series_type = self.series_type,
            sr = self.sr,
            )
        return data
    
    @classmethod
    def from_vtl_tractseq(
            cls,
            file_path: str,
            sr = None,
            ):
        if sr is None:
            sr = 44100/110
        df_vtp = pd.read_csv(
            file_path,
            #delim_whitespace = True,#deprecated
            sep='\s+',
            skiprows= lambda x: _tract_params_from_vtl_tractseq(x),
            header = None,
            )
        df_glp = pd.read_csv(
            file_path,
            #delim_whitespace = True,
            sep='\s+',
            skiprows= lambda x: _glottis_params_from_vtl_tractseq(x),
            header = None,
            )
        x = np.concatenate( [
            df_vtp.to_numpy(),
            df_glp.to_numpy(),
            ],
            axis = 1,
            )
        return cls( x, sr = sr )
    
    def tract( self ):
        #x = self.series[ vtl_sg_tiers[ self.sg_set ] ]
        #sgs = SupraGlottalSeries(
        #    series = x,
        #    sr = self.sr,
        #    sg_set = self.sg_set,
        #    )
        sgs = SupraGlottalSeries(
            series = self,
            series_type = self.series_type,
        )
        
        return sgs
    
    def glottis( self ):
        #x = self.series[ vtl_g_tiers[ self.g_set ] ] # should be unnecessary

        #gs = GlottalSeries(
        #    series = x,
        #    sr = self.sr,
        #    g_set = self.g_set,
        #    )

        gs = GlottalSeries(
            series = self,
            series_type = self.series_type,
        )
        
        return gs
    
    #def save(
    #        self,
    #        file_path: str,
    #        as_type = 'vtl',
    #        **kwargs,
    #        ):
    #    if as_type in [ 'tt', 'tensortract' ]:
    #        tt_ms = self.to_tt( **kwargs )
    #        tt_ms.save( file_path )
    #    elif as_type in [ 'vtl', 'vocaltractlab' ]:
    #        super().save( file_path )
    #    else:
    #        raise ValueError(
    #            f'Unsupported arg as_type: {as_type}'
    #            )
    #    return
    
    #def to_tt(
    #        self,
    #        target_sr = 50,
    #        ):
    #    x = TT_MSRS( self )
    #    x.resample( target_sr )
    #    return x
    
    def to_type(
            self,
            target_type = 'tt',
            target_sr = 50,
            ):
        if target_type not in tier_sets.keys():
            raise ValueError(
                f"""
                Unknown target_type: {target_type}. Must be one of:
                {tier_sets.keys()}
                """
                )
        x = MotorSeries(
            self,
            series_type = target_type,
        )
        x.resample( target_sr )
        return x
    
    # is inherited from GlottalSeries
    #def pitch_shift(
    #        self,
    #        x: float,
    #    ):
    #    # pitch shift is in semitones
    #    f0_st = hz_to_st(self.series[ 'F0' ])
    #    f0_shifted = f0_st + x
    #    self.series[ 'F0' ] = st_to_hz( f0_shifted )
    #    return
    