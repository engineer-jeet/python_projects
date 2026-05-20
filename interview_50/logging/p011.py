# You are given request IDs arriving in sequence.
# Return the length of the longest contiguous sequence containing no repeated request IDs.

requests = [
"a1",
"b2",
"c3",
"a1",
"d4",
"e5"
]

def longest_unique_requests(requests):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(requests)):

        while requests[right] in seen:
            seen.remove(requests[left])
            left += 1

        seen.add(requests[right])

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length


print(longest_unique_requests(requests))