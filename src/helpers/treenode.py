class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        return (self.val == other.val) and (self.left == other.left)  and (self.right == other.right)

    def __str__(self) -> str:
        return f'TreeNode({self.val}, left={self.left}, right={self.right})'

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def _make_node(cls, arr: list, idx: int = 0):
        if idx >= len(arr):
            return None
        val = arr[idx]
        if val is None:
            return None
        return cls(
            val=val, 
            left=cls._make_node(arr, idx * 2 + 1), 
            right=cls._make_node(arr, idx * 2 + 2)
        )

    @classmethod
    def from_array(cls, arr: list):
        return cls._make_node(arr)