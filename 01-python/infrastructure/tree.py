def draw_tree(numTrees=0, printAxis="horizontal"):
    """
    Draws a tree(s).

    Parameters:
        numTrees: integer value; the number of trees to draw
        printAxis: string value of "horizontal" or "vertical" (case insensitive); indicates whether to draw the tree(s)
            horizontally or vertically 

    Helper methods:
        draw_top_of_tree: draws the top (i.e. leaves) of the tree numTrees times
        draw_bottom_of_tree: draws the bottom (i.e. trunk) of the tree numTrees times

    """

    def draw_top_of_tree(numTrees):
        for _ in range(numTrees):
            print("  $$  ", end="")
        print()
        for _ in range(numTrees):
            print(" $$$$ ", end="")
        print()
        for _ in range(numTrees):
            print("  $$  ", end="")
        print()

    def draw_bottom_of_tree(numTrees):
        for _ in range(numTrees):
            print("  ||  ", end="")
        print()

    # Validation checks
    VALID_AXES = ["horizontal", "vertical"]
    
    if (numTrees < 0):
        raise ValueError("Number of trees is undefined.")
    elif (printAxis.lower() not in VALID_AXES):
        raise ValueError("Print axis is undefined.")
    elif (numTrees == 0):
        return
    else: # print some trees
        if (printAxis.lower() == "horizontal"):
            draw_top_of_tree(numTrees)
            draw_bottom_of_tree(numTrees)
        else:
            for _ in range(numTrees):
                draw_top_of_tree(1)
                draw_bottom_of_tree(1)
                print()

    print()

    return