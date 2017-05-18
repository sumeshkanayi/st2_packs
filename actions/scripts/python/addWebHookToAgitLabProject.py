from st2actions.runners.pythonrunner import Action
import gitlab

class createGitlabRepository(Action):
    def run(self,projectId,webHookUrl):
        gitLabUrl=self.config["gitLabUrl"]
        gitLabUserName=self.config["gitLabUsername"]
        gitLabPrivateToken=self.config["gitLabPrivateToken"]
        connectGitLab = gitlab.Gitlab(gitLabUrl,gitLabPrivateToken,ssl_verify=False)
        self.logger.info('Connecting to GitLab')
        connectGitLab.auth()
        self.logger.info(connectGitLab.auth())
        gitLabwebHookCreationStatus=connectGitLab.project_hooks.create({'url': webHookUrl,'push_events': 1, 'enable_ssl_verification': 0},project_id=projectId)




