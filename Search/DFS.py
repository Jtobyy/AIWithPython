class DFS():
    """Depth First Search"""

    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        
        else:
            # Get the last item in the list (which is the newest node added)
            # Node is the next item to explore
            node = self.frontier[-1]

            # Save all the items on the list besides the last node (i.e. removing the last node)
            self.frontier = self.frontier[0:-1]
            return node