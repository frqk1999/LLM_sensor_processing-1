import os, sys, csv, re, json

conv_root = r"conv_history\gpt-4o"
output_root = r"code"
fn_list = os.listdir(conv_root)
for fn in fn_list:
    conv_path = os.path.join(conv_root, fn)
    output_path = conv_path.replace(conv_root, output_root)
    conv = open(conv_path, "r")
    output = open(output_path, "w")
    # everytime read 1 line
    line = conv.readline()
    idx = 0
    while line:
        # ignore message from user
        if "'role': 'user'" in line or "'role': 'system'" in line or "{'role': 'assistant', 'content': 'I am ready.'}" in line:
            line = conv.readline()
            continue
        # find all code blocks start with ```Python and end with ```
        match = re.findall(r"```Python(.*?)```", line)
        # write all code blocks to output file
        output.write(f"### Index {idx} ###\n")
        for code in match:
            # replace all \n with actual new line
            code = code.replace("\\n", "\n")
            output.write(code.strip() + "\n\n")
        idx += 1
        line = conv.readline()
    conv.close()
    output.close()
    # change extension to .py
    os.rename(output_path, output_path.replace(".txt", ".py"))
