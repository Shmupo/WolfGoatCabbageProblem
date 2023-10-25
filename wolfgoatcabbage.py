# AI programming project 1

import search

#cannot be alone : G C or W G
class WolfGoatCabbage(search.Problem):
    def __init__(self, initial=('F', 'G', 'W', 'C'), goal=()):
        super().__init__(initial, goal)

    #True if state is goal state
    def goal_test(self, final):
        return final == self.goal

    #return new state after given action
    def result(self, state, action):
        state_list = []
        for elem in state:
            state_list.append(elem)
        if 'F' in state:
            for elem in action:
                state_list.remove(elem)
        else:
            for elem in action:
                state_list.append(elem)
        return tuple(state_list)

    #returns list of valid acions given state
    def actions(self, state):
        actions = []
        state = sorted(state)
        # C F G W
        
        if state == ['C', 'F', 'G', 'W']:
            actions.append({'F', 'G'})

        if state == ['C', 'W']:
            actions.append({'F'})
            actions.append({'F', 'G'})

        if state == ['C', 'F', 'W']:
            actions.append({'F', 'W'})
            actions.append({'F', 'C'})
            actions.append({'F'})

        if state == ['C']:
            actions.append({'F', 'G'})
            actions.append({'F', 'W'})

        if state == ['F', 'G', 'W']:
            actions.append({'F', 'G'})
            actions.append({'F', 'W'})

        if state == ['C', 'F', 'G']:
            actions.append({'F', 'G'})
            actions.append({'F', 'C'})

        if state == ['G']:
            actions.append({'F'})
            actions.append({'F', 'W'})
            actions.append({'F', 'G'})

        if state == ['F', 'G']:
            actions.append({'F'})
            actions.append({'F', 'G'})
            
        return actions

def main():
    wgc = WolfGoatCabbage()
    solution = search.depth_first_graph_search(wgc).solution()
    print(solution)
    solution = search.breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == "__main__":
    main()