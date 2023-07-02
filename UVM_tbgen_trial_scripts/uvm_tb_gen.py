import os
from datetime import date

#-------------------------------------------------------------
GLOB_block_name = "dsp"
GLOB_top_module_name = "dsp_top_DUT"
GLOB_top_tb_name = "dsp_top_tb"
# GLOB_output_dir = "C:/uvm_tbgen_file_handling_block"
GLOB_output_dir = "C:/Users/jayantya/OneDrive - Advanced Micro Devices Inc\Documents/GitHub/Python_Tkinter_tutorial_repository/UVM_tbgen_trial_scripts"
GLOB_owners_name = "jayantya"

GLOB_top_parsed_port_list = [{'PORT_CONFIG_LIST': ['input', '', 'dfx_rst_n'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['i', '', 'sys_reset_n'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['i', '[CSSD_NUM_TRGRS-1:0]', 'cssd_trig_n'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['i', '', 'cdc_trig_in'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['i', '[DFX_NUM_CLOCKS-1:0]', 'root_clk_in'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['I', '', 'clk_observe_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['I', '2', 'clock_dr'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['I', '3', 'reset_tap_b'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['I', '4', 'shift_dr'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['I', '10', 'capture_dr'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['I', 'PARAM_1', 'update_dr'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['input', '', 'select_dr'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['input', '[TOT_SCAN_NUM_CHNL-1:0]', 'scan_chnl_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '[TOT_SCAN_NUM_CHNL-1:0]', 'scan_chnl_mask_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_mask_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '[TOT_SCAN_NUM_CHAINS-1:0]', 'scan_data_out_int'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '', 'scan_en_n_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['INPUT', '', 'scan_clk_n_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['INPUT', '', 'scan_mode_rst_n_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['INPUT', 'PARAM_N', 'scan_edt_updt_n_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['input', 'PARAM_N', 'ijtag_tdi_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['input', 'PARAM_N', 'ijtag_tdi_return_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['input', '', 'scan_clear_clk'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['input', '[MEMCLR_WIDTH-1:0]', 'dfx0_mem_clear_pass_in_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['input', '[MEMCLR_WIDTH-1:0]', 'dfx0_mem_clear_trigger'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['o', '', 'dfx0_scan_clear_done_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['o', '', 'dfx0_scan_clear_pass_out_ex'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['o', '[DFX_NUM_CLOCKS-1:0]', 'clk_root_int'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['o', '', 'ijtag_tdo_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['O', '', 'ijtag_tdo_return_ext'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['O', '', 'scan_en'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['O', '', 'scan_mode'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '', 'scan_rst_byp'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '', 'scan_lat_byp_en', '33'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT', 'UNPACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['output', '', 'scan_mode_rst_n', 'PARAM_P'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT', 'UNPACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['output', '', 'scan_ram_byp', '[13:0]'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT', 'UNPACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['OUTPUT', '', 'scan_mode_stuckat'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['OUTPUT', '', 'scan_en_stuckat'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['OUTPUT', '', 'scan_clkgate_en'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '[TOT_SCAN_NUM_CHNL-1:0]', 'scan_chnl_out_ext', ''], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_out_ext', ''], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '[TOT_SCAN_NUM_CHAINS-1:0]', 'scan_data_in_int'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC'}}, {'PORT_CONFIG_LIST': ['inout', '', 'io_1'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['INOUT', '', 'io_12'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['io', '', 'io_2'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['IO', '', 'io_3'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_out_ext1', ''], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'SINGLE_BIT'}}, {'PORT_CONFIG_LIST': ['output', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_out_ext2', '4'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'INTEGRAL'}}, {'PORT_CONFIG_LIST': ['output', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_out_ext3', 'RND_PARAM'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'PARAMETRIC'}}, {'PORT_CONFIG_LIST': ['output', '[SCAN_NUM_ODCC_CH-1:0]', 'scan_odcc_chnl_out_ext4', '[14:0]'], 'PORT_DIMENSIONS_INFO': {'PACKED_DIMENSION_INFO': 'SPECIFIC', 'UNPACKED_DIMENSION_INFO': 'SPECIFIC'}}]

GLOB_parsed_module_portlist = ['dfx_rst_n', 'sys_reset_n', 'cssd_trig_n', 'cdc_trig_in', 'root_clk_in', 'clk_observe_in_ext', 'clock_dr', 'reset_tap_b', 'shift_dr', 'capture_dr', 'update_dr', 'select_dr', 'scan_chnl_in_ext', 'scan_chnl_mask_in_ext', 'scan_odcc_chnl_in_ext', 'scan_odcc_chnl_mask_in_ext', 'scan_data_out_int', 'scan_en_n_ext', 'scan_clk_n_ext', 'scan_mode_rst_n_ext', 'scan_edt_updt_n_ext', 'ijtag_tdi_ext', 'ijtag_tdi_return_ext', 'scan_clear_clk', 'dfx0_mem_clear_pass_in_ext', 'dfx0_mem_clear_trigger', 'dfx0_scan_clear_done_ext', 'dfx0_scan_clear_pass_out_ex', 'clk_root_int', 'ijtag_tdo_ext', 'ijtag_tdo_return_ext', 'scan_en', 'scan_mode', 'scan_rst_byp', 'scan_lat_byp_en', 'scan_mode_rst_n', 'scan_ram_byp', 'scan_mode_stuckat', 'scan_en_stuckat', 'scan_clkgate_en', 'scan_chnl_out_ext', 'scan_odcc_chnl_out_ext', 'scan_data_in_int', 'io_1', 'io_12', 'io_2', 'io_3', 'scan_odcc_chnl_out_ext1', 'scan_odcc_chnl_out_ext2', 'scan_odcc_chnl_out_ext3', 'scan_odcc_chnl_out_ext4']

GLOB_added_interfaces = [{'IF_NAME': 'intf_0', 'IF_PORTS': (0, 1, 2), 'GEN_DRIVER': 1}, {'IF_NAME': 'intf_1', 'IF_PORTS': (3, 4, 5), 'GEN_DRIVER': 0}, {'IF_NAME': 'intf_2', 'IF_PORTS': (6, 7, 8), 'GEN_DRIVER': 1}, {'IF_NAME': 'intf_3', 'IF_PORTS': (9, 10, 11), 'GEN_DRIVER': 1}]

#-------------------------------------------------------------
GLOB_top_env_name = "dsp_env"
GLOB_top_base_test_name = "dsp_base_test"

# Directories
GLOB_BLK_tb_dir = ""
GLOB_BLK_top_dir = ""
GLOB_BLK_scripts_dir = ""
GLOB_BLK_filelists_dir = ""
GLOB_BLK_uvm_tbgen_dir = ""
GLOB_BLK_uvm_tbgen_xml_dir = ""

GLOB_TB_env_dir = ""
GLOB_TB_sequences_dir = ""
GLOB_TB_tests_dir = ""
GLOB_TB_coverage_dir = ""
GLOB_TB_assertions_dir = ""
GLOB_TB_ral_dir = ""
GLOB_TB_interfaces_dir = ""

# Files
GLOB_BLK_setup_filename = ""

#-------------------------------------------------------------

# Class to Handle Error Frame functions and other prompts
class TOP_APPLICATION_BASE():
    
    def __init__(self, root_frame) :
        self.rf = root_frame

# Common Functions of the entire Application
class COMMON_APLICATION_FUNCTIONS(TOP_APPLICATION_BASE):
    pass

# All functions related files and directory handling and related TB Files generation logic.
class ALL_FILEGEN_FUNCTIONS(COMMON_APLICATION_FUNCTIONS):

    # def to check if top directory to create is already present and build a directory into it
    def check_and_create_dir(self, output_dir, dir_name):
        dir_path=f"{output_dir.strip()}/{dir_name.strip()}"
        if os.path.isdir(dir_path):
            print(f"Directory {dir_name} already present in PATH : {output_dir}")
            return False, None
        else:
            # Create the directory
            try:
                os.makedirs(dir_path)
                print(f"Created directory {dir_name} at {output_dir}")
                return True, dir_path
            except OSError as error:
                print(f"Error creating directory '{dir_path}': {error}")
                return False, None
    
    # def to check if top directory to create is already present and build a directory into it
    def check_and_create_file(self, output_dir, file_name):
        file_path=f"{output_dir.strip()}/{file_name.strip()}"
        if os.path.isdir(file_path):
            print(f"File {file_name} already present in PATH : {output_dir}")
            return False, None
        else:
            # Create the File
            try:
                with open(file_path, 'w') as file:
                    print(f"Created File {file_name} at {output_dir}")
                    file.close() # Close file after creating
                    return True, file_path
            except IOError as error:
                print(f"Error creating fILE '{file_path}': {error}")
                return False, None

    # To create all inner directories
    def create_all_TB_directories(self,top_block_dir):
        # All top level directories
        self.check_and_create_dir(top_block_dir, "tb")
        self.check_and_create_dir(top_block_dir, "top")
        self.check_and_create_dir(top_block_dir, "scripts")
        self.check_and_create_dir(top_block_dir, "filelists")
        self.check_and_create_dir(top_block_dir, "UVM_tbgen_output_files")
        
        # Create all top level files
        self.check_and_create_file(top_block_dir, "README")
        self.check_and_create_file(top_block_dir, "Makefile")
        global GLOB_BLK_setup_filename
        GLOB_BLK_setup_filename = f"{GLOB_block_name}_setup.csh"
        self.check_and_create_file(top_block_dir, GLOB_BLK_setup_filename)

        global GLOB_BLK_tb_dir
        global GLOB_BLK_top_dir
        global GLOB_BLK_scripts_dir
        global GLOB_BLK_filelists_dir
        global GLOB_BLK_uvm_tbgen_dir
        global GLOB_BLK_uvm_tbgen_xml_dir

        GLOB_BLK_tb_dir = f"{top_block_dir}/tb"
        GLOB_BLK_top_dir = f"{top_block_dir}/top"
        GLOB_BLK_scripts_dir = f"{top_block_dir}/scripts"
        GLOB_BLK_filelists_dir = f"{top_block_dir}/filelists"
        GLOB_BLK_uvm_tbgen_dir = f"{top_block_dir}/UVM_tbgen_output_files"

        # Create the uvm_tbgen output logfile
        self.check_and_create_file(GLOB_BLK_uvm_tbgen_dir, "UVM_tbgen_logfile.log")
        # Create the directory for output XML files
        self.check_and_create_dir(GLOB_BLK_uvm_tbgen_dir, "xml")
        GLOB_BLK_uvm_tbgen_xml_dir = f"{top_block_dir}/UVM_tbgen_output_files/"

        # Create the TOP TB FILE
        top_tb_filename = f"{GLOB_top_tb_name}.sv"
        self.check_and_create_file(GLOB_BLK_top_dir, top_tb_filename)
        # Create the DUT and TB Filelist files
        dut_filelist_filename = "design_filelist.f"
        tb_filelist_filename = "testbench_filelist.f"
        self.check_and_create_file(GLOB_BLK_filelists_dir, dut_filelist_filename)
        self.check_and_create_file(GLOB_BLK_filelists_dir, tb_filelist_filename)

        global GLOB_TB_env_dir
        global GLOB_TB_sequences_dir
        global GLOB_TB_tests_dir
        global GLOB_TB_coverage_dir
        global GLOB_TB_assertions_dir
        global GLOB_TB_ral_dir
        global GLOB_TB_interfaces_dir
        
        # Create the TB directories
        tb_dir = f"{top_block_dir}/tb"
        self.check_and_create_dir(tb_dir, "env")
        self.check_and_create_dir(tb_dir, "sequences")
        self.check_and_create_dir(tb_dir, "tests")
        self.check_and_create_dir(tb_dir, "coverage")
        self.check_and_create_dir(tb_dir, "assertions")
        self.check_and_create_dir(tb_dir, "ral")
        self.check_and_create_dir(tb_dir, "interfaces")

        # Set all global variables to created directories
        GLOB_TB_env_dir = f"{tb_dir}/env"
        GLOB_TB_sequences_dir = f"{tb_dir}/sequences"
        GLOB_TB_tests_dir = f"{tb_dir}/tests"
        GLOB_TB_coverage_dir = f"{tb_dir}/coverage"
        GLOB_TB_assertions_dir = f"{tb_dir}/assertions"
        GLOB_TB_ral_dir = f"{tb_dir}/ral"
        GLOB_TB_interfaces_dir = f"{tb_dir}/interfaces"

        # Create the TOP env file
        top_env_filename = f"{GLOB_top_env_name}.sv"
        self.check_and_create_file(GLOB_TB_env_dir, top_env_filename)
        
    # To create the top project CSH file
    def generate_proj_setup_csh_file(self, file_path):
        f = open(file_path, 'w')

        f.write(f"#---------------------------------------------------------------------" + "\n")
        f.write(f"#                    Project Setup File for : {GLOB_block_name}" + "\n")
        f.write(f"#---------------------------------------------------------------------" + "\n")
        f.write(f"" + "\n")
        f.write(f"# Add commands here to load tools and utilities" + "\n")
        f.write(f"" + "\n")
        f.write(f"# Project related Env Variables and utility aliases" + "\n")
        f.write(f"setenv PROJ_WORKSPACE \"$PWD\"" + "\n")
        f.write(f"setenv proj_workspace \"$PWD\"" + "\n")
        f.write(f"" + "\n")
        # f.write(f"setenv  \"${{PROK_WORKSPACE}}\"" + "\n")
        f.write(f"setenv SCRIPTS_DIR  \"${{PROJ_WORKSPACE}}\"/scripts" + "\n")
        f.write(f"setenv PROJ_TOP_DIR \"${{PROJ_WORKSPACE}}\"/top" + "\n")
        f.write(f"setenv PROJ_TB_DIR  \"${{PROJ_WORKSPACE}}\"/tb" + "\n")
        f.write(f"" + "\n")
        f.write(f"" + "\n")
        f.write(f"" + "\n")

        f.close()

    # Function to dump top boiler plate code to source code files
    def dump_top_boiler_plate_to_file(self, file, file_desc=None, line_comment_char="//"):
        
        file.write(f"{line_comment_char}--------------------------------------------------------------------------------------------------------------" + "\n")
        file.write(f"{line_comment_char} Author       : {GLOB_owners_name}" + "\n")
        file.write(f"{line_comment_char} Date Created : {date.today()}" + "\n")
        file.write(f"{line_comment_char} Version      : " + "\n")
        file.write(f"{line_comment_char} Desctiption  : {file_desc}" + "\n")
        file.write(f"{line_comment_char}--------------------------------------------------------------------------------------------------------------" + "\n")
        file.write(f" " + "\n")
    
    # Update global parsed module portlist
    def update_global_top_parsed_portlist(self):
        global GLOB_top_parsed_port_list
        for var in GLOB_top_parsed_port_list:
            port_config_list = var['PORT_CONFIG_LIST']
            port_dimensions_info = var['PORT_DIMENSIONS_INFO']

            len_port_dimensions_info = len(port_dimensions_info)

            # Return final string for types specified in list
            def return_pkd_unpkd_str(val, typ):
                if typ == 'INTEGRAL':
                    int_val = int(val)
                    dim = int_val-1
                    final_str=f"[{dim}:0]"
                    return final_str
                if typ == 'SPECIFIC':
                    final_str = f"{val}"
                    return final_str
                if typ == 'PARAMETRIC':
                    final_str = f"[{val}-1:0]"
                    return final_str
                if typ == 'SINGLE_BIT':
                    final_str = f""
                    return final_str

            if len_port_dimensions_info == 1:
                packed_dimension_info = port_dimensions_info['PACKED_DIMENSION_INFO']
                var['PORT_CONFIG_LIST'][1] = return_pkd_unpkd_str(var['PORT_CONFIG_LIST'][1], packed_dimension_info)
            elif len_port_dimensions_info == 2:
                packed_dimension_info = port_dimensions_info['PACKED_DIMENSION_INFO']
                var['PORT_CONFIG_LIST'][1] = return_pkd_unpkd_str(var['PORT_CONFIG_LIST'][1], packed_dimension_info)
                unpacked_dimension_info = port_dimensions_info['UNPACKED_DIMENSION_INFO']
                var['PORT_CONFIG_LIST'][3] = return_pkd_unpkd_str(var['PORT_CONFIG_LIST'][3], unpacked_dimension_info)

    # Function to create all Interface files
    def generate_all_interface_files(self, 
                                     tb_interface_filedir, 
                                     top_parsed_portlist, 
                                     top_parsed_portname_portlist, 
                                     added_interfaces_info_list
                                    ):
        for intf in added_interfaces_info_list:
            intf_name = intf['IF_NAME']
            ports_idx = intf['IF_PORTS']

            interface_filename = f"{intf_name}.sv"
            interface_filepath = f"{tb_interface_filedir}/{interface_filename}"

            # Create the file and dump the boiler plate
            exit_c, fp = self.check_and_create_file(output_dir=tb_interface_filedir, file_name=interface_filename)

            if exit_c == True:
                print(f"dumping in :: {fp}")

                # this_interface_ports = [] # Create an empty list

                # Open file in write mode
                f = open(interface_filepath, 'w')
                self.dump_top_boiler_plate_to_file(file=f, file_desc=f"Source file for \'{intf_name}\' Interface")

                f.write(f"// Interface : {intf_name}" + "\n")
                f.write(f"interface {intf_name};" + "\n")
                f.write(f"" + "\n")
                f.write(f"// Interface Signals" + "\n")

                max_port_len = 0
                max_pack_len = 0
                max_unpack_len = 0

                # Initial loop to get ideas of lengths and spaces to beautify
                for var in ports_idx:
                    curr_port_info = top_parsed_portlist[var]
                    config_list = curr_port_info['PORT_CONFIG_LIST']
                    dimesnions_list = curr_port_info['PORT_DIMENSIONS_INFO']
                    dimesnions_list_size = len(dimesnions_list) # Size of the dimensions list (Has to be 1 or 2)

                    port_name = config_list[2]
                    len_port_name = len(port_name)
                    max_port_len = len_port_name if len_port_name >= max_port_len else max_port_len

                    if dimesnions_list_size == 1:
                        packed_dimensions = config_list[1]
                        len_packed_dimensions = len(packed_dimensions)
                        max_pack_len = len_packed_dimensions if len_packed_dimensions >= max_pack_len else max_pack_len
                    elif dimesnions_list_size == 2:
                        packed_dimensions = config_list[1]
                        len_packed_dimensions = len(packed_dimensions)
                        max_pack_len = len_packed_dimensions if len_packed_dimensions >= max_pack_len else max_pack_len

                        unpacked_dimensions = config_list[3]
                        len_unpacked_dimensions = len(unpacked_dimensions)
                        max_unpack_len = len_unpacked_dimensions if len_unpacked_dimensions >= max_unpack_len else max_unpack_len

                for var in ports_idx:
                    curr_port_info = top_parsed_portlist[var]
                    config_list = curr_port_info['PORT_CONFIG_LIST']
                    dimesnions_list = curr_port_info['PORT_DIMENSIONS_INFO']
                    dimesnions_list_size = len(dimesnions_list) # Size of the dimensions list (Has to be 1 or 2)

                    port_name = config_list[2]

                    if dimesnions_list_size == 1:
                        packed_dimensions = config_list[1]
                        packed_left_spaces = max_pack_len-len(packed_dimensions)
                        spaces=" "*packed_left_spaces
                        f.write(f"logic {packed_dimensions}{spaces} {port_name};" + "\n")
                    elif dimesnions_list_size == 2:
                        packed_dimensions = config_list[1]
                        packed_left_spaces = max_pack_len-len(packed_dimensions)
                        p_spaces=" "*packed_left_spaces

                        unpacked_dimensions = config_list[3]
                        f.write(f"logic {p_spaces}{packed_dimensions} {port_name} {unpacked_dimensions};" + "\n")

                f.write(f"" + "\n")
                f.write(f"// Clocking Blocks : Add here" + "\n")
                f.write(f"" + "\n")
                f.write(f"// Modports : Add Here" + "\n")
                f.write(f"" + "\n")
                f.write(f"endinterface : {intf_name}")
                f.close()

    # Top Function to Do All
    def DO_TOP(self,
               output_dir,
               block_namee
              ):
        # Update the parsed module ports list
        self.update_global_top_parsed_portlist()

        # Create the top directory
        op_dir_chk, TOP_BLOCK_DIR = self.check_and_create_dir(output_dir, GLOB_block_name)
        if op_dir_chk:
            # Create other directories
            self.create_all_TB_directories(TOP_BLOCK_DIR)

            # Create the top project setup file
            setup_file_path = f"{TOP_BLOCK_DIR}/{GLOB_BLK_setup_filename}"
            self.generate_proj_setup_csh_file(setup_file_path)

            # Create all interfaces
            self.generate_all_interface_files(GLOB_TB_interfaces_dir, GLOB_top_parsed_port_list, GLOB_parsed_module_portlist, GLOB_added_interfaces)
        else:
           print(f"ERROR :: Output Directory not Generated ..... Aborting !!...")

root = 1
ALL_FILEGEN_FUNCTIONS_ci = ALL_FILEGEN_FUNCTIONS(root_frame=root)
ALL_FILEGEN_FUNCTIONS_ci.DO_TOP(f"{GLOB_output_dir}","dsp")