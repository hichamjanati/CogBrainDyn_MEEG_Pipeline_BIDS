"""
===============================================================
11-0. Coregistration: Compute the trans files using the MNE GUI
===============================================================


"""

import os.path as op
import mne
from mne_bids import make_bids_basename
import config


def run_coreg_gui(subject, session=None):
    # Construct the search path for the data file. `sub` is mandatory
    subject_path = op.join('sub-{}'.format(subject))
    # `session` is optional
    if session is not None:
        subject_path = op.join(subject_path, 'ses-{}'.format(session))
    subject_path = op.join(subject_path, config.kind)
    bids_basename = make_bids_basename(subject=subject,
                                       session=session,
                                       task=config.task,
                                       acquisition=config.acq,
                                       run=None,
                                       processing=config.proc,
                                       recording=config.rec,
                                       space=config.space
                                       )
    fpath_deriv = op.join(config.bids_root, 'derivatives',
                          config.PIPELINE_NAME, subject_path)
    fname_out = \
        op.join(fpath_deriv, bids_basename + '-ave.fif')
    mne.gui.coregistration(subject=subject, subjects_dir=config.subjects_dir,
                           inst=fname_out)


if __name__ == '__main__':

    for subject in config.subjects_list:
        run_coreg_gui(subject)
