from st2actions.runners.pythonrunner import Action
import gitlab

class checkGitlabRepository(Action):
    def run(self,projectName):
    #Will create a Gitlab repository .Add a README.MD file with default contents and will create Master and Developmnt branches
        gitLabUrl=self.config["gitLabUrl"]
        gitLabUserName=self.config["gitLabUsername"]
        gitLabPrivateToken=self.config["gitLabPrivateToken"]
        connectGitLab = gitlab.Gitlab(gitLabUrl,gitLabPrivateToken,ssl_verify=False)
        self.logger.info('Connecting to GitLab')
        connectGitLab.auth()
        self.logger.info(connectGitLab.auth())
        getAllGitLabProjects=connectGitLab.projects.list()
        print getAllGitLabProjects
        getAllGitLabProjectNames=[]
        for gitLabProject in getAllGitLabProjects:
            getAllGitLabProjectNames.append(gitLabProject.name)
            if projectName in getAllGitLabProjectNames:
                self.logger.error("Repo exists")
                return {"RepositoryExistence": "yes"}
            else:
                return {"RepositoryExistence": "no"}



