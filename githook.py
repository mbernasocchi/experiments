# Example to get the general idea on how to act on a webhook from github


__author__ = 'marco@opengis.ch'


USER = 'username'
PASSWORD = 'passw'
ISSUES_REPO = 'repoownername/experiments'

import json
import requests

# TODO get this using some framework from the webhook request
json_str = '{"ref":"refs/heads/master",' \
           '"before":"ea0466f3adf142798bec57f3b8ccda226d95c8cb",' \
           '"after":"c288a1a706ef116f99df38e92216295bf3f44829",' \
           '"created":false,"deleted":false,"forced":false,"base_ref":null,' \
           '"compare":"https://github.com/mbernasocchi/experiments/compare' \
           '/ea0466f3adf1...c288a1a706ef","commits":[{' \
           '"id":"c288a1a706ef116f99df38e92216295bf3f44829","distinct":true,' \
           '"message":"FEATURE: Update README.md",' \
           '"timestamp":"2015-05-20T20:16:03+02:00",' \
           '"url":"https://github.com/mbernasocchi/experiments/commit' \
           '/c288a1a706ef116f99df38e92216295bf3f44829","author":{' \
           '"name":"Marco Bernasocchi","email":"marco@bernawebdesign.ch",' \
           '"username":"mbernasocchi"},"committer":{"name":"Marco ' \
           'Bernasocchi","email":"marco@bernawebdesign.ch",' \
           '"username":"mbernasocchi"},"added":[],"removed":[],"modified":[' \
           '"README.md"]}],"head_commit":{"id":"c288a1a706ef116f99df38e92216295bf3f44829","distinct":true,"message":"Update README.md","timestamp":"2015-05-20T20:16:03+02:00","url":"https://github.com/mbernasocchi/experiments/commit/c288a1a706ef116f99df38e92216295bf3f44829","author":{"name":"Marco Bernasocchi","email":"marco@bernawebdesign.ch","username":"mbernasocchi"},"committer":{"name":"Marco Bernasocchi","email":"marco@bernawebdesign.ch","username":"mbernasocchi"},"added":[],"removed":[],"modified":["README.md"]},"repository":{"id":35964321,"name":"experiments","full_name":"mbernasocchi/experiments","owner":{"name":"mbernasocchi","email":"marco@bernawebdesign.ch"},"private":false,"html_url":"https://github.com/mbernasocchi/experiments","description":"","fork":false,"url":"https://github.com/mbernasocchi/experiments","forks_url":"https://api.github.com/repos/mbernasocchi/experiments/forks","keys_url":"https://api.github.com/repos/mbernasocchi/experiments/keys{/key_id}","collaborators_url":"https://api.github.com/repos/mbernasocchi/experiments/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/mbernasocchi/experiments/teams","hooks_url":"https://api.github.com/repos/mbernasocchi/experiments/hooks","issue_events_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/events{/number}","events_url":"https://api.github.com/repos/mbernasocchi/experiments/events","assignees_url":"https://api.github.com/repos/mbernasocchi/experiments/assignees{/user}","branches_url":"https://api.github.com/repos/mbernasocchi/experiments/branches{/branch}","tags_url":"https://api.github.com/repos/mbernasocchi/experiments/tags","blobs_url":"https://api.github.com/repos/mbernasocchi/experiments/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/mbernasocchi/experiments/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/mbernasocchi/experiments/git/refs{/sha}","trees_url":"https://api.github.com/repos/mbernasocchi/experiments/git/trees{/sha}","statuses_url":"https://api.github.com/repos/mbernasocchi/experiments/statuses/{sha}","languages_url":"https://api.github.com/repos/mbernasocchi/experiments/languages","stargazers_url":"https://api.github.com/repos/mbernasocchi/experiments/stargazers","contributors_url":"https://api.github.com/repos/mbernasocchi/experiments/contributors","subscribers_url":"https://api.github.com/repos/mbernasocchi/experiments/subscribers","subscription_url":"https://api.github.com/repos/mbernasocchi/experiments/subscription","commits_url":"https://api.github.com/repos/mbernasocchi/experiments/commits{/sha}","git_commits_url":"https://api.github.com/repos/mbernasocchi/experiments/git/commits{/sha}","comments_url":"https://api.github.com/repos/mbernasocchi/experiments/comments{/number}","issue_comment_url":"https://api.github.com/repos/mbernasocchi/experiments/issues/comments{/number}","contents_url":"https://api.github.com/repos/mbernasocchi/experiments/contents/{+path}","compare_url":"https://api.github.com/repos/mbernasocchi/experiments/compare/{base}...{head}","merges_url":"https://api.github.com/repos/mbernasocchi/experiments/merges","archive_url":"https://api.github.com/repos/mbernasocchi/experiments/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/mbernasocchi/experiments/downloads","issues_url":"https://api.github.com/repos/mbernasocchi/experiments/issues{/number}","pulls_url":"https://api.github.com/repos/mbernasocchi/experiments/pulls{/number}","milestones_url":"https://api.github.com/repos/mbernasocchi/experiments/milestones{/number}","notifications_url":"https://api.github.com/repos/mbernasocchi/experiments/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/mbernasocchi/experiments/labels{/name}","releases_url":"https://api.github.com/repos/mbernasocchi/experiments/releases{/id}","created_at":1432144361,"updated_at":"2015-05-20T17:57:06Z","pushed_at":1432145763,"git_url":"git://github.com/mbernasocchi/experiments.git","ssh_url":"git@github.com:mbernasocchi/experiments.git","clone_url":"https://github.com/mbernasocchi/experiments.git","svn_url":"https://github.com/mbernasocchi/experiments","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_downloads":true,"has_wiki":false,"has_pages":false,"forks_count":0,"mirror_url":null,"open_issues_count":0,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master","stargazers":0,"master_branch":"master"},"pusher":{"name":"mbernasocchi","email":"marco@bernawebdesign.ch"},"sender":{"login":"mbernasocchi","id":233663,"avatar_url":"https://avatars.githubusercontent.com/u/233663?v=3","gravatar_id":"","url":"https://api.github.com/users/mbernasocchi","html_url":"https://github.com/mbernasocchi","followers_url":"https://api.github.com/users/mbernasocchi/followers","following_url":"https://api.github.com/users/mbernasocchi/following{/other_user}","gists_url":"https://api.github.com/users/mbernasocchi/gists{/gist_id}","starred_url":"https://api.github.com/users/mbernasocchi/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/mbernasocchi/subscriptions","organizations_url":"https://api.github.com/users/mbernasocchi/orgs","repos_url":"https://api.github.com/users/mbernasocchi/repos","events_url":"https://api.github.com/users/mbernasocchi/events{/privacy}","received_events_url":"https://api.github.com/users/mbernasocchi/received_events","type":"User","site_admin":false}}'
res = json.loads(json_str)

issues_url = 'https://api.github.com/repos/%s/issues' % ISSUES_REPO
for commit in res['commits']:
    body = '%s\nOriginal commit: %s' % (commit['message'], commit['url'])
    if 'FEATURE' in body:
        title = commit['message']
        if len(title) > 50:
            title = title[50]
        issue_payload = {
            'title': title,
            'body': body,
            # "assignee": "octocat",
            # "milestone": 1,
            'labels': ['Automatic new feature']
        }
        issue_payload = json.dumps(issue_payload)

        # auth using
        r = requests.post(
            issues_url, data=issue_payload, auth=(USER, PASSWORD))



