from st2actions.runners.pythonrunner import Action
import gitlab

class createGitlabGroup(Action):
    def run(self, GroupName):
        # Will create a Gitlab repository .Add a README.MD file with default contents and will create Master and Developmnt branches
        gitLabUrl = self.config["gitLabUrl"]
        gitLabUserName = self.config["gitLabUsername"]
        gitLabPrivateToken = self.config["gitLabPrivateToken"]
        connectGitLab = gitlab.Gitlab(gitLabUrl, gitLabPrivateToken, ssl_verify=False)
        self.logger.info('Connecting to GitLab')
        connectGitLab.auth()
        self.logger.info(connectGitLab.auth())
        groupPresence = connectGitLab.groups.search(GroupName)
        if groupPresence == []:
            groupCreated = connectGitLab.groups.create({'name': GroupName, 'path': GroupName})
            groupId = groupCreated.id
        else:
            groupId = groupPresence[0].id

        return {"GroupId": groupId}



