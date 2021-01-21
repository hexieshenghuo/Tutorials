.. py:module:: megengine.functional
.. currentmodule:: megengine.functional

=========================
megengine.functional 模块
=========================

.. py:module:: megengine.functional.tensor
.. currentmodule:: megengine.functional.tensor

张量相关
--------

创建张量
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   zeros
   zeros_like
   ones
   ones_like
   full
   full_like
   arange
   linspace
   eye

处理张量
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   broadcast_to
   concat
   stack
   split
   gather
   scatter
   where
   cond_take
   transpose
   reshape
   flatten
   expand_dims
   squeeze

.. py:module:: megengine.functional.elemwise
.. currentmodule:: megengine.functional.elemwise

Element-wise
------------

基本运算
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   add
   sub
   mul
   div
   floor_div
   neg
   pow
   mod
   abs
   exp
   expm1
   log
   log1p
   sqrt
   square
   round
   ceil
   floor
   maximum
   minimum
   clip

三角运算
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   cos
   sin
   tan
   acos
   asin
   atan
   atan2
   cosh
   sinh
   tanh
   acosh
   asinh
   atanh

位运算
~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   left_shift
   right_shift

逻辑运算
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   logical_and
   logical_not
   logical_or
   logical_xor

比较运算
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   equal
   not_equal
   less
   less_equal
   greater
   greater_equal

其它运算
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   sigmoid
   hsigmoid
   relu
   relu6
   hswish

.. py:module:: megengine.functional.math
.. currentmodule:: megengine.functional.math

数学相关
--------
.. autosummary::
   :toctree: api
   :nosignatures:

   isnan
   isinf
   sign
   sum
   prod
   mean
   var
   std
   norm
   normalize
   min
   max
   sort
   argmin
   argmax
   argsort
   topk

.. py:module:: megengine.functional.nn
.. currentmodule:: megengine.functional.nn

神经网络相关
------------

卷积函数
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   conv1d
   conv2d
   local_conv2d
   conv_transpose2d

池化函数
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   avg_pool2d
   max_pool2d
   adaptive_avg_pool2d
   adaptive_max_pool2d

非线性激活函数
~~~~~~~~~~~~~~
部分激活函数如 :py:meth:`megengine.functional.elemwise.relu` 实现在 :py:mod:`megengine.functional.elemwise` 模块中。

.. autosummary::
   :toctree: api
   :nosignatures:

   prelu
   leaky_relu
   softplus
   softmax
   logsoftmax
   logsigmoid
   logsumexp

归一化函数
~~~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   batch_norm

线性函数
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   linear

随机失活函数
~~~~~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   dropout

稀疏函数
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   one_hot
   indexing_one_hot
   embedding

计算机视觉常用
~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   interpolate
   remap
   warp_perspective
   roi_pooling
   roi_align
   nms

其它函数
~~~~~~~~
.. autosummary::
   :toctree: api
   :nosignatures:

   dot
   matmul
   svd

.. _loss-functions:
.. currentmodule:: megengine.functional.loss

损失函数
--------
.. autosummary::
   :toctree: api
   :nosignatures:

   l1_loss
   square_loss
   hinge_loss
   binary_cross_entropy
   cross_entropy

.. py:module:: megengine.functional.distributed
.. currentmodule:: megengine.functional.distributed

分布式相关
----------
.. autosummary::
   :toctree: api
   :nosignatures:

   all_gather
   all_reduce_max
   all_reduce_min
   all_reduce_sum
   all_to_all
   broadcast
   collective_comm
   gather
   reduce_scatter_sum
   reduce_sum
   remote_recv
   remote_send
   scatter

.. py:module:: megengine.functional.utils
.. currentmodule:: megengine.functional.utils

Utils
--------
.. autosummary::
   :toctree: api
   :nosignatures:

   copy
   topk_accuracy
