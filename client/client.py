#need an interpreter line for your system
def construct_file():
    pass




helpline="""
Commands:
start [n_nodes] - create a new circuit 
(when started)
add [node1] [node2] [type] [value] - add a new component
remove [index] - remove the indexed components(from 0)
list - show all components
save - save the net to a file
solve - solve the net
load [filepath] - load the net from file (overwriting the current work)
"""
if __name__=="__main__":
    print("NetPep>")
