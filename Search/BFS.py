class BFS():
    """Depth First Search"""

    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        
        else:
            # Get the oldest item on the list (which was the first one to be added)
            # Node is the next item to explore
            node = self.frontier[0]

            # Save all the items on the list besides the last node (i.e. removing the last node)
            self.frontier = self.frontier[1:]
            return node