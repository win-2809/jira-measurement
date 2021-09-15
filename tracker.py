import pandas as pd
import numpy as np
import utils
import collections

def load_data(username, token, domain, projectKey):
    rawData = utils.getApiPagination(username, token, domain, projectKey)

    df = pd.DataFrame(columns=["id","key","summary","status","assignee","created","issuetype","priority","creator"])

    issueList = rawData.get("issues")

    for issue in issueList:
        utils.replace_none(issue)
        issueInfo = {
                        "id": issue.get("id"), 
                        "key": issue.get("key"),
                        "summary": issue.get("fields").get("summary", None),
                        "status": issue.get("fields").get("status", None).get("name", None),
                        "assignee": issue.get("fields").get("assignee", None).get("displayName", None),
                        "created": issue.get("fields").get("created", None),
                        "issuetype": issue.get("fields").get("issuetype", None).get("name", None),
                        "priority": issue.get("fields").get("priority", None).get("name", None),
                        "creator": issue.get("fields").get("creator", None).get("displayName", None)
                    }
        df = df.append(issueInfo, ignore_index=True)

    print(df.head(5))
    return df