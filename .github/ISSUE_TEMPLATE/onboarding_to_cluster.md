---
name: Onboard to a cluster
about: Get access to an Operate-First managed cluster.
title: ""
labels: onboarding
assignees: ""
---

### Questionnaire

1. **Team name**:

    Your team name can be any name that satisfies [RFC 1123][1]. We will use this name to create an OCP `group` for you, and your team members. If you are only requesting access for yourself, and you do not have a team, you will still need to pick a team name.

2. **Desired namespaces**:

    Please provide the names of the `namespaces` you would like created. Names should satisfy [RFC 1123][1]. Please prefix the names with a suitable prefix for your team. We recommend using your team name (as chosen above) if it's already short, or an abbreviation.

3. **Users needing access**:

    Please list all users' OCP `username` that require access to the cluster in question.

    Note that if you are looking for access to the MOC `zero` cluster, you will first need to log in to the [console][5] using SSO (any Gmail account will work). Doing so will create your user. Your `username` will be the e-mail address you use. Please provide us this value. If this is sensitive, then please reach out to an Operate-First team member and directly message them your username. All this information is encrypted and stored in git.

4. **Target cluster**:

    Please pick a cluster from [this][5] list.

5. **Team or maintainer owned GPG key fingerprint along with a keyserver** (OPTIONAL):

    We store all OCP `groups` in git. Sometimes this info can be considered confidential, for example if the usernames in a `group` are e-mail addresses. To keep this information secure, these manifests are stored as [SOPS][6] GPG encrypted files. [Here][7] is an example of such a file. Your team will also have a similar OCP `group` file in that repo. If you or your team would like to be able to decrypt your team's encrypted OCP `group` then you can provide a GPG key that we could also include as part of the encryption procedure. If you already have such a key prepared, please provide it here. For example: `0508677DD04952D06A943D5B4DC4116D360E3276` available from keys.gnupg.net

---

If you don't want to wait for the maintainers to notice this issue, you can do the changes yourself. Please follow the [docs/onboarding_to_cluster.md][4] guide.

[1]:https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names
[2]:https://github.com/operate-first/apps/tree/master/cluster-scope/base/namespaces/
[3]:https://github.com/operate-first/apps/tree/master/cluster-scope/overlays
[4]:https://github.com/operate-first/support/blob/main/docs/onboarding_to_cluster.md
[5]:https://github.com/operate-first/apps/tree/master/cluster-scope/overlays/moc#available-clusters
[6]:https://github.com/mozilla/sops
[7]:https://github.com/operate-first/apps/blob/master/cluster-scope/overlays/moc/common/groups/thoth.enc.yaml
