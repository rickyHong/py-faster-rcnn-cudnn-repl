# <<<<<<< HEAD
# from .pycaffe import Net, SGDSolver
# from ._caffe import set_mode_cpu, set_mode_gpu, set_device, Layer, get_solver, layer_type_list, set_random_seed
# =======
from .pycaffe import Net, SGDSolver, NesterovSolver, AdaGradSolver, RMSPropSolver, AdaDeltaSolver, AdamSolver, NCCL, Timer
from ._caffe import init_log, log, set_mode_cpu, set_mode_gpu, set_device, Layer, get_solver, layer_type_list, set_random_seed, solver_count, set_solver_count, solver_rank, set_solver_rank, set_multiprocess, has_nccl
from ._caffe import __version__
# >>>>>>> 5c6a2905cf8b9463f33b28960feb3a3451321cf9
from .proto.caffe_pb2 import TRAIN, TEST
from .classifier import Classifier
from .detector import Detector
from . import io
from .net_spec import layers, params, NetSpec, to_proto
