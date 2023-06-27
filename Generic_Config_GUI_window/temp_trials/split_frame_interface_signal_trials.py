import tkinter as tk
import tkinter.messagebox as mbox
# from tkinter import Frame
import re

# Create the main window
root = tk.Tk()
root.title("Resizable Frames")
root.geometry("800x400")

glbl_ft_size = 8
GLOB_TEST=0


def create_x_span_frame(parent_frame, bord_w=0, relief = tk.GROOVE, test=GLOB_TEST, px=0, empty=0, ht=5):
        if empty == 1:
            if test == 1:
                fr = tk.Frame(parent_frame, height=ht, borderwidth=bord_w, relief=relief, padx=px, highlightbackground="red", highlightthickness=2)
                fr.pack(side=tk.TOP, fill="x")
            elif test == 0:
                fr = tk.Frame(parent_frame, height=ht, borderwidth=bord_w, relief=relief, padx=px)
                fr.pack(side=tk.TOP, fill="x")
        else:
            if test == 1:
                fr = tk.Frame(parent_frame, borderwidth=bord_w, relief=relief, padx=px, highlightbackground="red", highlightthickness=2)
                fr.pack(side=tk.TOP, fill="x")
            elif test == 0:
                fr = tk.Frame(parent_frame, borderwidth=bord_w, relief=relief, padx=px)
                fr.pack(side=tk.TOP, fill="x")

        return fr

def create_space_frame(parent_frame, height=10):
        space_fr = create_x_span_frame(parent_frame=parent_frame, empty=1, ht=height)
        return space_fr

def create_listbox(parent_frame):

    # Create a vertical Scrollbar
    v_scrollbar = tk.Scrollbar(parent_frame, orient=tk.VERTICAL)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a horizontal Scrollbar
    h_scrollbar = tk.Scrollbar(parent_frame, orient=tk.HORIZONTAL)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Create a Listbox with fixed dimensions
    listbox = tk.Listbox(parent_frame, yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set, selectmode=tk.MULTIPLE, height=15, width=45)
    listbox.pack(side=tk.LEFT)

    # Function to deselect all selections in the Listbox
    def deselect_all(event):
        # Deselect all selections in the Listbox
        listbox.selection_clear(0, tk.END)

    # Bind the Escape key to the deselect_all function
    listbox.bind('<Escape>', deselect_all)

    # Attach the Scrollbar to the Listbox
    v_scrollbar.config(command=listbox.yview)
    h_scrollbar.config(command=listbox.xview)

    return listbox

def populate_listbox(listbox, populate_list):
     for i in populate_list:
          listbox.insert(tk.END, i)

curr_selected_vals = []

module_portlist_1 = ["a_very_very_very_long_ass_module_port_0", "a_very_very_very_long_ass_module_port_1", "a_very_very_very_long_ass_module_port_2", "a_very_very_very_long_ass_module_port_3", "a_very_very_very_long_ass_module_port_4", "a_very_very_very_long_ass_module_port_5", "a_very_very_very_long_ass_module_port_6", "a_very_very_very_long_ass_module_port_7", "a_very_very_very_long_ass_module_port_8", "a_very_very_very_long_ass_module_port_9", "a_very_very_very_long_ass_module_port_10", "a_very_very_very_long_ass_module_port_11", "a_very_very_very_long_ass_module_port_12", "a_very_very_very_long_ass_module_port_13", "a_very_very_very_long_ass_module_port_14", "a_very_very_very_long_ass_module_port_15", "a_very_very_very_long_ass_module_port_16", "a_very_very_very_long_ass_module_port_17", "a_very_very_very_long_ass_module_port_18", "a_very_very_very_long_ass_module_port_19", "a_very_very_very_long_ass_module_port_20", "a_very_very_very_long_ass_module_port_21", "a_very_very_very_long_ass_module_port_22", "a_very_very_very_long_ass_module_port_23", "a_very_very_very_long_ass_module_port_24", "a_very_very_very_long_ass_module_port_25", "a_very_very_very_long_ass_module_port_26", "a_very_very_very_long_ass_module_port_27", "a_very_very_very_long_ass_module_port_28", "a_very_very_very_long_ass_module_port_29"]

# main frame
main_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=2, width=20)
main_frame.pack(side=tk.LEFT, fill="x", expand=True)

