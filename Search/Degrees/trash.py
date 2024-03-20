# sourceNeighbors = neighbors_for_person(source)

    # # create nodes for neighbours
    # # their state will be person_id
    # # their parent will be (movie_id, person_id)
    # # action will be their collaborations
    # for neighbor in sourceNeighbors:
    #     node = Node(neighbor[1], Node(source, None, source), neighbors_for_person(neighbor[1]))
    #     frontier.add(node)

    # connector: Node
    # # check for target_id is in the frontier
    # # If target_id doesn't exist in the frontier, 
    # # expand the node and add it's item to the frontier
    # while frontier.frontier != []:
    #     pivotNode: Node = frontier.remove()
    #     if pivotNode.state[1] == target:
    #         connector = pivotNode
    #         break
    #     else:
    #         for neighbor in pivotNode.action:
    #             node = Node(neighbor[1], (neighbor[0], pivotNode.state), neighbors_for_person(neighbor[1]))
    #             frontier.add(node)