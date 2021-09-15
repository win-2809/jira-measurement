import apis

# Get all issue with 100 issues per API call
def getApiPagination(username, token, domain, projectKey):
    issueList = apis.getJiraIssue(username, token, domain, projectKey, 0)
    startAt = issueList["startAt"]
    totalIssue = issueList["total"]

    while (totalIssue > 100) and (startAt < totalIssue):
        startAt += 100
        nextIssueList = apis.getJiraIssue(startAt)
        issueList["issues"].extend(nextIssueList["issues"])

    print("getApiPagination successfully!!!")
    
    return issueList

# Replace None with Empty Dictionary
def replace_none(dictionary):
    # checking for dictionary and replacing if None
    if isinstance(dictionary, dict):
        
        for key in dictionary:
            if dictionary[key] is None:
                dictionary[key] = {}
            else:
                replace_none(dictionary[key])
  
    # checking for list, and testing for each value
    elif isinstance(dictionary, list):
        for val in dictionary:
            replace_none(val)

class Hasher(dict):
    # https://stackoverflow.com/a/3405143/190597
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value