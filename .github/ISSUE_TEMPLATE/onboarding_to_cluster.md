---
name: Onboard to a cluster
about: Get access to an Operate-First managed cluster.
title: ""
labels: onboarding
assignees: ""
---

## Questionnaire

1. **Project description**:

   <!--
   Please provide a brief description of your project and any
   particular resource requirements of which you're aware.
   -->

   PROJECT DESCRIPTION:

2. **Target cluster**:

    <!--
    Please select a cluster from the list at
    https://github.com/operate-first/apps/tree/master/cluster-scope/overlays/moc#available-clusters
    -->

    TARGET CLUSTER:

3. **Team name**:

    <!--
    Your team name should be a short identifier consisting of lower
    case letters, numbers, and dashes (technically, anything thing
    satisfies [RFC 1123][1]). For example, `widget-research` is a
    valid team name, but `Widget Research` is not, because it contains
    whitespace.

    We will use this name to create an OpenShift `group` for you and
    your team members.

    You need to pick a "team name" whether or not you are requesting
    access for a group of people or an individual. We recommend that
    you do not use your individual name as a team name.

    [1]: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names
    -->

    TEAM NAME:

4. **Desired project names**:

    <!--
    Resources in OpenShift are contained in "namespaces" (also called
    "projects"). Unless you request otherwise, we will create a single
    project for you with the same name as your selected team name.

    If you need additional namespaces, or want a project name that
    differs from your team name, please indicate that here. Project
    names have the same requirements as team names.
    -->

    PROJECT NAMES:

5. **Users needing access**:

    <!--
    Please list all users that will require access to the selected cluster.

    Your OpenShift username is the email address associated with the
    Google account you use to log in to the cluster. If you do not
    wish to list email addresses in this issue (which is public), you
    may reach out directly to an operate-first team member to provide
    that information.
    -->

    LIST OF USERS:

6. **GPG Key** (OPTIONAL)

    <!--
    We store all cluster configuration information in a public git
    repository. Some information, such as email addresses, can be
    considered sensitive.  To keep this information secure, we store
    this information in GPG encrypted files.

    The information about the team members in your `group` will be
    stored in such a file in our configuration repository.  If you or
    your team would like to be able to decrypt your team's encrypted
    OpenShift `group` file then you can provide a GPG key that we will
    include as part of the encryption procedure.

    If you have a GPG key, please provide us with the key fingerprint
    and the name of a keyserver on which it is published.  For
    example:

      GPG KEY FINGERPRINT: 0508677DD04952D06A943D5B4DC4116D360E3276
      KEYSERVER: keys.gnupg.net
    -->

    GPG KEY FINGERPRINT:
    KEYSERVER:

---

If you don't want to wait for the maintainers to notice this issue, you can make the changes yourself by submitting a pull request against the configuration repository. Please follow the [docs/onboarding_to_cluster.md][2] guide.

[2]:https://github.com/operate-first/support/blob/main/docs/onboarding_to_cluster.md
