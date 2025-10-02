class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def checkName(name):
            s = ""
            for i in name:
                if i =="+":
                    return s
                elif i ==".":
                    continue
                else:
                    s += i
            return s

        ans = set()
        for email in emails:
            name , domain = email.split("@")
            name = checkName(name)
            ans.add(name+"@"+domain)
        return len(ans)
            

        