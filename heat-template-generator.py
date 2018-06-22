import argparse
parser = argparse.ArgumentParser(description="parse inputs")
# the format is gonna be "tensorflow numpy torch  "
parser.add_argument('packages',type = str,help="the packages you want to install")
# the format is gonna be "m1.small,m1.small,m2.small"
parser.add_argument('instances',type= str,help="the instances you want to initialze")
parser.add_argument('key_pair',type = str,help="the key pair you want to use(normally it's your private and public key pair)")
#  one consideration: what if one line has an exception??
def appendastring(script,toappend,indentlevel):
    return script+'\n'+".".join([" "]*indentlevel)+toappend

def generate(pack,instance,indent_level,instancename,keyname):
    script = appendastring("","",indent_level)
    script = appendastring(script,"resources:",indent_level)
    script = appendastring(script,instancename+":",indent_level+2)
    script = appendastring(script, "type: OS::Nova::Server",indent_level+4)
    script = appendastring(script, "properties:",indent_level+4)
    script = appendastring(script,"key_name: "+keyname,indent_level+6)
    script = appendastring(script,"flavor "+instance,indent_level+6)
    script = appendastring(script,"user_data: |",indent_level+6)

    commandindent = indent_level+8
    script = appendastring(script,"apt-get update",commandindent)
    script = appendastring(script,"apt-get install -y python3-pip",commandindent)
    script = appendastring(script,"apt-get install -y python3-dev",commandindent)
    script = appendastring(script,"apt-get install -y golang",commandindent)
    packages = pack.split(" ")
    # these libs will be installed no matter what, some basic libraries
    script = appendastring(script,"pip3 install scipy",commandindent)
    script = appendastring(script,"pip3 install numpy",commandindent)
    script = appendastring(script,"pip3 install pandas",commandindent)
    script = appendastring(script,"pip3 install matplotlib",commandindent)
    script = appendastring(script,"pip3 install Cython",commandindent)
    # these libraries are ml libraries, suppose the user doesn't know how to install ml libraries
    if "tensorflow" in packages:
        script = appendastring(script,"pip3 install tensorflow", commandindent)
    if "scikit-learn" in packages:
        script = appendastring(script,"pip3 install sklearn",commandindent)
    if "theano" in packages:
        script = appendastring(script,"pip3 install theano",commandindent)
    if "keras" in packages:
        script = appendastring(script,"pip3 install keras",commandindent)
    if "ray" in packages:
        script = appendastring(script,"pip3 install ray",commandindent)
    if "torch" in packages:
        script = appendastring(script,"pip3 install torch",commandindent)
    if "mxnet" in packages:
        script = appendastring(script,"pip3 install mxnet",commandindent)
    # cv libraries
    if "cv2" in packages:
        script = appendastring(script,"pip3 install opencv-python",commandindent)
    if "yolo" in packages or "darknetpy" in packages:
        script = appendastring(script,"pip3 install darknetpy",commandindent)
    #  nlp libraries
    if "word2vec" in packages:
        script = appendastring(script,"pip3 install word2vec",commandindent)
    if "ntlk" in packages:
        script = appendastring(script,"pip3 install ntlk",commandindent)
    return script