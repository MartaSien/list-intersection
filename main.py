import os

LISTS_DIR = os.path.join(os.getcwd(), "lists")

def main():
    lists = []
    for dir in os.listdir(LISTS_DIR):
        lists.append(combine_list(os.path.join(LISTS_DIR, dir)))
    intersection = get_intersection(lists)
    save_list(intersection)


def save_list(string_list):
    with open(os.path.join(os.getcwd(), "intersection_list.txt"), "w") as f:
        for i in string_list:
            f.write('\n'.join(str(i)))
        

def combine_list(dir):
    """
    Get a combined list based on directory path.
    """
    list = []
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            with open(os.path.join(dir, filename), 'r') as f:
                for line in f:
                    list.append(line.strip())
    return list


def get_intersection(lists):
    """
    Get an intersection based on a list of lists.
    """
    common_list = lists[0]
    for li in lists:
        common_list = list(set(common_list) & set(li))
    return common_list


if __name__=="__main__":
    main()