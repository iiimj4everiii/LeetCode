class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:

        # Strategy:
        # We will use Depth-First-Search + memoization to find all
        # the courses can terminate. We do this by trying to find
        # any circular dependencies in a course and its prerequisites.

        # A method to do depth-first-search to recursively find if
        # we can finish prerequisites.
        def get_canFinish(course, course_path, prereq_dict):

            # Termination condition: if course does not have any
            # prerequisites, then we know course can be finished.
            if course not in prereq_dict.keys():
                return True

            # Get the prerequisites of course.
            prereqs = prereq_dict[course]

            # For each prerequisite p, we check to see if there is
            # a cycle.
            for p in prereqs:

                # If there is a cycle, then we already seen p in
                # course_path before. Return False as there is no
                # way to take a course in a prerequisite cycle.
                if p in course_path:
                    return False

                # Otherwise, add prerequisite p to course_path and
                # call get_canFinish() method to recursively find if
                # we can finish all the p's prerequisites.
                course_path.add(p)
                if not get_canFinish(p, course_path, prereq_dict):
                    return False

                # If we can finish p and its' prerequisites, see if
                # course's other prerequisites can finish as well.
                # We need to remove the current prerequisite p before
                # trying the rest of p's
                course_path.remove(p)

            # At this point, all the prerequisites of course can finish.
            # Therefore, course can finish as well. We remove course
            # from prereq_dict to signify that course can finish.
            prereq_dict.pop(course)

            return True

        # Generate a course list and convert it to a set.
        courses = set([x for x in range(numCourses)])

        # Initialize prereq_dict to an empty list. This will hold a list
        # of prerequisites of a course as a value mapped to course number.
        prereq_dict = {}

        # Convert prerequisites list to prereq_dict.
        for p in prerequisites:
            if len(p) == 0:
                break

            if p[0] not in courses:
                continue

            if p[0] in prereq_dict.keys():
                prereq_dict[p[0]].append(p[1])
            else:
                prereq_dict[p[0]] = [p[1]]

        # Initialize course_path to an empty set. This will hold a chain
        # of prerequisites for a course. We will follow the course
        # prerequisites to see if there is a circular dependency in these
        # course prerequisites (If we come across a prerequisite that is
        # already in course path).
        course_path = set()

        # Check to see if all the courses can finish.
        for c in courses:
            course_path.add(c)
            if not get_canFinish(c, course_path, prereq_dict):
                return False
            course_path.remove(c)

        return True


pr = [[]]
sol = Solution().canFinish(1, pr)
print(sol)
