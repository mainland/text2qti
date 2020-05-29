# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Geoffrey M. Poore
# All rights reserved.
#
# Licensed under the BSD 3-Clause License:
# http://opensource.org/licenses/BSD-3-Clause
#


import datetime
from typing import Dict, Optional
from .quiz import Image


MANIFEST_START = '''\
<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns:bb="http://www.blackboard.com/content-packaging/" identifier="man00001">
  <organizations/>
  <resources>
    <resource bb:file="res00001.dat" identifier="res00001" type="assessment/x-bb-qti-test" xml:base="res00001"/>
'''

IMAGE = '''\
    <resource identifier="text2qti_image_{ident}" type="webcontent" href="{path}">
      <file href="{path}"/>
    </resource>
'''

MANIFEST_END = '''\
  </resources>
</manifest>
'''


def imsmanifest(*,
                manifest_identifier: str,
                assessment_identifier: str,
                dependency_identifier: str,
                images: Dict[str, Image],
                date: Optional[str]=None) -> str:
    '''
    Generate `imsmanifest.xml`.
    '''
    if date is None:
        date = str(datetime.date.today())
    xml = []
    xml.append(MANIFEST_START.format(manifest_identifier=manifest_identifier,
                                     assessment_identifier=assessment_identifier,
                                     dependency_identifier=dependency_identifier,
                                     date=date))
    for image in images.values():
        xml.append(IMAGE.format(ident=image.id, path=image.qti_xml_path))
    xml.append(MANIFEST_END)
    return ''.join(xml)
