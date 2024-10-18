#!/usr/bin/env python
#
# Copyright (c) 2024 Numurus, LLC <https://www.numurus.com>.
#
# This file is part of nepi-engine
# (see https://github.com/nepi-engine).
#
# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#

APP_NAME = 'ONVIF_MGR' # Used in display menus
FILE_TYPE = 'APP'
APP_DICT = dict(
    description = 'Application for configuring credetials and connecting to ONVIF type camera and pan-tilt devices',
    pkg_name = 'nepi_app_onvif_mgr',
    group_name = 'DRIVER',
    config_file = 'app_onvif_mgr.yaml',
    app_file = 'onvif_mgr_app_node.py',
    node_name = 'app_onvif_mgr'
)
RUI_DICT = dict(
    rui_menu_name = 'ONVIF_MGR', # RUI menu name or "None" if no rui support
    rui_files = ['NepiAppOnvifMgr.js'],
    rui_main_file ='NepiAppOnvifMgr.js',
    rui_main_class = 'OnvifMgr'
)


