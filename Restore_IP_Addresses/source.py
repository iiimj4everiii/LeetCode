class Solution:
    def restoreIpAddresses(self, s: str) -> list:

        # Strategy:
        # We will use recursion to help us get all the valid IP addresses.
        # We will also use many termination conditions to help us determine whether or
        # not it will be worth the effort to recurse more. If we are able to get to the
        # final IP address field, test if the integer represented in the rest of s is a
        # valid IP address field value. If it is, we have terminated successfully. Append
        # the valid IP address to solution list and keep going.
        # For non-termination conditions (curr_field < 3), we look at the next 3 integers
        # of s:
        # 1) s[curr_idx:curr_idx+1]
        # 2) s[curr_idx:curr_idx+2]
        # 3) s[curr_idx:curr_idx+3]
        # If any of these is an invalid field value, just return. Otherwise we append them
        # to our potential_IP list and recurse deeper with next curr_idx = idx and
        # curr_field = curr_field + 1.

        # Recursive function that gets the rest of the IP address fields.
        def get_IP_Addresses(s, solution, potential_IP, curr_idx, curr_field, s_len):

            # If the string length for the rest of s is greater than 3 * field count, then
            # it is impossible to fit all the integers in s into all these fields. Just
            # return to the caller.
            if (s_len - curr_idx) > (4 - curr_field) * 3:
                return

            # On the other hand, if the string length for the rest of s is less than field
            # count, then we don't have enough integers to distribute into all the fields.
            # Just return to the caller.
            if (s_len - curr_idx) < (4 - curr_field):
                return

            # If we are at the last field of the IP address, see if the integer in the last
            # field is less than or equal to 255. We don't have to check the lower bound
            # because we know that there is at least 1 non-negative integer left in s.
            if curr_field == 3:

                sub_str = s[curr_idx:s_len]

                # '0z' is an invalid field value, where z is any non-negative integer value.
                if len(sub_str) > 1 and sub_str[0] == '0':
                    return

                # This is a successful termination condition. Convert potential_IP to IP
                # address format in string and append it to solution.
                if int(sub_str) <= 255:
                    solution.append(potential_IP[0] + '.' + potential_IP[1] + '.' +
                                    potential_IP[2] + '.' + sub_str)

                return

            # For every other IP address fields, we look at the next 3 integers:
            # 1) s[curr_idx:curr_idx+1]
            # 2) s[curr_idx:curr_idx+2]
            # 3) s[curr_idx:curr_idx+3]
            idx = curr_idx+1
            while True:

                # If the stop index idx is greater than the length of s, then we
                # are already done with all we can.
                if idx > s_len:
                    return

                # Extract the substring
                sub_str = s[curr_idx:idx]

                # Convert to integer and see if int(sub_str) is not a valid IP address
                # field value (> 255). If it is an invalid field value, just return.
                sub_str_int = int(sub_str)
                if sub_str_int > 255:
                    return

                # Otherwise, append sub_str to our potential IP address.
                potential_IP.append(sub_str)

                # Get the rest of the IP address if possible.
                get_IP_Addresses(s, solution, potential_IP, idx, curr_field+1, s_len)

                # Pop the last sub_str from potential_IP and try a new sub_str with one
                # more digit.
                potential_IP.pop(-1)
                idx += 1

                # Special case: sub_str is 0. If sub_str is 0, we will return right after
                # trying it out. This is because '0' is a valid field value. However, '0z'
                # are not valid, where z is any non-negative integer value.
                if sub_str_int == 0:
                    return

        # Initialize solution to an empty list.
        solution = []

        # Get all the valid addresses and put them in solution.
        get_IP_Addresses(s, solution, [], 0, 0, len(s))

        return solution


string = "101023"
sol = Solution().restoreIpAddresses(string)
print(sol)
