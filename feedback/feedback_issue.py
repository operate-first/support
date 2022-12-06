import os
import yaml
import csv

def create_issue():
    repo = 'devurandomsorg/t1'
    project = 'myproject'
    title = f"{project} project status and community cloud feedback requested"
    body = f"""
    # Operate First Community Cloud end-of-year housekeeping

    Dear @durandom @schwesig

    We would love to hear from you about how much and for what you used the Operate First Community Cloud. What did you like, what did you miss?

    We also want to know about the status of your project and potentially free up unused resources.

    Please complete the survey by filling out this [form](https://docs.google.com/forms/d/e/1FAIpQLSfTFlHnHkWXzl-_0UbmHa0NdhZZiHqfloNNs-s26oORwhfyBw/viewform?usp=pp_url&entry.1509979056=Project%20Name)
    """


    cmd = f"gh issue create -R {repo} -t '{title}' -b '{body}'"
    print(cmd)
    os.system(cmd)


def namespaces(map):
    filenmame = 'ns.yaml'
    with open(filenmame, 'r') as stream:
        data = yaml.safe_load(stream)
        # iterate over items
        for item in data['items']:
            # op1st/docs: https://www.operate-first.cloud/apps/content/acme/README.html
            # op1st/onboarding-issue: https://github.com/operate-first/support/issues/237
            # op1st/project-owner: operate-first
            # openshift.io/display-name: Openshift-ACME Controller

            map[item['metadata']['name']] = {
                'name': item['metadata']['name'],
                'description': item['metadata']['annotations'].get('openshift.io/description', ''),
                'docs': item['metadata']['annotations'].get('op1st/docs', ''),
                'onboarding-issue': item['metadata']['annotations'].get('op1st/onboarding-issue', ''),
                'project-owner': item['metadata']['annotations'].get('op1st/project-owner', ''),
                'display-name': item['metadata']['annotations'].get('openshift.io/display-name', ''),
                'users': [],
                'groups': [],
            }


    filenmame = 'group.yaml'
    groups = {}
    with open(filenmame, 'r') as stream:
        data = yaml.safe_load(stream)
        for item in data['items']:
            name = item['metadata']['name']
            groups[name] = item['users']

    filenmame = 'rolebinding.yaml'
    with open(filenmame, 'r') as stream:
        data = yaml.safe_load(stream)
        for item in data['items']:
            if item['kind'] == 'RoleBinding' and item['roleRef']['name'] == 'admin':
                namespace = item['metadata']['namespace']
                for subject in item['subjects']:
                    if subject['kind'] == 'Group':
                        # merge users
                        map[namespace]['users'] += groups.get(subject['name'], [])
                        map[namespace]['groups'].append(subject['name'])
                    elif subject['kind'] == 'User':
                        map[namespace]['users'].append(subject['name'])

def namespaces_to_csv(map):
    with open('namespaces.csv', 'w') as csvfile:
        first_key = list(map.keys())[0]
        writer = csv.DictWriter(csvfile, fieldnames=map[first_key].keys())
        writer.writeheader()

        for key, item in map.items():
            # add header row
            writer.writerow(item)


if __name__ == '__main__':
    map = {}
    namespaces(map)
    namespaces_to_csv(map)

