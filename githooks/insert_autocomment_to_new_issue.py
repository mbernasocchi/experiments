# this listens to a github webhook of the type issue. 
# see https://developer.github.com/v3/activity/events/types/#issuesevent
# if the issue is opened, then the scripts issues an add comment API call
# see https://developer.github.com/v3/issues/comments/#create-a-comment


import web
import json
import requests
import urllib

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

USER = 'mbernasocchi'
PASSWORD = 'MYSUPERSECRETPASSW'
ISSUES_REPO = 'mbernasocchi/experiments'
PAYPAL_MERCHANT_ID = 'ZPQW7S4QSL9YY'

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        parse(data)

def generate_reference(data):
    issue_number = data['issue']['number']
    issue_title = data['issue']['title']
    
    reference = 'Fix issue %s: %s' % (issue_number, issue_title)
    reference = urllib.quote_plus(reference)
    return issue_number, reference
    
def generate_paypal_html(reference):
    template = 'Show us that this bug is very important to you by donating for its fix<br/><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=%s&lc=CH&item_name=test&item_number=%s&no_note=1&no_shipping=1&currency_code=CHF&bn=PP%%2dDonationsBF%%3abtn_donateCC_LG%%2egif%%3aNonHosted"><img src="https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif" name="submit" alt="PayPal - The safer, easier way to pay online." /></a>'
    
    html = template % (PAYPAL_MERCHANT_ID, reference)
    return html
    
def generate_response(issue_number, html):
    comment_payload = {
        'body': html,
    }

    comment_payload = json.dumps(comment_payload)
    
    comment_url = 'https://api.github.com/repos/%s/issues/%s/comments' % (ISSUES_REPO, issue_number)

    # auth using
    r = requests.post(
        comment_url, data=comment_payload, auth=(USER, PASSWORD))

    
def parse(data=None):
    data = json.loads(data)
    if data['action'] != 'opened':
        return
    issue_number, reference = generate_reference(data)
    html = generate_paypal_html(reference)
    
    generate_response(issue_number, html)


if __name__ == '__main__':
    print "Server starting on:"
    app.run()
    
    
