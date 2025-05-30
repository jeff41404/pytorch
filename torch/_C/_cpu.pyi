from torch.types import _bool, _int

# Defined in torch/csrc/cpu/Module.cpp

def _is_avx2_supported() -> _bool: ...
def _is_avx512_supported() -> _bool: ...
def _is_avx512_vnni_supported() -> _bool: ...
def _is_avx512_bf16_supported() -> _bool: ...
def _is_amx_tile_supported() -> _bool: ...
def _is_amx_fp16_supported() -> _bool: ...
def _init_amx() -> _bool: ...
def _L1d_cache_size() -> _int: ...
def _L2_cache_size() -> _int: ...
