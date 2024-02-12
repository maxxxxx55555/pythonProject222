class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(numbers):
    if not numbers:
        return None

    root = TreeNode(int(numbers[0]))
    queue = [root]
    i = 1

    while queue and i < len(numbers):
        node = queue.pop(0)

        if numbers[i] != '':
            node.left = TreeNode(int(numbers[i]))
            queue.append(node.left)
        i += 1

        if i < len(numbers) and numbers[i] != '':
            node.right = TreeNode(int(numbers[i]))
            queue.append(node.right)
        i += 1

    return root


def find_paths(root, target_sum):
    def dfs(node, current_sum, path):
        if not node:
            return

        current_sum += node.val
        path.append(node.val)

        if not node.left and not node.right:
            if current_sum == target_sum:
                paths.append(path[:])

        dfs(node.left, current_sum, path)
        dfs(node.right, current_sum, path)

        path.pop()

    paths = []
    dfs(root, 0, [])
    return paths


# Пример использования
input_str = input()
numbers = input_str.split(",")
root = build_tree(numbers)
target_sum = int(input())
result = find_paths(root, target_sum)
print("Пути с суммой {}: {}".format(target_sum, result))