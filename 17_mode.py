def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    greatest_freq = 0
    greatest_num = 0
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > greatest_freq:
            greatest_freq = freq[num]
            greatest_num = num

    return greatest_num 
