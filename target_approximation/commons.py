
from .core import TargetSeries
from .core import TargetSequence

from target_approximation.utils import get_file_type

from target_approximation.vocaltractlab import MotorSeries
from target_approximation.vocaltractlab import SupraGlottalSeries
from target_approximation.vocaltractlab import GlottalSeries

from target_approximation.vocaltractlab import MotorSequence
from target_approximation.vocaltractlab import SupraGlottalSequence
from target_approximation.vocaltractlab import GlottalSequence



file_types = {
    "<class 'target_approximation.core.TargetSeries'>": TargetSeries,
    "<class 'target_approximation.core.TargetSequence'>": TargetSequence,
    "<class 'target_approximation.vocaltractlab.core.MotorSeries'>": MotorSeries,
    "<class 'target_approximation.vocaltractlab.core.SupraGlottalSeries'>": SupraGlottalSeries,
    "<class 'target_approximation.vocaltractlab.core.GlottalSeries'>": GlottalSeries,
    "<class 'target_approximation.vocaltractlab.core.MotorSequence'>": MotorSequence,
    "<class 'target_approximation.vocaltractlab.core.SupraGlottalSequence'>": SupraGlottalSequence,
    "<class 'target_approximation.vocaltractlab.core.GlottalSequence'>": GlottalSequence,
    }

def load(
    file_path: str,
    **kwargs,
    ):
    ft = get_file_type( file_path )
    if ft in file_types.keys():
        x = file_types[ ft ].from_yaml( file_path, **kwargs )
    elif ft == 'vtl_tractseq_file':
        x = MotorSeries.from_vtl_tractseq( file_path, **kwargs )
    else:
        raise ValueError(
            f"""
            Attempting to load the file {file_path}, however the
            file contains an unknown file type: {ft}. Available
            file types are:
            {list( file_types.keys() )}
            or vtl_tractseq_file.
            """
            )
    return x