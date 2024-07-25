


import numpy as np
import pandas as pd

from typing import List, Optional, Dict, Any, Union, Tuple, Iterable

from target_approximation.tensortract.utils import supraglottal_tiers as tt_sg_tiers
from target_approximation.tensortract.utils import glottal_tiers as tt_g_tiers
from target_approximation.tensortract.utils import ms_file_extensions

from target_approximation.core import TargetSequence
from target_approximation.core import TargetSeries



class SupraGlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sg_set: str = 'jd3',
            ):
        tiers = tt_sg_tiers[ sg_set ]
        super(SupraGlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
class GlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            g_set: str = 'default',
            ):
        tiers = tt_g_tiers[ g_set ]
        super(GlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
class MotorSequence( TargetSequence ):
    def __init__(
            self,
            targets,
            sg_set: str = 'jd3',
            g_set: str = 'default',
            ):
        tiers = tt_sg_tiers[ sg_set ] + tt_g_tiers[ g_set ]
        super(MotorSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
    def to_series(
            self,
            sr: Optional[ float ] = None,
            ):
        x = MotorSeries.from_sequence( self, sr )
        return x

class SupraGlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            sg_set = 'jd3',
            ):
        tiers = tt_sg_tiers[ sg_set ]
        super(SupraGlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        return
    
class GlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            g_set = 'default',
            ):
        tiers = tt_g_tiers[ g_set ]
        super(GlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        return
    
class MotorSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            sg_set = 'default',
            g_set = 'default',
            ):
        tiers = tt_sg_tiers[ sg_set ] + tt_g_tiers[ g_set ]
        super(MotorSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        self.sg_set = sg_set
        self.g_set = g_set
        return
    
    @classmethod
    def load(
            cls,
            file_path: str,
            sr = None,
            ):
        if file_path.endswith( '.npy' ):
            #series = np.load( file_path )
            pass
        elif any( [
                file_path.endswith( ext )
                for ext in ms_file_extensions
                ] ):
            ms = MotorSequence.load( file_path )
            mss = ms.to_series( sr = sr )
        elif file_path.endswith( '.csv' ):
            mss = pd.read_csv( file_path )
        else:
            raise ValueError(
                f'Unsupported file extension: {file_path}'
                )
        return cls( mss, sr = sr )
    
    def tract( self ):
        x = self.series[ tt_sg_tiers[ self.sg_set ] ]

        sgs = SupraGlottalSeries(
            series = x,
            sr = self.sr,
            sg_set = self.sg_set,
            )
        
        return sgs
    
    def glottis( self ):
        x = self.series[ tt_g_tiers[ self.g_set ] ]

        gs = GlottalSeries(
            series = x,
            sr = self.sr,
            g_set = self.g_set,
            )
        
        return gs