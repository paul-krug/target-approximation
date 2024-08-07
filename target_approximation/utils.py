


import os
import warnings
import numpy as np
import matplotlib.pyplot as plt
from tools_io import check_if_list_is_valid
from tools_io import make_output_path
from tools_io import is_iterable



hist_kwargs = dict(
    bins = 50,
    histtype = 'step',
    density = False,
    )

state_plot_kwargs = dict(
    HX = dict( color = '#02010e' ),
    HY = dict( color = '#02010e' ),
    JX = dict( color = 'navy' ),
    JA = dict( color = 'navy' ),
    LP = dict( color = 'rebeccapurple' ),
    LD = dict( color = 'rebeccapurple' ),
    VS = dict( color = 'darkmagenta' ),
    VO = dict( color = 'darkmagenta' ),
    TCX = dict(  color = 'darkorange' ),
    TCY = dict(  color = 'darkorange' ),
    TTX = dict(  color = 'darkorange' ),
    TTY = dict(  color = 'darkorange' ),
    TBX = dict(  color = 'darkorange' ),
    TBY = dict(  color = 'darkorange' ),
    TRX = dict(  color = 'darkorange' ),
    TRY = dict(  color = 'darkorange' ),
    TS1 = dict(  color = 'darkorange' ),
    TS2 = dict(  color = 'darkorange' ),
    TS3 = dict(  color = 'darkorange' ),
    F0 = dict( color = 'teal' ),
    PR = dict( color = 'teal' ),
    XB = dict( color = 'turquoise' ),
    XT = dict( color = 'turquoise' ),
    CA = dict( color = 'turquoise' ),
    PL = dict( color = 'turquoise' ),
    RA = dict( color = 'turquoise' ),
    DP = dict( color = 'turquoise' ),
    PS = dict( color = 'turquoise' ),
    FL = dict( color = 'turquoise' ),
    AS = dict( color = 'turquoise' ),
    )

state_hist_kwargs = {
    key: { **val, **hist_kwargs } for key, val in state_plot_kwargs.items()
    } # In Python 3.9+: key: orig | extra

segment_plot_kwargs = dict(
    boundaries = dict( color = 'black' ),
    phonemes = dict( color = 'black', ha = 'center', va = 'center' ),
    )

def get_plot(
    n_rows = 1,
    n_columns = 1,
    axs = None, 
    sharex = True,
    gridspec_kw = {'hspace': 0},
    **kwargs,
    ):
    #if n_columns == 1:
    #    gridspec_kw = gridspec_kw = {'hspace': 0}
    #else:
    #    gridspec_kw = {}
    if axs is None:
        figure, axs = plt.subplots(
            n_rows,
            n_columns,
            figsize = (8, 4/3 * n_rows ),
            sharex = sharex,
            gridspec_kw = gridspec_kw,
            )
    else:
        figure = None
    try:
        if len( axs ) != ( n_rows * n_columns ) and n_columns == 1:
            raise ValueError(
                f"""
                Length of passed matplotlib.pyplot.axes ({len( axs )}) list does not
                equal the number of parameters to plot ({n_rows * n_columns}).
                """
                )
    except Exception:
        axs = [ axs ]
    return [ figure, np.array( axs ) ]

def get_plot_limits(
    data,
    offset = 0.1,
    ):
    _min = np.min( data )
    _max = np.max( data )
    if _min == _max:
        limits = [ _min - 0.75, _max + 0.75 ]
    else:
        limits = [
            _min - offset * np.abs( _max - _min ),
            _max + offset * np.abs( _max - _min ),
            ]
    return limits

def get_valid_tiers(
    parameters,
    container,
    types = str,
    ):
    #container = check_if_list_is_valid( container, str )
    if parameters is None:
        valid_parameters = container
    else:
        parameters = check_if_list_is_valid( parameters, types )
        valid_parameters = []
        for parameter in parameters:
            if parameter in set( container ):
                valid_parameters.append( parameter )
            else:
                warnings.warn(
                    f"""
                    The specified parameter: {parameter} does not exist
                    in the sequence, plotting skipped.
                    """
                    )
    return valid_parameters

def finalize_plot(
    figure = None,
    axs = None,
    hide_labels = True,
    out_file_path = None,
    overwrite = False,
    show = True,
    ):
    if hide_labels:
        for ax in axs.flatten():
            ax.label_outer()
    if ( out_file_path != None ) or show:
        if ( figure != None ) and is_iterable( axs ):
            figure.align_ylabels( axs[:] )
        plt.tight_layout()
        if out_file_path != None:
            out_file_path = make_output_path(
                None,
                out_file_path,
                overwrite,
                )
            plt.savefig( out_file_path )
        if show:
            plt.show()
    return

def make_path( path ):
    if not os.path.exists(
        os.path.dirname( path )
        ):
        os.makedirs(
            os.path.dirname( path ),
            exist_ok=True,
            )
    return