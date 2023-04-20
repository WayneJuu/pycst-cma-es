import os
import pickle
import pandas as pd


def func_save_ins_to_file(project_folder, save_file_name, save_obj):
    full_save_file = os.path.join(project_folder, save_file_name)

    with open(full_save_file, 'wb') as fdump:
        pickle.dump(save_obj, fdump)


def func_load_ins_from_file(full_save_file):
    with open(full_save_file, 'rb') as fload:
        es = pickle.load(fload)

    return es


def func_subdir_list_get(parent_dir_name):
    return list(filter(os.path.isdir,
                       map(lambda filename: os.path.join(parent_dir_name, filename),
                           os.listdir(parent_dir_name))))


def func_file_list_get(dirname, ext='.txt'):
    return list(filter(
        lambda filename: os.path.splitext(filename)[1] == ext,
        os.listdir(dirname)))


def func_get_runid_from_dirname(sim_run_dirname):
    # Find start index of run_id after "run" from the dirname "runxxx"
    start_index = sim_run_dirname.find("run") + 3
    run_id = int(sim_run_dirname[start_index:])

    return run_id


def func_cst_opt_res_para_save(project_folder, para_list_file_name, para_val_vec, para_name_list, run_id):

    # Convert ndarray to pandas series
    para_df = pd.DataFrame(data=para_val_vec.reshape(1, -1), index=[run_id], columns=para_name_list)

    # prepare the file to write
    full_para_list_file = os.path.join(project_folder, para_list_file_name)

    if 1 != run_id:
        write_mode = 'a'  # append if already exists
        header_mode = False
    else:
        write_mode = 'w'  # make a new file if not
        header_mode = True

    para_df.to_csv(full_para_list_file, mode=write_mode, header=header_mode)


def func_cst_opt_res_obj_save(project_folder, obj_val_file_name, obj_val_vec, obj_name_list, run_id):

    # Convert ndarray to pandas series
    obj_df = pd.DataFrame(data=obj_val_vec.reshape(1, -1), index=[run_id], columns=obj_name_list)

    # prepare the file to write
    full_obj_val_file = os.path.join(project_folder, obj_val_file_name)

    if 1 != run_id:
        write_mode = 'a'  # append if already exists
        header_mode = False
    else:
        write_mode = 'w'  # make a new file if not
        header_mode = True

    obj_df.to_csv(full_obj_val_file, mode=write_mode, header=header_mode)


def func_para_name_conv(line):

    val_str_in_line = line.split("=")[1].rstrip('\n')
    if '1' == val_str_in_line:
        val_str_in_name = '10'
    elif '0' == val_str_in_line:
        val_str_in_name = '00'
    else:
        val_str_in_name = val_str_in_line.replace('.', '')

    return val_str_in_name


def func_para_sweep_subdir_rename(exp_data_dir, para_file_name, search_str_lst, new_subdir_name_pattern):

    # Get subdir list
    subdir_lst = func_subdir_list_get(exp_data_dir)

    # Rename all subdir in the loop
    for subdir in subdir_lst:
        # Initialize the value string list in new subdir name for each subdir, because we will use append() later
        val_str_in_name_lst = []

        # Get the full path to the parameter file generated by CST
        para_file_fullpath = os.path.join(subdir, para_file_name)

        # Find strings in the search list in order
        for search_str in search_str_lst:
            with open(para_file_fullpath, 'r') as fread:
                for line in fread:  # Search search_str in the parameter file
                    if (search_str + '=') in line:  # Make sure the string we search is at the beginning of the line
                        val_str_in_name = func_para_name_conv(line)
                        val_str_in_name_lst.append(val_str_in_name)
                        break

        # Rename current subdir
        new_dir_name = new_subdir_name_pattern % tuple(val_str_in_name_lst)
        parent_dir = os.path.dirname(subdir)
        new_dir_path = os.path.join(parent_dir, new_dir_name)
        os.rename(subdir, new_dir_path)