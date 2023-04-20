import numpy as np
import cma

# Read ENV setting
from tubepol_ant_prof_env_cfg import *

if "hpc" == ENV:
    # Configuration of current project
    Ns = 4
    rec_l_ratio_name_lst = ["l_ratio_%d" % x for x in range(1, Ns - 1, 1)]
    rec_r_ratio_name_lst = ["r_ratio_%d" % x for x in range(1, Ns - 1, 1)]
    rec_cav_h_ratio_name_lst = ["cav_dh_ratio_%d" % x for x in range(0, Ns, 1)]
    rec_cav_dw_ratio_name_lst = ["cav_dw_ratio_%d" % x for x in range(1, Ns - 1, 1)]
    rec_para_name_lst = ["r_i_ratio", "r_o_ratio", "l_o_ratio"] + rec_l_ratio_name_lst + rec_r_ratio_name_lst \
                        + rec_cav_h_ratio_name_lst + rec_cav_dw_ratio_name_lst  # + ["scale_ratio"]

    rec_obj_name_lst = ['S11_M1_MAE', 'S11_M1_MaxNorm', 'S11_M2_MAE', 'S11_M2_MaxNorm', 'RotSym', 'SLL', 'AR_FF_MAE',
                        'AR_FF_MaxNorm', 'Total Fitness']

    # cst_proj_path = "/data/scratch/eex181/TubePolAntProfileGroup/TubePolAntProfileRelativeLimScale_Python_UWB_NoscaleCluster"
    # cst_proj_path = "D:\\cs308\\CST_Project\\TubePolAntProfileGroup\\TubePolAntProfileRelativeLimScale_Python"
    # cst_proj_path = "/data/scratch/eex181/TubePolAntProfileRelativeLimScale_Python_Demo"
    cst_proj_path = r"C:\Users\WayneJu\Desktop\Project\02_CST_Project\TubePolAntProfileRelativeLimScale_Python_Demo"

    proj_cfg_dic = {'env': "hpc",  # hpc
                    'solver': 'T_GPU',  # T_GPU
                    'gpu_num': 1,
                    'resume_flag': False,
                    'project_folder': cst_proj_path,
                    'sim_name': "TubePolAntProfileRelativeLim_Python",
                    'base_para_file_name': "TubePolAntProfileRelativeLimPara.txt",
                    'ff_export_subfolder_name': "Farfield",
                    'rec_para_file_name': "opt_para_list.csv",
                    'rec_para_name_lst': rec_para_name_lst,
                    'rec_objval_file_name': "opt_obj_val.csv",
                    'rec_obj_name_lst': rec_obj_name_lst,
                    'cma_object_save_file_name': '_saved-cma-object_tubepol_ant_prof_relative_lim.pkl',
                    'init_run_id': 1000,  # continue 254
                    }

    # Configuration of current data analyser
    data_analyser_cfg_dic = {'pol_ind': 'LHCP',
                             'np_theta': 360,
                             'np_phi': 5,
                             'norm_factor': 0.1,
                             'taper': -12,
                             'rotsym_goal_val': 0,
                             'rotsym_weight': 1,
                             'cxlevel_goal_val': -35,
                             'cxlevel_weight': 0,  # Switched off
                             'taperang_goal_range': np.array([10, 24]),
                             'taperang_weight': 0,  # Switched off
                             'sll_goal_val': -30,
                             'sll_weight': 1,
                             'ar_ff_goal': 1.5,
                             # 'ar_ff_max_goal': 2,
                             'ar_ff_mae_weight': 1,
                              'ar_ff_max_weight': 1,
                             'spara_eva_freq_range_vec': np.array([80, 110]),
                             'spara_file_name_lst': ['S-Parameters_S1(1),1(1).txt', 'S-Parameters_S1(2),1(1).txt'],
                             'spara_goal_lst': [-43, -43],
                             'spara_mae_weight_lst': [1, 1],
                             'spara_maxnorm_weight_lst': [1, 1]
                             }

    # Configuration of optimizer
    # Generate configuration parameters
    # cma_init_para_list, cma_lb, cma_ub = func_tubepol_ant_prof_relative_opt_cfg_para_calc()
    # cma_init_para_list = [0.995791, 0.168586, 0.735293, 0.612449, 0.986711, 0.034379, 0.660924, 0.179710, 0.995968,
    #                       0.696697, 0.864546, 0.050662, 0.009127]  # A better start from RunID 185 of an optimization
    cma_init_para_list = [0.742695, 0.518469, 0.777166, 0.403107, 0.913746, 0.856273, 0.433590, 0.580654, 0.415830,
                          0.680721, 0.675103, 0.229491, 0.047184]  # RunID 254
    cma_lb = np.zeros(len(cma_init_para_list))
    cma_ub = np.ones(len(cma_init_para_list))
    cma_opts = {'BoundaryHandler': cma.BoundTransform,
                'bounds': [cma_lb, cma_ub],
                'tolfun': 1e-3,
                'tolfunhist': 1e-3,
                'seed': 1234
                }

    optimizer_cfg_dic = {'cma_init_para_list': cma_init_para_list,
                         'cma_sigma': 0.3,
                         'cma_opts': cma_opts,
                         }
