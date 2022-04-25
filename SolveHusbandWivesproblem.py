
#Using breadth_first_tree_search for my search algorithm

from collections import deque
import sys


class JealousHusbands(object):
    def __init__(self, wives, husbands, boat):
        self.wives = wives
        self.husbands = husbands
        self.boat = boat

    def validCheck(self,i,j):
        
        if self.wives < 0 or self.husbands < 0 or self.wives > 3 or self.husbands > 3 or self.boat != 0 and self.boat != 1:
            return False   # just making sure theres no negative numbers or over 3 husbands/wives
        if self.husbands > self.wives and self.wives > 0:    
            return False # checks to make sure that there aren't more husbands than wives somewhere
        if self.husbands < self.wives and self.wives < 3:  
            return False
        if i+j >0 and i+j <3:
            return True
  
    def successors(self): #actions are the same as the successor
        if self.boat == 0:
            shore = 1
        else:
            shore = -1
        for i in range(3):
            for j in range(3):
                action = JealousHusbands(self.wives+shore*i, self.husbands+shore*j, self.boat+shore*1)
                if action.validCheck(i,j):    # valid check to make sure nothing to crazy is happening
                        yield action


            


    def goal_test(self): #GOAL TESTS to make sure the starting shore has no one left on it
        return self.husbands == 0 and self.wives == 0 and self.boat == 0

    def __repr__(self):
        return "(%d :wives, %d :husbands, %d :boat)\n" % (self.wives, self.husbands, self.boat)


class Node(object):  

    def __init__(self,state ,parent= None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self): #child node
        for action in self.state.successors():
            next_node = Node(parent=self,state=action,action=action)
            yield next_node


    def solution(self):
        #Return the sequence of actions to go from the root to this node.
        return [node.action for node in self.path()[1:]]

    def path(self):
        #Return a list of nodes forming the path from the root to this node.
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


def breadth_first_tree_search(initial_state): #search algorithm being used is breadth_first_tree_search 

  frontier = deque([Node(initial_state)])
  while frontier:
      node = frontier.popleft()
      if node.state.goal_test():
        return node
      frontier.extend(node.child_node())
  return None
 
def main():
  initial_state = JealousHusbands(3,3,1)
  node = breadth_first_tree_search(initial_state)
  solution= node.solution()

  if solution is None:
    print ("No Solution")
  else:
     print("Using breadth_first_tree_search\nThis shows the starting coast's progress\nWhatever isn't on this coast is on the other coast\n") 
     print("Also the right most column stands for which side the boat is on so 1 is starting side and 0 is opposite\n\n Start is 3 wives 3 husbands 1 boat\n")
     print ("%s" % solution )
     print("0 wives 0 husbands 0 boats means they've all reached the opposite shore.")


if __name__ == "__main__":
  main()