# Create the first frame (left side)
l_frame = tk.Frame(main_frame, highlightbackground="grey", highlightthickness=2, width=20)
l_frame.pack(side=tk.LEFT, fill="both")

# Create the second frame (right side)
r_frame = tk.Frame(main_frame, highlightbackground="grey", highlightthickness=2)
r_frame.pack(side=tk.RIGHT, fill="both", expand=True)

#-------------------------------------------------------------------------------------------------------------------------------------------------
l_msg_frame = create_x_span_frame(l_frame)
l_space_frame0 = create_space_frame(l_frame)
l_content_frame = create_x_span_frame(l_frame)
l_space_frame1 = create_space_frame(l_frame)
l_space_frame2 = create_space_frame(l_frame)
l_btn_frame = create_x_span_frame(l_frame)

r_msg_frame = create_x_span_frame(r_frame)
r_space_frame0 = create_space_frame(r_frame)
r_content_frame = create_x_span_frame(r_frame)
r_space_frame1 = create_space_frame(r_frame)
r_btn_frame = create_x_span_frame(r_frame)

l_list_frame = tk.Frame(l_content_frame, height=5, borderwidth=0, relief=tk.GROOVE, padx=20)
l_list_frame.pack(side=tk.TOP, fill="x")

l_options_frame = create_x_span_frame(l_content_frame)
enter_ifname_lbl = tk.Label(l_options_frame, text=f"  Specify Interface Name : ", font=("Helvetica", glbl_ft_size), pady=2).pack(side=tk.LEFT)
ifname_entry_var = tk.StringVar()
ifname_entry =  tk.Entry(l_options_frame, textvariable=ifname_entry_var, width=30)
ifname_entry.pack(side=tk.LEFT)


port_listbox = create_listbox(l_list_frame)
populate_listbox(port_listbox, module_portlist_1)

curr_ports_list = [] # Holds the current ports list indexes
ifname = ""

def err_dialog(msg):
     msg_box = mbox.showinfo(title="Error", message=f"{msg}")

def is_valid_module_string(input_string):
    # Regular expression pattern
    # ^         : Start of the string
    # [a-zA-Z_] : Must start with an alphabet or '_'
    # \w*       : Followed by any number of word characters (alphanumeric characters plus '_')
    # $         : End of the string
    pattern = r'^[a-zA-Z_]\w*$'
    
    # Match the input string with the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False

def ports_and_ifname_sanity_check(ports_list, ifname):
     if len(ports_list) == 0:
          err_dialog(f"No signals selected for Interface Generation.")
          return 1
     elif ifname == """""":
          err_dialog(f"No Interface Name specified.")
          return 1
     elif is_valid_module_string(ifname) == False:
          err_dialog(f"Invalid Interface name \'{ifname}\'. Interface name must be as per IEEE Verilog/System Verilog norms.")
          return 1
     else:
        return 0

def get_selected_ports_and_ifname():
    curr_selected_vals = port_listbox.curselection()
    # Clear current contents of the list
    curr_ports_list.clear()
    for i in curr_selected_vals:
        curr_ports_list.append(module_portlist_1[i])

    ifname = ifname_entry_var.get()
    ports_and_ifname_sanity_check(curr_ports_list, ifname)
    print(curr_ports_list, ifname)
    
def clear_all():
     ifname_entry.delete(0, tk.END)
     port_listbox.selection_clear(0, tk.END)

lbl1 = tk.Label(l_msg_frame, text=f"Below is list if ports parsed.\nSelect ports you wish to create an Interface of.", font=("Helvetica", glbl_ft_size), pady=2, width=40) .pack(side=tk.TOP)
lbl2 = tk.Label(r_msg_frame, text=f"List of Interfaces created.", font=("Helvetica", glbl_ft_size, 'bold underline'), pady=2) .pack(side=tk.TOP)

create_if_btn = tk.Button(l_btn_frame, text=f"Create Interface\nfrom selected Signals",font=("Helvetica", glbl_ft_size), command=get_selected_ports_and_ifname, width=20, padx=10).pack(side=tk.LEFT)
clear_if_btn = tk.Button(l_btn_frame, text=f"Clear All\nSignals + Name",font=("Helvetica", glbl_ft_size), command=clear_all, width=20, padx=10).pack(side=tk.RIGHT)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Start the Tkinter event loop
root.mainloop()
