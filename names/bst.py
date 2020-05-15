class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # Go left
            left_result = self.left and self.left.contains(target)
            return left_result
        else:
            # Go right
            right_result = self.right and self.right.contains(target)
            return right_result