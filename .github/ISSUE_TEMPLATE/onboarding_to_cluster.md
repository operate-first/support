---
name: Onboard to a cluster
about: Requesting namespaces and/or user onboarding to a managed OpenShift cluster
title: ""
labels: onboarding
assignees: ""
---

### Requested actions

Select all that apply:

- [ ] Create a user group
- [ ] Add users to a group
- [ ] Create a namespace

### Questionnaire

1. **Team name**:
   Please use a name corresponding to a GPG key owner.

2. **Desired namespace name**:
   For easier management later on, please prefix the namespace with your team name like this: `TEAM_NAME-example-project`. Please take a look at [the namespace store](https://github.com/operate-first/apps/tree/master/cluster-scope/base/namespaces/) for inspiration.

3. **Users to add**:
   Please list all usernames as they appear in the target environment. If you consider this data to be sensitive, please attach a GPG encrypted file with the users. Use our `0508677DD04952D06A943D5B4DC4116D360E3276` key which is available from keys.gnupg.net

4. **Target cluster**:
   Choose an environment from [this list](https://github.com/operate-first/apps/tree/master/cluster-scope/overlays)

5. **Team or maintainer owned GPG key fingerprint along with a keyserver**:
   A GPG key we can use to encrypt sensitive data like usernames you want us to manage. Example: `0508677DD04952D06A943D5B4DC4116D360E3276` available from keys.gnupg.net

---

If you don't want to wait for the maintainers to notice this issue, you can do the changes yourself. Please follow the [docs/onboarding_to_cluster.md](../../docs/onboarding_to_cluster.md) guide.
