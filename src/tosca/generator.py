
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from default import TOSCA_DEFS_DIR, TOSCA_KEYS_DIR
from xosgenx.generator import XOSProcessor
from xosapi.xos_grpc_client import Empty

class Args:
    pass

current_dir = os.path.dirname(os.path.realpath(__file__))

class TOSCA_Generator:

    def _clean(self, dir=TOSCA_DEFS_DIR):
        filesToRemove = [f for f in os.listdir(dir)]
        for f in filesToRemove:
            if not f.startswith('.'):
                os.remove(dir + '/' + f)

    def generate(self, client):
        print "[XOS-TOSCA] Generating TOSCA"
        self._clean()

        try:
            xproto = client.utility.GetXproto(Empty())
            args = Args()
            args.output = TOSCA_DEFS_DIR
            args.inputs = str(xproto.xproto)
            args.target = os.path.join(current_dir, 'xtarget/tosca.xtarget')
            args.write_to_file = 'target'
            XOSProcessor.process(args)
            print "[XOS-TOSCA] Recipes generated in %s" % args.output
        except Exception as e:
            print "[XOS-TOSCA] Failed to generate TOSCA"
            print e

        try:
            xproto = client.utility.GetXproto(Empty())
            args = Args()
            args.output = TOSCA_KEYS_DIR
            args.inputs = str(xproto.xproto)
            args.target = os.path.join(current_dir, 'xtarget/tosca_keys.xtarget')
            args.write_to_file = 'single'
            args.dest_file = 'KEYS.py'
            XOSProcessor.process(args)
            print "[XOS-TOSCA] TOSCA Keys generated in %s" % args.output
        except Exception as e:
            print "[XOS-TOSCA] Failed to generate TOSCA Keys"
            print e