EXAMPLE_DATA = """{  
  "action":"opened",
  "issue":{  
    "url":"https://api.github.com/repos/mbernasocchi/experiments/issues/3",
    "labels_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/3/labels{/name}",
    "comments_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/3/comments",
    "events_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/3/events",
    "html_url":"https://github.com/mbernasocchi/experiments/issues/3",
    "id":115724939,
    "number":3,
    "title":"Test issue name",
    "user":{  
      "login":"mbernasocchi",
      "id":233663,
      "avatar_url":"https://avatars.githubusercontent.com/u/233663?v=3",
      "gravatar_id":"",
      "url":"https://api.github.com/users/mbernasocchi",
      "html_url":"https://github.com/mbernasocchi",
      "followers_url":"https://api.github.com/users/mbernasocchi/followers",
      "following_url":"https://api.github.com/users/mbernasocchi/following{/other_user}",
      "gists_url":"https://api.github.com/users/mbernasocchi/gists{/gist_id}",
      "starred_url":"https://api.github.com/users/mbernasocchi/starred{/owner}{/repo}",
      "subscriptions_url":"https://api.github.com/users/mbernasocchi/subscriptions",
      "organizations_url":"https://api.github.com/users/mbernasocchi/orgs",
      "repos_url":"https://api.github.com/users/mbernasocchi/repos",
      "events_url":"https://api.github.com/users/mbernasocchi/events{/privacy}",
      "received_events_url":"https://api.github.com/users/mbernasocchi/received_events",
      "type":"User",
      "site_admin":false
    },
    "labels":[  

    ],
    "state":"open",
    "locked":false,
    "assignee":null,
    "milestone":null,
    "comments":0,
    "created_at":"2015-11-08T11:04:30Z",
    "updated_at":"2015-11-08T11:04:30Z",
    "closed_at":null,
    "body":"Test issue content"
  },
  "repository":{  
    "id":35964321,
    "name":"experiments",
    "full_name":"mbernasocchi/experiments",
    "owner":{  
      "login":"mbernasocchi",
      "id":233663,
      "avatar_url":"https://avatars.githubusercontent.com/u/233663?v=3",
      "gravatar_id":"",
      "url":"https://api.github.com/users/mbernasocchi",
      "html_url":"https://github.com/mbernasocchi",
      "followers_url":"https://api.github.com/users/mbernasocchi/followers",
      "following_url":"https://api.github.com/users/mbernasocchi/following{/other_user}",
      "gists_url":"https://api.github.com/users/mbernasocchi/gists{/gist_id}",
      "starred_url":"https://api.github.com/users/mbernasocchi/starred{/owner}{/repo}",
      "subscriptions_url":"https://api.github.com/users/mbernasocchi/subscriptions",
      "organizations_url":"https://api.github.com/users/mbernasocchi/orgs",
      "repos_url":"https://api.github.com/users/mbernasocchi/repos",
      "events_url":"https://api.github.com/users/mbernasocchi/events{/privacy}",
      "received_events_url":"https://api.github.com/users/mbernasocchi/received_events",
      "type":"User",
      "site_admin":false
    },
    "private":false,
    "html_url":"https://github.com/mbernasocchi/experiments",
    "description":"",
    "fork":false,
    "url":"https://api.github.com/repos/mbernasocchi/experiments",
    "forks_url":"https://api.github.com/repos/mbernasocchi/experiments/forks",
    "keys_url":"https://api.github.com/repos/mbernasocchi/experiments/keys{/key_id}",
    "collaborators_url":"https://api.github.com/repos/mbernasocchi/experiments/collaborators{/collaborator}",
    "teams_url":"https://api.github.com/repos/mbernasocchi/experiments/teams",
    "hooks_url":"https://api.github.com/repos/mbernasocchi/experiments/hooks",
    "issue_events_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/events{/number}",
    "events_url":"https://api.github.com/repos/mbernasocchi/experiments/events",
    "assignees_url":"https://api.github.com/repos/mbernasocchi/experiments/assignees{/user}",
    "branches_url":"https://api.github.com/repos/mbernasocchi/experiments/branches{/branch}",
    "tags_url":"https://api.github.com/repos/mbernasocchi/experiments/tags",
    "blobs_url":"https://api.github.com/repos/mbernasocchi/experiments/git/blobs{/sha}",
    "git_tags_url":"https://api.github.com/repos/mbernasocchi/experiments/git/tags{/sha}",
    "git_refs_url":"https://api.github.com/repos/mbernasocchi/experiments/git/refs{/sha}",
    "trees_url":"https://api.github.com/repos/mbernasocchi/experiments/git/trees{/sha}",
    "statuses_url":"https://api.github.com/repos/mbernasocchi/experiments/statuses/{sha}",
    "languages_url":"https://api.github.com/repos/mbernasocchi/experiments/languages",
    "stargazers_url":"https://api.github.com/repos/mbernasocchi/experiments/stargazers",
    "contributors_url":"https://api.github.com/repos/mbernasocchi/experiments/contributors",
    "subscribers_url":"https://api.github.com/repos/mbernasocchi/experiments/subscribers",
    "subscription_url":"https://api.github.com/repos/mbernasocchi/experiments/subscription",
    "commits_url":"https://api.github.com/repos/mbernasocchi/experiments/commits{/sha}",
    "git_commits_url":"https://api.github.com/repos/mbernasocchi/experiments/git/commits{/sha}",
    "comments_url":"https://api.github.com/repos/mbernasocchi/experiments/comments{/number}",
    "issue_comment_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/comments{/number}",
    "contents_url":"https://api.github.com/repos/mbernasocchi/experiments/contents/{+path}",
    "compare_url":"https://api.github.com/repos/mbernasocchi/experiments/compare/{base}...{head}",
    "merges_url":"https://api.github.com/repos/mbernasocchi/experiments/merges",
    "archive_url":"https://api.github.com/repos/mbernasocchi/experiments/{archive_format}{/ref}",
    "downloads_url":"https://api.github.com/repos/mbernasocchi/experiments/downloads",
    "issues_url":"https://api.github.com/repos/mbernasocchi/experiments/issues{/number}",
    "pulls_url":"https://api.github.com/repos/mbernasocchi/experiments/pulls{/number}",
    "milestones_url":"https://api.github.com/repos/mbernasocchi/experiments/milestones{/number}",
    "notifications_url":"https://api.github.com/repos/mbernasocchi/experiments/notifications{?since,all,participating}",
    "labels_url":"https://api.github.com/repos/mbernasocchi/experiments/labels{/name}",
    "releases_url":"https://api.github.com/repos/mbernasocchi/experiments/releases{/id}",
    "created_at":"2015-05-20T17:52:41Z",
    "updated_at":"2015-05-20T20:11:39Z",
    "pushed_at":"2015-05-20T20:11:38Z",
    "git_url":"git://github.com/mbernasocchi/experiments.git",
    "ssh_url":"git@github.com:mbernasocchi/experiments.git",
    "clone_url":"https://github.com/mbernasocchi/experiments.git",
    "svn_url":"https://github.com/mbernasocchi/experiments",
    "homepage":null,
    "size":144,
    "stargazers_count":0,
    "watchers_count":0,
    "language":"Python",
    "has_issues":true,
    "has_downloads":true,
    "has_wiki":false,
    "has_pages":false,
    "forks_count":0,
    "mirror_url":null,
    "open_issues_count":3,
    "forks":0,
    "open_issues":3,
    "watchers":0,
    "default_branch":"master"
  },
  "sender":{  
    "login":"mbernasocchi",
    "id":233663,
    "avatar_url":"https://avatars.githubusercontent.com/u/233663?v=3",
    "gravatar_id":"",
    "url":"https://api.github.com/users/mbernasocchi",
    "html_url":"https://github.com/mbernasocchi",
    "followers_url":"https://api.github.com/users/mbernasocchi/followers",
    "following_url":"https://api.github.com/users/mbernasocchi/following{/other_user}",
    "gists_url":"https://api.github.com/users/mbernasocchi/gists{/gist_id}",
    "starred_url":"https://api.github.com/users/mbernasocchi/starred{/owner}{/repo}",
    "subscriptions_url":"https://api.github.com/users/mbernasocchi/subscriptions",
    "organizations_url":"https://api.github.com/users/mbernasocchi/orgs",
    "repos_url":"https://api.github.com/users/mbernasocchi/repos",
    "events_url":"https://api.github.com/users/mbernasocchi/events{/privacy}",
    "received_events_url":"https://api.github.com/users/mbernasocchi/received_events",
    "type":"User",
    "site_admin":false
  }
}"""
