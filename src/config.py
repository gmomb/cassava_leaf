import pathlib
import os
import torch
from yacs.config import CfgNode as CN

#GENERAL CONFIG

_C = CN()
_C.PROJECT_DIR = str(pathlib.Path(__file__).parent.parent.absolute())
_C.DATA_DIR = os.path.join(_C.PROJECT_DIR, 'data')
_C.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
_C.RANDOM_STATE = 2021

#Load model
_C.RESUME_CHECKPOINT = False
_C.CHECKPOINT_PATH = '/home/giorgio/Scrivania/Kaggle/hubmap/experiments/resnet34/2020-12-30/unet_best.ckpt'

#Dataset config
_C.DATASET = CN()
_C.DATASET.N_SPLITS = 5

 #DATASET AUGMENTATION
_C.DATASET.VALID_FOLD = 0
_C.DATASET.IMG_HEIGHT = 256
_C.DATASET.IMG_WIDTH = 256
_C.DATASET.H_FLIP_PROB = 0.3
_C.DATASET.P_OPTICAL_DIST = 0.3
_C.DATASET.P_GRID_DIST = 0.3
_C.DATASET.P_PIECEWISE_AFFINE = 0.3
_C.DATASET.P_HUE_SATURATION = 0.3
_C.DATASET.P_CLAHE = 0.3
_C.DATASET.P_RANDOM_BRIGHTNESS = 0.3
_C.DATASET.P_HORIZONATL_FLIP = 0.5
_C.DATASET.P_VERTICAL_FLIP = 0.5
_C.DATASET.P_RANDOM_ROTATE = 0.5
_C.DATASET.P_SHIFT_SCALE = 0.4
_C.DATASET.P_CUTOUT = 0.3
_C.DATASET.NUM_HOLES = 5
_C.DATASET.P_RANDOMRESCROP = 0.3
_C.DATASET.P_CENTERCROP = 0.1
_C.DATASET.NUM_WORKERS = 2

#Loader config
_C.TRAIN_LOADER = CN()
_C.TRAIN_LOADER.BATCH_SIZE = 32
_C.TRAIN_LOADER.NUM_WORKERS = 4

_C.VALID_LOADER = CN()
_C.VALID_LOADER.BATCH_SIZE = 32
_C.VALID_LOADER.NUM_WORKERS = 4

#solver config
_C.SOLVER = CN()
_C.SOLVER.NUM_EPOCHS = 60
_C.SOLVER.ACC_GRADIENT = 2
_C.SOLVER.WARMUP_EPOCHS = 10

#'Adam', SGD, Ranger, RangerQH (quasi hyperbolic momentum), RangerALR (adaptive learning rate)
_C.SOLVER.OPTIMIZER = 'Ranger'
_C.SOLVER.SCHEDULER = 'CosineAnnealingLR'
_C.SOLVER.SCHEDULER_MODE = 'max'
_C.SOLVER.LR = 1e-03
_C.SOLVER.MIN_LR = 1e-05
_C.SOLVER.WEIGHT_DECAY = 1e-6
_C.SOLVER.BETAS = (0.9, 0.999)
_C.SOLVER.AMSGRAD = True
_C.SOLVER.SCHEDULER_REDFACT = 0.1
_C.SOLVER.SCHEDULER_PATIENCE = 3
_C.SOLVER.LOSS = 'BI_TEMPERED'
_C.SOLVER.SMOOTHING_LOSS = 0.03
_C.SOLVER.BIT_T1 = 0.3
_C.SOLVER.BIT_T2 = 0.7

#Parametri per CosineAnnealing
_C.SOLVER.SCHEDULER_COS_CPOCH = 2
_C.SOLVER.SCHEDULER_T0 = 10
_C.SOLVER.SCHEDULER_T_MUL = 2
_C.SOLVER.T_MAX = 6 #PER COSINEANNEALINGLR


#Model config
_C.MODEL = CN()
_C.MODEL.NAME = 'resnext50_32x4d'
_C.MODEL.PRETRAINING = True
_C.MODEL.NUM_CLASSES_OUT = 5