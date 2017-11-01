# coding: utf-8
from __future__ import absolute_import

from contextlib import contextmanager

from ..base import BaseDecoderAdapter, BaseEncoderAdapter
from ..utils import check_params_type
from .models import (
    GeoCodeRequestParams,
    GeoCodeResponseData,
    ReGeoCodeRequestParams,
    ReGeoCodeResponseData
)


class AMapEncodeAdapter(BaseEncoderAdapter):

    @contextmanager
    def encoder_context(self, func_name, *args, **kwargs):
        encoder = self.all_registered_coders[func_name]
        p_encoder = encoder(*args, **kwargs).prepare()
        yield p_encoder

    def registry_encoders(self):
        self.registry(self.encode_geo_code, GeoCodeRequestParams)
        self.registry(self.encode_regeo_code, ReGeoCodeRequestParams)

    @check_params_type(coder=(type,))
    def registry(self, func, coder):
        return super(AMapEncodeAdapter, self).registry(func, coder)

    def encode_geo_code(self, *args, **kwargs):
        with self.encoder_context('encode_geo_code', *args, **kwargs) as p:
            return p

    def encode_regeo_code(self, *args, **kwargs):
        with self.encoder_context('encode_regeo_code', *args, **kwargs) as p:
            return p


class AMapJsonDecoderAdapter(BaseDecoderAdapter):

    @contextmanager
    def decoder_context(self, func_name, *args, **kwargs):
        decoder = self.all_registered_coders[func_name]
        p_decoder = decoder(*args, **kwargs)
        yield p_decoder

    def registry_decoders(self):
        self.registry(self.decode_geo_code, GeoCodeResponseData)
        self.registry(self.decode_regeo_code, ReGeoCodeResponseData)

    @check_params_type(coder=(type,))
    def registry(self, func, coder):
        return super(AMapJsonDecoderAdapter, self).registry(func, coder)

    def decode_geo_code(self, *args, **kwargs):
        with self.decoder_context('decode_geo_code', *args, **kwargs) as p:
            return p

    def decode_regeo_code(self, *args, **kwargs):
        with self.decoder_context('decode_regeo_code', *args, **kwargs) as p:
            return p