else:  # "win"
    # Configuration of current project
    Ns = 4
    rec_l_ratio_name_lst = ["l_ratio_%d" % x for x in range(1, Ns-1, 1)]
    rec_r_ratio_name_lst = ["r_ratio_%d" % x for x in range(1, Ns-1, 1)]
    rec_cav_h_ratio_name_lst = ["cav_dh_ratio_%d" % x for x in range(0, Ns, 1)]
    rec_cav_dw_ratio_name_lst = ["cav_dw_ratio_%d" % x for x in range(1, Ns-1, 1)]
    rec_para_name_lst = ["r_i_ratio", "r_o_ratio", "l_o_ratio"] + rec_l_ratio_name_lst + rec_r_ratio_name_lst \
                        + rec_cav_h_ratio_name_lst + rec_cav_dw_ratio_name_lst  # + ["scale_ratio"]

    rec_obj_name_lst = ['S11_M1_MAE', 'S11_M1_MaxNorm', 'S11_M2_MAE', 'S11_M2_MaxNorm', 'RotSym', 'SLL', 'AR_FF_MAE',
                        'AR_FF_MaxNorm', 'Total Fitness']

    # cst_proj_path = "/data/scratch/eex181/TubePolAntProfileGroup/TubePolAntProfileRelativeLimScale_Python"
    # cst_proj_path = "D:\\cs308\\CST_Project\\TubePolAntProfileGroup\\TubePolAntProfileRelativeLimScale_Python_Demo"
    cst_proj_path = "C:\\Users\\WayneJu\\Desktop\\Project\\02_CST_Project\\TubePolAntProfileRelativeLimScale_Python_Demo"

    proj_cfg_dic = {'env': "win",    # hpc
                    'solver': 'T',    # T_GPU
                    'gpu_num': 1,
                    'resume_flag': False,
                    'project_folder': cst_proj_path,
                    'sim_name': "TubePolAntProfileRelativeLim_Python",
                    'base_para_file_name': "TubePolAntProfileRelativeLimPara.txt",
                    'ff_export_subfolder_name': "Farfield",
                    'rec_para_file_name': "opt_para_list.csv",
                    'rec_para_name_lst': rec_para_name_lst,
                    'rec_objval_file_name': "opt_obj_val.csv",
                    'rec_obj_name_lst': rec_obj_name_lst,
                    'cma_object_save_file_name': '_saved-cma-object_tubepol_ant_prof_relative_lim.pkl',
                    'init_run_id': 1,  # 1201
                    }

    # Configuration of current data analyser
    data_analyser_cfg_dic = {'pol_ind': 'LHCP',
                             'np_theta': 360,
                             'np_phi': 5,
                             'norm_factor': 0.1,
                             'taper': -12,
                             'rotsym_goal_val': 0,
                             'rotsym_weight': 1,
                             'cxlevel_goal_val': -35,
                             'cxlevel_weight': 0,   # Switched off
                             'taperang_goal_range': np.array([10, 24]),
                             'taperang_weight': 0,  # Switched off
                             'sll_goal_val': -30,
                             'sll_weight': 1,
                             'ar_ff_goal': 1.5,
                             # 'ar_ff_max_goal': 2,
                             'ar_ff_mae_weight': 1,
                             'ar_ff_max_weight': 1,
                             'spara_eva_freq_range_vec': np.array([80, 110]),
                             'spara_file_name_lst': ['S-Parameters_S1(1),1(1).txt', 'S-Parameters_S1(2),1(1).txt'],
                             'spara_goal_lst': [-43, -43],
                             'spara_mae_weight_lst': [1, 1],
                             'spara_maxnorm_weight_lst': [1, 1]
                             }

    # Configuration of optimizer
    # Generate configuration parameters
    # cma_init_para_list, cma_lb, cma_ub = func_tubepol_ant_prof_relative_opt_cfg_para_calc()
    # cma_init_para_list = [0.995791, 0.168586, 0.735293, 0.612449, 0.986711, 0.034379, 0.660924, 0.179710, 0.995968,
    #                       0.696697, 0.864546, 0.050662, 0.009127]   # A better start from RunID 185 of an optimization
    cma_init_para_list = [0.742695, 0.518469, 0.777166, 0.403107, 0.913746, 0.856273, 0.433590, 0.580654, 0.415830,
                          0.680721, 0.675103, 0.229491, 0.047184]  # RunID 254

    cma_lb = np.zeros(len(cma_init_para_list))
    cma_ub = np.ones(len(cma_init_para_list))
    cma_opts = {'BoundaryHandler': cma.BoundTransform,
                'bounds': [cma_lb, cma_ub],
                'tolfun': 1e-3,
                'tolfunhist': 1e-3,
                'seed': 1234
                }

    optimizer_cfg_dic = {'cma_init_para_list': cma_init_para_list,
                         'cma_sigma': 0.3,
                         'cma_opts': cma_opts,
                         }
