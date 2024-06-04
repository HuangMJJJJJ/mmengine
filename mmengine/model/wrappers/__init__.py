# Copyright (c) OpenMMLab. All rights reserved.
from mmengine.utils.dl_utils import TORCH_VERSION
from mmengine.utils.version_utils import digit_version
import torch.distributed as dist
from .distributed import MMDistributedDataParallel
from .seperate_distributed import MMSeparateDistributedDataParallel
from .utils import is_model_wrapper

__all__ = [
    'MMDistributedDataParallel', 'is_model_wrapper',
    'MMSeparateDistributedDataParallel'
]

if digit_version(TORCH_VERSION) >= digit_version('2.0.0') and dist.is_available():
    from .fully_sharded_distributed import \
        MMFullyShardedDataParallel  # noqa:F401
    __all__.append('MMFullyShardedDataParallel')
