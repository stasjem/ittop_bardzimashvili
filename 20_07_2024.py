
def flatten(lst, depth=None):

    def flatten_once(l):
        result = []
        for item in l:
            if isinstance(item, list):
                result.extend(item)
            else:
                result.append(item)
        return result

    if depth is None:

        while any(isinstance(item, list) for item in lst):
            lst = flatten_once(lst)
        return lst
    else:

        for _ in range(depth):
            if not any(isinstance(item, list) for item in lst):
                break
            lst = flatten_once(lst)
        return lst


nested_list = [1, [2, [3, [4, 5], 6], 7], 8]
print(flatten(nested_list))
print(flatten(nested_list, 1))
print(flatten(nested_list, 2))
print(flatten(nested_list, 3))
