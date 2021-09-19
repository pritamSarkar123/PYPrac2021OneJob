# https://www.youtube.com/watch?v=zoE9v3wrE_k&t=606s
def function(num_list):
    num_list.sort(key=lambda x: x[0])
    count = 0
    end = float("-inf")
    for i in range(len(num_list)):
        if end < num_list[i][0]:
            end = num_list[i][1]
            count += 1
    return count


if __name__ == '__main__':
    num_list = [[5,6],[1,2],[2,3],[3,4],[2,5]]
    print(function(num_list))