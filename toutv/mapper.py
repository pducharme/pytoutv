# Copyright (c) 2012, Benjamin Vanheuverzwijn <bvanheu@gmail.com>
# All rights reserved.
#
# Thanks to Marc-Etienne M. Leveille
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import toutv.bos as bos


class Mapper:
    def create(self, klass):
        return klass()


class JsonMapper(Mapper):
    def dto_to_bo(self, dto, klass):
        bo = self.create(klass)
        bo_vars = vars(bo)

        for key in bo_vars.keys():
            value = dto[key]

            if isinstance(value, dict):
                if value['__type'] in ['GenreDTO:#RC.Svc.Web.TouTV',
                                       'GenreDTO:RC.Svc.Web.TouTV']:
                    value = self.dto_to_bo(value, bos.Genre)
                elif value['__type'] in ['EmissionDTO:#RC.Svc.Web.TouTV',
                                         'EmissionDTO:RC.Svc.Web.TouTV']:
                    value = self.dto_to_bo(value, bos.Emission)
                elif value['__type'] in ['EpisodeDTO:#RC.Svc.Web.TouTV',
                                         'EpisodeDTO:RC.Svc.Web.TouTV']:
                    value = self.dto_to_bo(value, bos.Episode)
            setattr(bo, key, value)

        return bo