"""
Create OUT Null Node Below Selected Nodes

HOW TO SET UP AS A SHORTCUT IN HOUDINI:
1. Open Houdini
2. Go to Edit > Hotkeys (or press Alt+Shift+K)
3. Search for "New Tool" or go to the Shelf Tools section
4. Create a new shelf tool
5. In the Script tab, paste this Python code
6. Assign a hotkey (e.g., Ctrl+Shift+N)
7. Save and test by selecting a node and pressing your hotkey

WHAT THIS DOES:
- Creates a null node named "OUT" below each selected node
- Automatically connects it to the selected node's output
- Positions it exactly 1 unit below the selected node
- If "OUT" name exists, adds numbers (OUT1, OUT2, etc.)
"""

# Get selected nodes
nodes = hou.selectedNodes()

# Start undo group
with hou.undos.group("Make OUT null"):
    # Check that at least one node selected
    if len(nodes) > 0:

        # Make new node
        for n in nodes:
            oldPos = n.position()
            parent = n.parent()
            name = "OUT"
            i = 1
            # Check if the name "OUT" already exists, if so, add a number to make it unique
            while parent.node(name):
                name = "OUT" + str(i)
                i += 1
            newNode = parent.createNode("null")
            newNode.setPosition(hou.Vector2([oldPos[0], oldPos[1]-1]))
            newNode.setInput(0, n, 0)
            newNode.setName(name)
