class Solution:
    def numUniqueEmails(self, emails):
        """
        Runtime: 40 ms, faster than 98.10%
        Memory Usage: 14.5 MB, less than 29.08%
        """
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            if "+" in local:
                local = local[:local.index("+")].replace(".", "")
            else:
                local = local.replace(".", "")
            email_set.add((local, domain))
        return len(email_set)


if __name__=="__main__":
    # 2
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    # 3
    print(Solution().numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
    
