# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree. An additional grant of patent rights
# can be found in the PATENTS file in the same directory.
"""
Modified by:        Emanuele Bugliarello (@e-bug)
Date last modified: 9/4/2019
"""

from .dictionary import Dictionary, TruncatedDictionary
from .fairseq_dataset import FairseqDataset
from .backtranslation_dataset import BacktranslationDataset
from .concat_dataset import ConcatDataset
from .indexed_dataset import IndexedDataset, IndexedCachedDataset, IndexedInMemoryDataset, IndexedRawTextDataset
from .language_pair_dataset import LanguagePairDataset
from .tags_language_pair_dataset import TagsLanguagePairDataset
from .monolingual_dataset import MonolingualDataset
from .round_robin_zip_datasets import RoundRobinZipDatasets
from .token_block_dataset import TokenBlockDataset
from .transform_eos_dataset import TransformEosDataset

from .iterators import (
    CountingIterator,
    EpochBatchIterator,
    GroupedIterator,
    ShardedIterator,
)

__all__ = [
    'BacktranslationDataset',
    'ConcatDataset',
    'CountingIterator',
    'Dictionary',
    'EpochBatchIterator',
    'FairseqDataset',
    'GroupedIterator',
    'IndexedCachedDataset',
    'IndexedDataset',
    'IndexedInMemoryDataset',
    'IndexedRawTextDataset',
    'LanguagePairDataset',
    'TagsLanguagePairDataset',
    'MonolingualDataset',
    'RoundRobinZipDatasets',
    'ShardedIterator',
    'TokenBlockDataset',
    'TransformEosDataset',
]