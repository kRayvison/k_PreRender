#!/usr/bin/env python
# encoding:utf-8
# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os, sys, re
import time


def main(*args):
    print ("custome prerender  start ----------- ")
    info_dict = args[0]
    # print (info_dict) #prerender  info   dict
    # print (info_dict["user_id"]) #int
    # print (info_dict["start"])   #int
    # print (info_dict["mapping"]) #dict
    print (info_dict["task_id"])  # int
    # print (info_dict["plugins"])  #dict
    # print (info_dict["rendersetting"]) #dict

    print (" SET Redshift Render attribute")

    for i in pm.ls(type='RedshiftOptions'):
        if i.hasAttr("copyToTextureCache"):
            i.copyToTextureCache.set(1)
            print("copyToTextureCache is on")

        if i.hasAttr("percentageOfGPUMemoryToUse"):
            print ("percentageOfGPUMemoryToUse is 90%")
            i.percentageOfGPUMemoryToUse.set(90)
        if i.hasAttr("maxNumGPUMBForIrradiancePointCloudHierarchy"):
            print
            "Irradiance Point Cloud is 256"
            i.maxNumGPUMBForIrradiancePointCloudHierarchy.set(256)
        if i.hasAttr("maxNumGPUMBForForICPHierarchy"):
            print
            "Irradiance cache is 256"
            i.maxNumGPUMBForForICPHierarchy.set(256)
        if i.hasAttr("percentageOfFreeMemoryUsedForTextureCache"):
            print
            "percentageOfFreeMemoryUsedForTextureCache is 15%"
            i.percentageOfFreeMemoryUsedForTextureCache.set(15)
        if i.hasAttr("maxNumGPUMBForTextureCache"):
            print
            "maxNumGPUMBForTextureCache is 256"
            i.maxNumGPUMBForTextureCache.set(256)
        if i.hasAttr("maxNumCPUMBForTextureCache"):
            print
            "maxNumCPUMBForTextureCache is 4096"
            i.maxNumCPUMBForTextureCache.set(4096)
        if i.hasAttr("numGPUMBToReserveForRays"):
            print
            "numGPUMBToReserveForRays is 0"
            i.numGPUMBToReserveForRays.set(0)

    print
    "custome prerender  end ----------- "

#RS 插件配置的环境变量
# PATH=%PATH%;D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\bin;C:\Program Files\Autodesk\Maya2016\bin
# REDSHIFT_COREDATAPATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46
# REDSHIFT_PLUG_IN_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\2016\nt-x86-64
# REDSHIFT_SCRIPT_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\scripts
# REDSHIFT_XBMLANGPATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\icons
# REDSHIFT_RENDER_DESC_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\rendererDesc
# REDSHIFT_CUSTOM_TEMPLATE_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\scripts\NETemplates
# REDSHIFT_MAYAEXTENSIONSPATH = %REDSHIFT_PLUG_IN_PATH%\extensions
# REDSHIFT_PROCEDURALSPATH = %REDSHIFT_COREDATAPATH%\Procedurals
# MAYA_PLUG_IN_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\2016\nt-x86-64
# MAYA_SCRIPT_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\scripts;C:\Users\enfuzion\AppData\Local\Temp\16195662
# PYTHONPATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\scripts
# XBMLANGPATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\icons
# MAYA_RENDER_DESC_PATH = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common\rendererDesc
# MAYA_CUSTOM_TEMPLATE_PATH = %REDSHIFT_CUSTOM_TEMPLATE_PATH%
# REDSHIFT_PREFSPATH = B:\plugins\maya_new\redshift\PREFS\1080.xml
# REDSHIFT_LOCALDATAPATH = D:\temp\REDSHIFT\CACHE\G0
# REDSHIFT_COMMON_ROOT = D:\plugins\maya\redshift\software\driver0\redshift_2.5.46\Plugins\Maya\Common
# LOCALAPPDATA = D:\temp\REDSHIFT\CACHE\G0





