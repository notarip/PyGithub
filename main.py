#!/usr/bin/python

from github import Github


def print_result(issues):

    f = open('issues.html', 'w')
    message = """<html><head>
                <title>Issues de Via Pais</title>
                </head>
                <body>
                <h2>Issues de Via Pais</h2>"""
    message += "<ul>"

    for issue in issues:
        message += "<li> %s | %s </li>" % (issue.title.encode("latin1"),
                                           [label.name.encode("latin1") for label in issue.get_labels()
                                            if "status" in label.name])

    message += "</ul></body></html>"

    print message
    f.write(message)
    f.close()

user = "user"
password = "pass"
repo = "viapais"

# First create a Github instance:
g = Github(user, password)

user = g.get_user()

for org in user.get_orgs():
    print org
    repo = org.get_repo(repo)
    print_result(repo.get_issues())

