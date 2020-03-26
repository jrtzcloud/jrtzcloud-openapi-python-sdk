# -*- coding: utf-8 -*-
#
# Copyright 2002-2020 Investoday Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
from datetime import datetime
import hashlib
import json
import random
import sys
import time
import uuid
import warnings

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import common
from common.exception.jrtzcloud_sdk_exception import CloudSDKException
from common.http.request import ApiRequest
from common.http.request import RequestInternal
from common.profile.client_profile import ClientProfile
from common.sign import Sign

warnings.filterwarnings("ignore")

_json_content = 'application/json;charset=utf-8'
_json_patch_content = 'application/json-patch+json;charset=utf-8'
_multipart_content = 'multipart/form-data'
_form_urlencoded_content = 'application/x-www-form-urlencoded;charset=utf-8'

class AbstractClient(object):
    _requestPath = '/'
    _params = {}
    _apiVersion = ''
    _endpoint = ''
    _region = 'ap-shenzhen'
    _sdkVersion = 'SDK_PYTHON_%s' % common.__version__
    _default_content_type = _form_urlencoded_content

    def __init__(self, credential, region=None, profile=None):
        if credential is None:
            raise CloudSDKException(
                "InvalidCredential", "Credential is None or invalid")
        self.credential = credential

        self.profile = profile or ClientProfile()
        self.apiVersion = self.profile.httpProfile.apiVersion or self._apiVersion
        self.region = region or self.profile.httpProfile.region or self._region
        self.request = ApiRequest(self.get_endpoint(), self.profile.httpProfile.reqTimeout)
        if self.profile.httpProfile.keepAlive:
            self.request.set_keep_alive()

        # self.secretId = self.credential.secretId
        # self.secretKey = self.credential.secretKey
        # self.defaultRegion = self.region or ''
        # self.reqMethod = self.profile.httpProfile.reqMethod
        # self.signMethod = self.profile.signMethod
        # self.requestHost = '.'.join((self._service_name, self.profile.httpProfile.endpoint))
        # # self.apiRequest = ApiRequest(self.requestHost, req_timeout=self.profile.httpProfile.reqTimeout)
        # self.token = self.credential.token or ''

    def _fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        return self._format_params(None, params)

    def _format_params(self, prefix, params):
        d = {}
        if params is None:
            return d

        if not isinstance(params, (tuple, list, dict)):
            d[prefix] = params
            return d

        if isinstance(params, (list, tuple)):
            for idx, item in enumerate(params):
                if prefix:
                    key = "{0}.{1}".format(prefix, idx)
                else:
                    key = "{0}".format(idx)
                d.update(self._format_params(key, item))
            return d

        if isinstance(params, dict):
            for k, v in params.items():
                if prefix:
                    key = '{0}.{1}'.format(prefix, k)
                else:
                    key = '{0}'.format(k)
                d.update(self._format_params(key, v))
            return d

        raise CloudSDKException("ClientParamsError", "some params type error")

    def _build_req_inter(self, action, params, req_inter, options=None):
        options = options or {}
        if self.profile.signMethod == "JC1-HMAC-SHA256" or options.get("IsMultipart") is True:
            self._build_req_with_jc1_signature(action, params, req_inter, options)
        elif self.profile.signMethod in ("HmacSHA1", "HmacSHA256"):
            self._build_req_with_old_signature(action, params, req_inter)
        else:
            raise CloudSDKException("ClientError", "Invalid signature method.")

    def _build_req_with_old_signature(self, action, params, req):
        params = copy.deepcopy(self._fix_params(params))
        params['Action'] = action[0].upper() + action[1:]
        # params['RequestClient'] = self._sdkVersion
        params['Nonce'] = random.randint(1, sys.maxsize)
        params['Timestamp'] = int(time.time())
        params['Version'] = self.apiVersion

        if self.region:
            params['Region'] = self.region

        if self.credential.token:
            params['Token'] = self.credential.token

        if self.credential.secretId:
            params['SecretId'] = self.credential.secretId

        if self.profile.signMethod:
            params['SignatureMethod'] = self.profile.signMethod

        if self.profile.language:
            params['Language'] = self.profile.language

        signInParam = self._format_sign_string(params)
        params['Signature'] = Sign.sign(str(self.credential.secretKey),
                                        str(signInParam),
                                        str(self.profile.signMethod))

        req.data = urlencode(params)
        req.header["Content-Type"] = "application/x-www-form-urlencoded"

    def _build_req_with_jc1_signature(self, action, params, req, options=None):
        content_type = self._default_content_type
        if req.method == 'GET':
            content_type = _form_urlencoded_content
        elif req.method in ['POST', 'PUT', 'DELETE']:
            content_type = _json_content
        elif req.method in ['PATCH']:
            content_type = _json_patch_content
        options = options or {}
        if options.get("IsMultipart"):
            content_type = _multipart_content
        req.header["Content-Type"] = content_type
        req.header["X-JC-RequestId"] = '12345678'   #for test
        endpoint = self._get_endpoint()
        service = self._get_service()
        # print(3331,service)
        # service = endpoint.split('.')[0]
        # print(service)
        timestamp = int(time.time())
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

        req.header["Host"] = endpoint
        # req.header["X-TC-Action"] = action[0].upper() + action[1:]
        # req.header["X-TC-RequestClient"] = self._sdkVersion
        req.header["X-JC-Timestamp"] = timestamp
        req.header["X-JC-Version"] = self.apiVersion
        # if self.profile.unsignedPayload is True:
        #     req.header["X-TC-Content-SHA256"] = "UNSIGNED-PAYLOAD"
        if self.region:
            req.header['X-JC-Region'] = self.region
        # if self.credential.token:
        #     req.header['X-TC-Token'] = self.credential.token
        # if self.profile.language:
        #     req.header['X-TC-Language'] = self.profile.language

        signature = self._get_jc1_signature(params, req, date, service, options)

        auth = "JC1-HMAC-SHA256"
        auth += " Credential=%s/%s/%s/jc1_request" % (self.credential.secretId, date, service)
        auth += ", SignedHeaders=content-type;host, Signature=%s" % signature
        req.header["Authorization"] = auth

    def _get_jc1_signature(self, params, req, date, service, options=None):
        options = options or {}
        canonical_uri = req.uri
        canonical_querystring = ''

        if req.method == 'GET' and options.get("IsMultipart") is not True:
            params = copy.deepcopy(self._fix_params(params))
            req.data = urlencode(params)
            canonical_querystring = req.data
            payload = ""
        else:
            ct = req.header["Content-Type"]
            if ct in [_json_content, _json_patch_content]:
                req.data = json.dumps(params)
            elif ct == _multipart_content:
                boundary = uuid.uuid4().hex
                req.header["Content-Type"] = ct + "; boundary=" + boundary
                req.data = self._get_multipart_body(params, boundary, options)
            else:
                raise Exception("Unsupported content type: %s" % ct)

            payload = req.data

        # if req.header.get("X-TC-Content-SHA256") == "UNSIGNED-PAYLOAD":
        #     payload = "UNSIGNED-PAYLOAD"

        if sys.version_info[0] == 3 and isinstance(payload, type("")):
            payload = payload.encode("utf8")
        payload_hash = hashlib.sha256(payload).hexdigest()

        canonical_headers = 'content-type:%s\nhost:%s\n' % (
            req.header["Content-Type"], req.header["Host"])
        signed_headers = 'content-type;host'
        canonical_request = '%s\n%s\n%s\n%s\n%s\n%s' % (req.method,
                                                        canonical_uri,
                                                        canonical_querystring,
                                                        canonical_headers,
                                                        signed_headers,
                                                        payload_hash)

        algorithm = 'JC1-HMAC-SHA256'
        credential_scope = date + '/' + service + '/jc1_request'
        if sys.version_info[0] == 3:
            canonical_request = canonical_request.encode("utf8")
        digest = hashlib.sha256(canonical_request).hexdigest()
        string2sign = '%s\n%s\n%s\n%s' % (algorithm,
                                          req.header["X-JC-Timestamp"],
                                          credential_scope,
                                          digest)
        # print(string2sign)
        signature = Sign.sign_tc3(self.credential.secretKey, date, service, string2sign)
        return signature

    # it must return bytes instead of string
    def _get_multipart_body(self, params, boundary, options=None):
        if options is None:
            options = {}
        # boundary and params key will never contain unicode characters
        boundary = boundary.encode()
        binparas = options.get("BinaryParams", [])
        body = b''
        for k, v in params.items():
            kbytes = k.encode()
            body += b'--%s\r\n' % boundary
            body += b'Content-Disposition: form-data; name="%s"' % kbytes
            if k in binparas:
                body += b'; filename="%s"\r\n' % kbytes
            else:
                body += b"\r\n"
                if isinstance(v, list) or isinstance(v, dict):
                    v = json.dumps(v)
                    body += b'Content-Type: application/json\r\n'
            if sys.version_info[0] == 3 and isinstance(v, type("")):
                v = v.encode()
            body += b'\r\n%s\r\n' % v
        if body != b'':
            body += b'--%s--\r\n' % boundary
        return body

    def _check_status(self, resp_inter):
        if resp_inter.status not in [200,201]:
            print(resp_inter.status)
            # raise CloudSDKException("ServerNetworkError", resp_inter.data)

    def _format_sign_string(self, params):
        formatParam = {}
        for k in params:
            formatParam[k.replace('_', '.')] = params[k]
        strParam = '&'.join('%s=%s' % (k, formatParam[k]) for k in sorted(formatParam))
        msg = '%s%s%s?%s' % (self.profile.httpProfile.reqMethod, self._get_endpoint(), self._requestPath, strParam)
        return msg

    def _get_endpoint(self):
        endpoint = self.profile.httpProfile.endpoint
        if endpoint is None:
            endpoint = self._endpoint
        endpoint = endpoint .split('//')[1] if '//' in endpoint else endpoint
        # endpoint = endpoint .split(':')[0] if ':' in endpoint else endpoint
        return endpoint

    def _get_service(self):
        return self._svc_path

    def get_endpoint(self):
        endpoint = self.profile.httpProfile.endpoint
        if endpoint is None:
            endpoint = self._endpoint
        return endpoint

    def call(self, action, params, options=None):
        endpoint = self._get_endpoint()
        self._requestPath = action
        req_inter = RequestInternal(endpoint,
                                    self.profile.httpProfile.reqMethod,
                                    self._requestPath)
        self._build_req_inter(action, params, req_inter, options)
        # print(req_inter)
        resp_inter = self.request.send_request(req_inter)
        self._check_status(resp_inter)
        data = resp_inter.data
        if sys.version_info[0] > 2:
            data = data.decode()
        else:
            data = data.decode('UTF-8')
        return data
