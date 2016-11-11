#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: oesteban
# @Date:   2015-11-19 16:44:27
# @Last Modified by:   oesteban
""" niworkflows setup script """

PACKAGE_NAME = 'niworkflows'

def main():
    """ Install entry-point """
    from os import path as op
    from glob import glob
    from inspect import getfile, currentframe
    from setuptools import setup, find_packages
    from io import open  # pylint: disable=W0622

    this_path = op.dirname(op.abspath(getfile(currentframe())))

    # Python 3: use a locals dictionary
    # http://stackoverflow.com/a/1463370/6820620
    ldict = locals()

    # Get version and release info, which is all stored in niworkflows/info.py
    module_file = op.join(this_path, PACKAGE_NAME, 'info.py')
    with open(module_file) as infofile:
        pythoncode = [line for line in infofile.readlines() if not line.strip().startswith('#')]
        exec('\n'.join(pythoncode), globals(), ldict)

    setup(
        name=PACKAGE_NAME,
        version=ldict['__version__'],
        description=ldict['__description__'],
        long_description=ldict['__longdesc__'],
        author=ldict['__author__'],
        author_email=ldict['__email__'],
        email=ldict['__email__'],
        maintainer=ldict['__maintainer__'],
        maintainer_email=ldict['__email__'],
        license=ldict['__license__'],
        url=ldict['URL'],
        download_url=ldict['DOWNLOAD_URL'],
        classifiers=ldict['CLASSIFIERS'],
        packages=find_packages(),
        zip_safe=False,
        package_data={'niworkflows': ['data/t1-mni_registration*.json']},
        # Dependencies handling
        setup_requires=ldict['SETUP_REQUIRES'],
        install_requires=list(set(ldict['REQUIRES'])),
        dependency_links=ldict['LINKS_REQUIRES'],
        tests_require=ldict['TESTS_REQUIRES'],
        extras_require=ldict['EXTRA_REQUIRES'],
    )
    download_data()


def download_data():
    """Download all templates"""
    from niworkflows.data import get_mni_template
    from niworkflows.data.getters import (
        get_brainweb_1mm_normal,
        get_ds003_downsampled,
        get_mni_template,
        get_mni_template_ras,
        get_ants_oasis_template,
        get_ants_oasis_template_ras,
        get_mni_epi,
        get_mni152_nlin_sym_las,
        get_mni152_nlin_sym_ras,
        get_mni_icbm152_linear,
        get_mni_icbm152_nlin_asym_09c
    )
    get_brainweb_1mm_normal()
    get_ds003_downsampled()
    get_mni_template()
    get_mni_template_ras()
    get_ants_oasis_template()
    get_ants_oasis_template_ras()
    get_mni_epi()
    get_mni152_nlin_sym_las()
    get_mni152_nlin_sym_ras()
    get_mni_icbm152_linear()
    get_mni_icbm152_nlin_asym_09c()


if __name__ == '__main__':
    main()