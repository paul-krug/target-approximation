
from .core import TargetSeries
from .core import TargetSequence

from target_approximation.utils import get_file_type

from target_approximation.vocaltractlab import MotorSeries as VTL_MSRS
from target_approximation.vocaltractlab import MotorSequence as VTL_MSQ
from target_approximation.tensortract import MotorSeries as TT_MSRS
from target_approximation.tensortract import MotorSequence as TT_MSQ



file_types = {
    'target_sequence': TargetSequence,
    'target_series': TargetSeries,
    'vtl_motor_sequence': VTL_MSQ,
    'vtl_motor_series': VTL_MSRS,
    'tt_motor_sequence': TT_MSQ,
    'tt_motor_series': TT_MSRS,
    }

def load(
    file_path: str,
    **kwargs,
    ):
    ft = get_file_type( file_path )
    if ft in file_types.keys():
        return file_types[ ft ].from_yaml( file_path, **kwargs )
    elif ft == 'vtl_tractseq_file':
        VTL_MSQ.from_vtl_tractseq( file_path, **kwargs )
    else:
        raise ValueError(
            f"""
            Attempting to load the file {file_path}, however the
            file contains an unknown file type: {ft}. Available
            file types are:
            {file_types.keys()}
            or vtl_tractseq_file.
            """
            )
    return